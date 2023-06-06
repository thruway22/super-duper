import streamlit as st
import utilities as utl

st.title('Saudi REITs')
ticker = st.selectbox('Choose fund', utl.tickers.keys(),
                      label_visibility='collapsed', format_func=lambda x:utl.tickers[x])

st.table(utl.get_ticker_timeseries(ticker))
st.table(utl.get_ticker_categorical(ticker, 'full-year'))