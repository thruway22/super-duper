import streamlit as st
import utilities as utl
import displays as dsp

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title('Saudi REITs')
ticker = st.selectbox('Choose fund', utl.tickers.keys(),
                      label_visibility='collapsed', format_func=lambda x:utl.tickers[x])

sector_ts = utl.get_sector_timeseries()

if ticker != 9999:
    st.header(utl.tickers[ticker])
    ticker_ts = utl.get_ticker_timeseries(ticker)

    ticker_ct = utl.get_ticker_categorical(ticker)

    st.subheader('NAV Premium')
    dsp.display_text('''
        The Net Asset Value (NAV) of a Real Estate Investment Trust (REIT) is its total \
        assets minus liabilities, divided by shares outstanding. If a REIT's market share \
        price is higher than its NAV, it's trading at a "premium." If the share price is \
        lower, it's trading at a "discount." These can indicate investor sentiment about \
        the REIT's future performance or reflect market trends.
    ''')
    dsp.display_metric(ticker_ts, sector_ts, 'navpd')
    dsp.display_timeseries_chart(ticker_ts, sector_ts, 'navpd')
    dsp.display_divider()

    st.subheader('Dividend Yield')
    dsp.display_text('''
        g
    ''')
    dsp.display_metric(ticker_ts, sector_ts, 'yield')
    dsp.display_timeseries_chart(ticker_ts, sector_ts, 'yield')
    dsp.display_divider()

    st.subheader('P/FFO')
    dsp.display_metric(ticker_ts, sector_ts, 'pffo')
    dsp.display_timeseries_chart(ticker_ts, sector_ts, 'pffo')
    dsp.display_divider()

    right, left = st.columns(2)
    with right:
        st.subheader('FFO/Sahre')
        dsp.display_categorical_chart(ticker_ct, 'ffos')
        dsp.display_divider()
    with left:
        st.subheader('FFO Payout Ratio')
        dsp.display_categorical_chart(ticker_ct, 'ffo_payout')
        dsp.display_divider()

    right, left = st.columns(2)
    with right:
        st.subheader('FFO Margin')
        dsp.display_categorical_chart(ticker_ct, 'ffo_margin')
        dsp.display_divider()
    with left:
        st.subheader('FFO ROIC')
        dsp.display_categorical_chart(ticker_ct, 'ffo_roic')
        dsp.display_divider()

    right, left = st.columns(2)
    with right:
        st.subheader('FFO Coverage')
        dsp.display_categorical_chart(ticker_ct, 'ffo_coverage')
        dsp.display_divider()
    with left:
        st.subheader('FFO Leverage')
        dsp.display_categorical_chart(ticker_ct, 'ffo_leverage')
        dsp.display_divider() 
