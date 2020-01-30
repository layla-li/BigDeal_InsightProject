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


st.title("BigDeal")
st.header("Find the best deal at the right time!")
#st.markdown("> XXX")

def display(brand):
    df = pd.read_csv("Datasets/" + brand + "_features.csv")
    if st.checkbox('Show dataframe'): 
        st.write(df)
    yslider = st.slider('Please choose the year:', 2015, 2019)
    #st.slider('year: ', df["year"].min(), df["year"].max())
    data_year = df[df["discount_today"] == 1][(df["year"] == yslider) & (df["Y_avg_discount_1d"] > 40)].copy()
    sns.countplot(x = "month", data = data_year)    
    st.pyplot()
    
category = ['baby/kids', 'beauty', 'fashion'] 
choose = st.radio('Please choose the product category:', category)
if choose == 'baby/kids':
    brand = ['Carters', 'Oshkosh', 'Hanna Andersson', 'Janie&Jack']
    deal = st.selectbox('Please choose the brand:', brand)
    if deal == 'Carters':
        st.header("Suggestion is: XXX")
        st.markdown("XXX")
        display(deal)
    elif deal == 'Oshkosh':
        display(deal)
elif choose == 'beauty':
    brand = ['Estee Lauder', 'Clinique']
    deal = st.selectbox('Please choose the brand:', brand)
    if deal == 'Estee Lauder':
        display(deal)
    elif deal == 'Clinique':
        display(deal)
elif choose == 'fashion':
    brand = ['Gap', 'Jcrew']
    deal = st.selectbox('Please choose the brand:', brand)
    if deal == 'Gap':
        display(deal)
    elif deal == 'Jcrew':
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

#Image

image = Image.open('/Users/universebright/Desktop/sunrise.jpg')
st.image(image, caption='Sunrise by the mountains', use_column_width=True)
