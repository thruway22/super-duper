import streamlit as st
import utilities as utl

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
    utl.display_text('''
        The Net Asset Value (NAV) of a Real Estate Investment Trust (REIT) is its total \
        assets minus liabilities, divided by shares outstanding. If a REIT's market share \
        price is higher than its NAV, it's trading at a "premium." If the share price is \
        lower, it's trading at a "discount." These can indicate investor sentiment about \
        the REIT's future performance or reflect market trends.
    ''')
    utl.display_metric(ticker_ts, sector_ts, 'navpd')
    utl.display_timeseries_chart(ticker_ts, sector_ts, 'navpd')
    utl.display_divider()

    st.subheader('Dividend Yield')
    utl.display_text('''
        g
    ''')
    utl.display_metric(ticker_ts, sector_ts, 'yield')
    utl.display_timeseries_chart(ticker_ts, sector_ts, 'yield')
    utl.display_divider()

    st.subheader('P/FFO')
    utl.display_metric(ticker_ts, sector_ts, 'pffo')
    utl.display_timeseries_chart(ticker_ts, sector_ts, 'pffo')
    utl.display_divider()

    right, left = st.columns(2)
    with right:
        utl.display_categorical_section(ticker_ct, 'ffos')
    with left:
        utl.display_categorical_section(ticker_ct, 'ffo_payout')

    right, left = st.columns(2)
    with right:
        utl.display_categorical_section(ticker_ct, 'ffo_margin')
    with left:
        utl.display_categorical_section(ticker_ct, 'ffo_roic')

    right, left = st.columns(2)
    with right:
        utl.display_categorical_section(ticker_ct, 'ffo_coverage')
    with left:
        utl.display_categorical_section(ticker_ct, 'ffo_leverage')
