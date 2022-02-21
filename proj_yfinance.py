import yfinance as yf
import streamlit as st
import pandas as pandas

current_ticker = "GOOGL"

st.write("""
#### Simple Stock Price App 
# * **Credit:** Project guided by dataprofessor on freeCodeCamp.org, tutorial link: (https://www.youtube.com/watch?v=JwSS70SZdyM&t=11s)""")
current_ticker = st.text_input("Selected Ticker: ", value="GOOGL", max_chars=10, type="default")

ticker_data = yf.Ticker(current_ticker)

try:
    ticker_df = ticker_data.history(period="1d", start='2020-01-01', end="2022-02-18")
    if 'Empty DataFrame' in str(ticker_df):
        raise Exception('Empty DataFrame - might be caused by an invalid symbol')
    else:
        message = f"""The daily stock closing price and volume of **{current_ticker}** are shown below"""
        st.write(message)
        st.write("""##### Closing Price """)
        st.line_chart(ticker_df.Close)
        st.write("""##### Volume """)
        st.line_chart(ticker_df.Volume)

except Exception as e:
    message = f"""**{current_ticker}** is not found. Check https://finance.yahoo.com/ for the list of valid tickers"""
    st.write(message)




