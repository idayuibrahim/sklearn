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
from sklearn.linear_model import LinearRegression

st.title("Stock Price Prediction App")

option = st.sidebar.selectbox(
    'Stock Price Data Processing',
     ['Home','Data Frame','Cleaning','Prediction']
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
    st.write('Before you continue, please read the [stock market terms and glossary](https://www.nasdaq.com/glossary/a)')
    show = st.checkbox('I have read and understand')
    if show:
        st.write("""
## Lets start the stock price prediction!
""")
elif option=='Data Frame':
    st.write("This is the raw data with the selected features for the analysis")
    data1 = data[['Close','Volume','SPV','CHG']]
    st.write('SPV (Spread Volatility) is differences between High and Low divided by Close price multiplied by 100') 
    st.write('CHG (Change) is percentage difference between Close and Open price') 
    st.write('Data Frame')
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


else:
    'Starting a long computation...'

    
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
   
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    '...and now we\'re done!'
