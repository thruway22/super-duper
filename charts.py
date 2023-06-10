import pandas as pd
import plotly.express as px
import streamlit as st


def display_timeseries_chart(df, metric):
    pass

def display_categorical_chart(df, metric):
    fig = px.bar(df, x=df.index, y=metric, height=350)
    fig.update_layout(
        bargap=0.05,
        margin=dict(l=20, r=20, t=20, b=20)
        )
    fig.update_yaxes(visible=False, showticklabels=False, showgrid=False)
    # for i, t in enumerate(texts):
    #     fig.data[i].text = t
    #     fig.data[i].textposition = 'outside'
    st.plotly_chart(fig, use_container_width=True, config= {'displayModeBar': False})