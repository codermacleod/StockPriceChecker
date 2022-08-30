import yfinance as yf
import streamlit as st
import datetime as dt 
from dateutil.relativedelta import relativedelta


st.title("Stock Price Checker")
st.header("Apple, Google and Tesla")


today = dt.date.today()
years_ago = today-relativedelta(years=10)

#define tickers
tickers = yf.Tickers('tsla aapl googl')
#get the historical prices for this ticker
tickerDf = tickers.history(period='20y')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.subheader("Close")
st.line_chart(tickerDf.Close)
st.subheader("Volume")
st.line_chart(tickerDf.Volume)
