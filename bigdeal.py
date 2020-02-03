import pandas as pd
import streamlit as st
import os
import re
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import pickle
from datetime import datetime, timedelta
from PIL import Image
import random


st.title('BigDeal')
st.header('Find the best deal at the right time!')
    
def plot(brand=None, thresholds=[0, 10, 50, 100], **kwargs):
    
    df = pd.read_csv('Datasets/' + brand + '_features.csv')
    random.seed(236) 

    fig_x = kwargs["fig_x"] if "fig_x" in kwargs else 6.0
    fig_y = kwargs["fig_y"] if "fig_y" in kwargs else 6.0
    title = kwargs["title"] if "title" in kwargs else "Prediction for %s"%brand
    out_name = kwargs["out_name"] if "out_name" in kwargs else "figures/"+brand
    out_type = kwargs["out_type"] if "out_type" in kwargs else ["png"]
    label_y = kwargs["label_y"] if "label_y" in kwargs else "Predication in N days"
    label_x = kwargs["label_x"] if "label_x" in kwargs else "Discount in %"
    lim_y = kwargs["lim_y"] if "lim_y" in kwargs else [99, -99]
    lim_x = kwargs["lim_x"] if "lim_x" in kwargs else [-50, 50]

    data = df
    nd_list=[1, 3, 7, 14]
    mean, up, down = [], [], []
    for j in nd_list:
        col = "Y_avg_discount_%dd"%j
        last_val = data[col].iloc[-1]
        idx = random.randint(0, len(data))
        last_val = data[col].iloc[idx]
        igroup = -1
        for ig in range(1, len(thresholds)):
            if last_val >= thresholds[ig-1] and last_val < thresholds[ig]:
                igroup = ig
                break
        print(brand, j, igroup)
        dt_slice = data[(data[col]>=thresholds[igroup-1]) & (data[col]<thresholds[igroup])]
        m = dt_slice[col].mean()
        mean.append(m)
        sigma = dt_slice[col].std()
        up.append(95 if m+sigma>=95 else m+sigma)
        down.append(1 if m-sigma<=1 else m-sigma)
    
    
    plt.figure(figsize=(fig_x,fig_y))
    plt.fill_between(nd_list, up, down, color='blue', alpha=0.25, label='__nolabel__')
    plt.plot(nd_list, mean, "o-", color='orangered', label="__nolabel__")
    plt.ylim(0, 100)
    plt.grid()
    plt.xlabel(label_y)                 
    plt.ylabel(label_x)                   
    plt.title(title)
    st.pyplot()
    
    # return the number of days in nd_list for the best discount
    m = max(mean)
    idx = [i for i, j in enumerate(mean) if j == m][0]
    return nd_list[idx]

# Define display function to show historical deals info using streamlit slider as an interactive way
def display(brand):
    st.header('Here is some fun fact about historical data!')
    df = pd.read_csv('Datasets/' + brand + '_features.csv')
    if st.checkbox('Show dataframe'): 
        st.write(df)
    data_year_1 = df[df['discount_today'] == 1][(df['Y_avg_discount_1d'] > 0)].copy()
    data_year_11 = df[(df['Y_avg_discount_1d'] < 100)].copy()
    data_year_2 = df[df['discount_today'] == 1][(df['Y_avg_discount_1d'] > 0)].copy()
    data_year_22 = df[(df['Y_avg_discount_1d'] <= 50)].copy() 
    data_year_3 = df[df['discount_today'] == 1][(df['Y_avg_discount_1d'] > 0)].copy()
    data_year_33 = df[(df['Y_avg_discount_1d'] <= 25)].copy()
    sns.countplot(x = 'month', data = data_year_11, color='Green') # discount > 50% 
    sns.countplot(x = 'month', data = data_year_22, color='blue') # 25% < discount <= %50
    sns.countplot(x = 'month', data = data_year_33, color='red') # discount <= 25%
    bottom, top = plt.ylim()
    plt.legend(['discount > 50%', '25% < discount <= %50', 'discount <= 25%'])
    plt.ylim(bottom, top*1.25)
    st.pyplot()

    yslider = st.slider('Do you know which month has the most deals? Please choose the year:', 2015, 2019, 2016)
    #st.slider('year: ', df["year"].min(), df["year"].max())
    data_year = df[df['discount_today'] == 1][(df['year'] == yslider) & (df['Y_avg_discount_1d'] > 0)].copy()
    sns.countplot(x = 'month', data = data_year) # discount > 50% 
    st.pyplot()

