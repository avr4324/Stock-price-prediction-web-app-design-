import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model
import streamlit as st
import yfinance as yf

start = '2010-01-04'
end = '2019-12-30'

st.title('Stock trend Prediction')
user_input = st.text_input("Enter Stock Ticker", 'AAPL')
df = yf.download('AAPL', start=start, end=end)

st.subheader('Data from 2010-2019')
st.write(df.describe())