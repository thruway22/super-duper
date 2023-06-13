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
    ts = utl.get_ticker_timeseries(ticker)

    ct = utl.get_ticker_categorical(ticker)
    st.table(ts.head())

    # st.subheader('Price/NAV')
    # fig = px.line(ts, x=ts.index, y=['price', 'nav'])
    # fig.update_layout(
    #     xaxis_title = 'Date',
    #     yaxis_title = 'Price (SAR)',
    #     legend_title = 'Variable')
    # # fig.update_yaxes(fixedrange=True)#minor=dict(tickmode='auto', showgrid=True))
    # # griddash='dash', minor_griddash="dot"
    # newnames = {'price':'Quote', 'nav': 'NAV'}
    # fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
    #                                     legendgroup = newnames[t.name],
    #                                     hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
    #                                     )
    #                 )
    # st.plotly_chart(fig, use_container_width=True, config= {'displayModeBar': False})

    right, left = st.columns(2)
    with right:
        st.subheader('FFO/Sahre')
        cht.display_categorical_chart(ct, 'ffos')
    with left:
        st.subheader('FFO Payout Ratio')
        cht.display_categorical_chart(ct, 'ffo_payout')

    right, left = st.columns(2)
    with right:
        st.subheader('FFO Margin')
        cht.display_categorical_chart(ct, 'ffo_margin')
    with left:
        st.subheader('FFO ROIC')
        cht.display_categorical_chart(ct, 'ffo_roic')

    right, left = st.columns(2)
    with right:
        st.subheader('FFO Coverage')
        cht.display_categorical_chart(ct, 'ffo_coverage')
    with left:
        st.subheader('FFO Leverage')
        cht.display_categorical_chart(ct, 'ffo_leverage') 
