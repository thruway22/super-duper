import streamlit as st
import utilities as utl
import plotly.express as px

st.title('Saudi REITs')
ticker = st.selectbox('Choose fund', utl.tickers.keys(),
                      label_visibility='collapsed', format_func=lambda x:utl.tickers[x])

if ticker != 9999:
    ts = utl.get_ticker_timeseries(ticker)
    ct = utl.get_ticker_categorical(ticker, 'full-year')
    st.table(ts.head())

    fig = px.line(ts, x=ts.index, y=['price', 'nav'])
    st.plotly_chart(fig)