import streamlit as st
import utilities as utl

st.title('Saudi REITs')
ticker = st.selectbox('Choose fund', utl.tickers.keys(),
                      label_visibility='collapsed', format_func=lambda x:utl.tickers[x])

pdata = utl.get_pdata()
fdata = utl.get_fdata()

st.table(pdata.head())
st.table(fdata.head())