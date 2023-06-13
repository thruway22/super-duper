import streamlit as st
import utilities as utl
import charts as cht
# import display as dsp

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title('Saudi REITs')
ticker = st.selectbox('Choose fund', utl.tickers.keys(),
                      label_visibility='collapsed', format_func=lambda x:utl.tickers[x])

sector_ts = utl.get_sector_timeseries()

if ticker != 9999:
    ticker_ts = utl.get_ticker_timeseries(ticker)

    ticker_ct = utl.get_ticker_categorical(ticker)

    st.subheader('NAV Premium')
    cht.display_metric(ticker_ts, sector_ts, 'navpd')
    cht.display_timeseries_chart(ticker_ts, sector_ts, 'navpd')
    cht.display_divider()

    st.subheader('Dividend Yield')
    cht.display_metric(ticker_ts, sector_ts, 'yield')
    cht.display_timeseries_chart(ticker_ts, sector_ts, 'yield')

    st.subheader('P/FFO')
    cht.display_metric(ticker_ts, sector_ts, 'pffo')
    cht.display_timeseries_chart(ticker_ts, sector_ts, 'pffo')

    right, left = st.columns(2)
    with right:
        st.subheader('FFO/Sahre')
        cht.display_categorical_chart(ticker_ct, 'ffos')
    with left:
        st.subheader('FFO Payout Ratio')
        cht.display_categorical_chart(ticker_ct, 'ffo_payout')

    right, left = st.columns(2)
    with right:
        st.subheader('FFO Margin')
        cht.display_categorical_chart(ticker_ct, 'ffo_margin')
    with left:
        st.subheader('FFO ROIC')
        cht.display_categorical_chart(ticker_ct, 'ffo_roic')

    right, left = st.columns(2)
    with right:
        st.subheader('FFO Coverage')
        cht.display_categorical_chart(ticker_ct, 'ffo_coverage')
    with left:
        st.subheader('FFO Leverage')
        cht.display_categorical_chart(ticker_ct, 'ffo_leverage') 
