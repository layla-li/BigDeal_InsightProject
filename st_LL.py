import pandas as pd
import streamlit as st
import os
import re
import numpy as np
import pandas as pd
import seaborn as sns
import pickle
from datetime import datetime, timedelta
from PIL import Image


st.title('BigDeal')
st.header('Find the best deal at the right time!')
#st.markdown("> XXX")

# Define display function to show historical deals info using streamlit slider as an interactive way
def display(brand):
    df = pd.read_csv('Datasets/' + brand + '_features.csv')
    if st.checkbox('Show dataframe'): 
        st.write(df)
    yslider = st.slider('Please choose the year:', 2015, 2019)
    #st.slider('year: ', df["year"].min(), df["year"].max())
    data_year = df[df['discount_today'] == 1][(df['year'] == yslider) & (df['Y_avg_discount_1d'] > 40)].copy()
    sns.countplot(x = 'month', data = data_year)    
    st.pyplot()

# Define image function to show the prediction image
def image(brand):
    image = Image.open('Datasets/figures/' + brand + '.png')
    st.image(image, caption='', use_column_width=True)
   
    
category = ['baby/kids', 'beauty', 'fashion']
choose = st.radio('Please choose the product category:', category)
if choose == 'baby/kids':
    brand = ['Carters', 'Oshkosh', 'Hanna Andersson', 'Janie&Jack']
    deal = st.selectbox('Please choose the brand:', brand)
    if deal == 'Carters':
        st.header("Suggestion is: ")
        st.markdown("Best deal will happen in 3 days for " + deal + "!")
        image(deal)
        display(deal)
    elif deal == 'Oshkosh':
        st.header("Suggestion is: ")
        st.markdown("Best deal will happen in 7 days for " + deal + "!")
        image(deal)
        display(deal)
elif choose == 'beauty':
    brand = ['EsteeLauder', 'Clinique']
    deal = st.selectbox('Please choose the brand:', brand)
    if deal == 'EsteeLauder':
        st.header("Suggestion is: ")
        st.markdown('Best deal for ' + deal + 'is now!')
        image(deal)
        display(deal)
    elif deal == 'Clinique':
        st.header("Suggestion is: ")
        st.markdown("Best deal will happen in 7 days for " + deal + "!")
        image(deal)
        display(deal)
elif choose == 'fashion':
    brand = ['Gap', 'Jcrew']
    deal = st.selectbox('Please choose the brand:', brand)
    if deal == 'Gap':
        st.header("Suggestion is: ")
        st.markdown("Best deal will happen in 7 days for " + deal + "!")
        image(deal)
        display(deal)
    elif deal == 'Jcrew':
        st.header("Suggestion is: ")
        st.markdown("Best deal will happen in 14 days for " + deal + "!")
        image(deal)
        display(deal)
#         df = pd.read_csv("Datasets/Carters_features.csv")
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

