import pandas as pd
import streamlit as st
import os
import re
import numpy as np
import pandas as pd
import seaborn as sns
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from collections import Counter

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
#from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC

st.title("DealTime")
st.markdown("Predicting next best deals")
#st.header("XXXX")
#st.markdown("> XXX")

df = pd.read_csv("Carters_feature.csv")
if st.checkbox('Show dataframe'):
     st.write(df)

#species = st.multiselect('Show iris per variety?', df['year'].unique())
#col1 = st.selectbox('Which feature on x?', df.columns[0:4])
#col2 = st.selectbox('Which feature on y?', df.columns[0:4])
#new_df = df[(df['year'].isin(species))]
#st.write(new_df)
#fig = px.scatter(new_df, x =col1,y=col2, color='variety')
#st.plotly_chart(fig)