def message_deal(best_in_days, brand):
    message_dict = {
        1: "Best deal will happen tomorrow for %s! Go for it!"%brand,
        3: "Best deal will happen in 3 days for %s! Check back shortly!"%brand,
        7: "Best deal will happen in 1 week for %s! Please wait and come back in a few days!"%brand,
        14: "Best deal will happen in 2 weeks for %s! Please be patient and come back later!"%brand
    }
    if best_in_days not in message_dict:
        return "ERROR! Use best_in_days = 1, 3, 7 or 14!"
    return message_dict[best_in_days]
    
category = ['baby/kids', 'beauty', 'fashion']
brands_dict = {
    'baby/kids': ['', 'Carters', 'Oshkosh', 'Hanna Andersson', 'Janie&Jack'],
    'beauty': ['', 'Lancome', 'EsteeLauder', 'Clinique'],
    'fashion': ['', 'Gap', 'Jcrew']
}
choose = st.radio('Please choose the product category:', category)
deal = st.selectbox('Please choose the brand:', 
                    brands_dict[choose], format_func=lambda x: 'Select an option' if x == '' else x)
if deal != "":
    #st.header(deal)
    ndays = plot(deal)
    st.header("Suggestion is: ")
    st.markdown(message_deal(ndays, deal))
    display(deal)






# if choose == 'baby/kids':
#     deal = st.selectbox('Please choose the brand:', ['', 'Carters', 'Oshkosh', 'Hanna Andersson', 'Janie&Jack'], format_func=lambda x: 'Select an option' if x == '' else x)
    
#     if deal == 'Carters':
#         st.header("Suggestion is: ")
#         st.markdown("Best deal will happen in 3 days for " + deal + "!")
#         plot(deal)
#         display(deal)
#     elif deal == 'Oshkosh':
#         st.header("Suggestion is: ")
#         st.markdown("Best deal will happen in 7 days for " + deal + ". You should wait and come back in a few days!!")          
#         plot(deal)
#         display(deal)
# elif choose == 'beauty':
#     deal = st.selectbox('Please choose the brand:', ['', 'Lancome', 'EsteeLauder', 'Clinique'], format_func=lambda x: 'Select an option' if x == '' else x)
#     if deal == 'EsteeLauder':
#         st.header("Suggestion is: ")
#         st.markdown('Best deal for ' + deal + 'is now. Go for it!') 
#         plot(deal)
#         display(deal)
#     elif deal == 'Clinique':
#         st.header("Suggestion is: ")
#         st.markdown("Best deal will happen in 7 days for " + deal + ". You should wait and come back in a few days!!")
#         plot(deal)
#         display(deal)
# elif choose == 'fashion':
#     deal = st.selectbox('Please choose the brand:', ['', 'Gap', 'Jcrew'], format_func=lambda x: 'Select an option' if x == '' else x)
#     if deal == 'Gap':
#         st.header("Suggestion is: ")
#         st.markdown("Best deal will happen in 7 days for " + deal + ". You should wait and come back in a few days!!")
#         plot(deal)
#         display(deal)
#     elif deal == 'Jcrew':
#         st.header("Suggestion is: ")
#         st.markdown("Best deal will happen in 14 days for " + deal + ". You should wait and come back in a few days!")
#         plot(deal)
#         display(deal)

#         if st.checkbox('Show dataframe'): 
#             st.write(df)
#         yslider = st.slider('Please choose the year:', 2013, 2020)
#         #st.slider('year: ', df["year"].min(), df["year"].max())
#         data_year = df[df["discount_today"] == 1][(df["year"] == yslider) & (df["Y_avg_discount_1d"] > 40)].copy()
#         sns.countplot(x = "month", data = data_year)    
#         st.pyplot()
        
 

         #rf = RandomForestClassifier()
#         #rf.fit(X_train, y_train)
#         x0 = {'ndays_of_deal': [1], 
#           'avg_comments':[10], 
#           'avg_bookmarks':[12], 
#           'avg_shares':[8], 
#           'year':[2020], 
#           'month':[1], 
#           'day':[23], 
#           'weekday':[4]}
#         x0_pd = pd.DataFrame(x0)
#         y0 = pickle_model.predict(x0_pd)
#         if y0 == 1:
#             st.markdown("Yes, there is a deal in 3 days!")
#         elif y0 == 0:
#             st.markdown("No deal")


# add_selectbox = st.sidebar.selectbox(
#     'Which year?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# Adds a slider to the sidebar
#add_slider = st.sidebar.slider(
#    'Select which year',
#    0.0, 100.0, (25.0, 75.0)
#)  

