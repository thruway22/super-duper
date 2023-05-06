import streamlit as st

st.title('Saudi REITs')

pdata = pd.read_csv('data/pdata.csv')

st.write(pdata)
