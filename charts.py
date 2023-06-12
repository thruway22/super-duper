import pandas as pd
import plotly.express as px
import streamlit as st

var_dict = {
    'revenue': '%.1fM', 
    'asset': '%.1fM',
    'ffos': '.2f',
    'ffo_payout': '.1%',
    'ffo_roic': '.1%',
    'ffo_margin': '.1%',
    'net_debt_ebitda': '%.2fx',
    'coverage': '%.2fx',
    }

def display_timeseries_chart(df, metric):
    pass

def display_categorical_chart(df, metric):
    fig = px.bar(df, x=df.index, y=metric, text_auto=var_dict[metric], height=280)
    fig.update_layout(
        bargap=0.03,
        margin=dict(l=5, r=5, t=5, b=5)
        )
    fig.update_yaxes(visible=False, showticklabels=False, showgrid=False)
    # for i, t in enumerate(texts):
    #     fig.data[i].text = t
    #     fig.data[i].textposition = 'outside'
    st.plotly_chart(fig, use_container_width=True, config= {'displayModeBar': False})