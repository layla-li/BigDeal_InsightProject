# BigDeal
## Find the best deal at the right time
A web app that predicts the next best deal for online shoppers to help them save both money and time.

App Link: https://bigdeal.herokuapp.com/

## Problem/context:
For online shoppers, getting good deals helps a lot in terms of saving money. However, hunting discount online can be time consuming. Morever, people are not sure when is the bet time to buy and whether the current discount is good enough. BigDeal directly provides users the prediction about the upcoming discount information, as well as suggestion about when is the right time to get the best discount. 
### 1. Data Collection:
I scraped over 10,000 historical sales events using Python Selenium from two major websites which are the leading and most trusted online community dedicated to sharing, rating and reviewing deals. 
### 2. Data Cleaning:
The original data was messy with a lot of texts. I extracted Useful information, like the amount of deal for a particular brand from the deal description and what day the deal was posted on the website, etc. I performed regular expression to get my final clean data.
### 3. Feature Engineering:
(1). *Seasonality features:*

Month of year, Day of year, Day of week, Distance to major holidays, etc.

(2). *Autocorrelation features:*

Discount past 1 day, Discount past 2 days, Discount past 3 days...Discount past 7 days

(3). *Other statistical features:*

Max discount past 15 days, Average discount past 15 days, Max discount past 30 days, Average discount past 30 days, etc.
### 4. Modeling:
Logistic Regression

Random Forest

XGBoost



