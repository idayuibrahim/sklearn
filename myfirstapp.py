import streamlit as st
import math
import numpy as np
import pandas as pd
import datetime
import time

import yfinance as yf

import matplotlib.pyplot as plt
from matplotlib import style
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, svm
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM

st.title("Stock Price Prediction App")

option = st.sidebar.selectbox(
    'Stock Price Data Processing',
     ['Home','Data Frame','Cleaning','SVR & Linear Regression']
)
    
StockCode = st.text_input('Please enter the stock code:','SPY')
StartDate = "2015-01-01"
EndDate = st.text_input('Please enter the end date',str(datetime.datetime.today()).split()[0])
if StockCode == "" or EndDate == "" :
    st.write("Welcome to my simple stock price app!")
else:
    data = yf.download(StockCode, start=StartDate, end=EndDate)
    
data = yf.download(StockCode, start=StartDate, end=EndDate)    
data['SPV'] = ((data['High'] - data['Low']) / data['Close'])*100
data['CHG'] = ((data['Close'] - data['Open']) / data['Open'])*100
    
    
data1 = data[['Close','Volume','SPV','CHG']]
data1.fillna(value=-99999, inplace = True)

    
if option=='Home' or option=="" :
    st.header("Main Page")
    st.write("This is the main page of the stock price prediction app")
    st.write('Before you continue, you may read the [stock market terms and glossary](https://www.nasdaq.com/glossary/a) for better understanding on the indicator used')
    show = st.checkbox('I have read and understand')
    if show:
        st.write("""
## Lets start the stock price prediction!
""")
        st.write("""
### Prepared by Nur Idayu Ibrahim
""")
elif option=='Data Frame':
    st.write("This is the raw data with the selected features for the analysis")
    st.write('SPV (Spread Volatility) is differences between High and Low divided by Close price multiplied by 100') 
    st.write('CHG (Change) is percentage difference between Close and Open price') 
    st.write('Data Frame')
    data1 = data[['Close','Volume','SPV','CHG']]
    st.write(data1)
    st.write("""
## Closing Price
""")
    st.line_chart(data1.Close)
    st.write("""
## Volume
""")
    st.line_chart(data1.Volume)
    st.write("""
## SPV
""")
    st.line_chart(data1.SPV)
    st.write("""
## CHG
""")
    st.line_chart(data1.CHG)
    

elif option=='Cleaning':
    data1.fillna(value=-99999, inplace = True)
    st.write(data1)


elif option=='SVR & Linear Regression':
    Forecast_Out = int(math.ceil(0.01*len(data1)))
    data1['PredictionOutput'] = data['Close'].shift (-Forecast_Out)
    st.write('Prediction Output Length : ')
    st.write((Forecast_Out), 'days ahead. ')
    
    st.write(' SVR (Support Vector Regression) prediction accuracy : ')
    X = np.array(data1.drop(['PredictionOutput'],1))
    X = preprocessing.scale(X)
    X_predict = X[-Forecast_Out:]
    X = X[:-Forecast_Out]
    data1.dropna(inplace=True)
    y = np.array(data1['PredictionOutput'])
    
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2)
    clf = svm.SVR()
    clf.fit(X_train,  y_train)
    Confidence = clf.score(X_test, y_test)
    st.write(Confidence)
    setPrediction0 = clf.predict(X_predict)
    st.write('Prediction output using SVR: ')
    st.write(setPrediction0)
    
    
    st.write(' Linear Regression prediction accuracy : ')
    clf = LinearRegression(n_jobs=-1)
    clf.fit(X_train, y_train)
    Confidence2 = clf.score(X_test, y_test)
    st.write(Confidence2)
    
    st.write('Prediction output using Linear Regression: ')
    setPrediction = clf.predict(X_predict)
    st.write(setPrediction)
    st.write("""
## Stock price prediction
""")
    
    st.line_chart(setPrediction)
    
#     data1['Prediction'] = np.nan
    
#     lastDate = data1.iloc[-1].name
    
#     lastSecond = lastDate.timestamp()
#     oneDay = 86400
#     nextSecond = lastSecond + oneDay


#     for i in setPrediction :
#         nextDate = datetime.datetime.fromtimestamp(nextSecond)
#         nextSecond += 86400
#         data1.loc[nextDate] = np.nan for _ in range(len(data1.columns)-1)]+[i]
#         data1['Close'].plot()
#         data1['Prediction'].plot()
#         plt.legend
#         plt.xlabel('Year')
#         plt.ylabel('Price')
#         plt.title(StockPrice + 'Stock price prediction')
#         legend = plt.show

        

   
    
    
    
 
    
    
    
    
    
    

