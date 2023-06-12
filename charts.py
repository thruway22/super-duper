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
    'ffo_leverage': '.2f',
    'ffo_coverage': '.2f',
    }

var_dict = {
    'ffos': '%.2f',
    'ffo_payout': '%.1f%%',
    'ffo_roic': '%.1f%%',
    'ffo_margin': '%.1f%%',
    'ffo_leverage': '%.2fx',
    'ffo_coverage': '%.2fx',
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

def display_categorical_chart2(df, metric):

    # set x and y axis data
    x = df.index
    y = df[metric_col]

    # set defult font and colors
    plt.rcParams['font.size'] = 8
    plt.rcParams['font.family'] = "sans-serif"
    plt.rcParams['text.color'] = "262730"
    #plt.rcParams['axes.labelcolor'] = 'ffffff'
    plt.rcParams['xtick.color'] = '262730'

    fig, ax = plt.subplots(2, 1, figsize=4.5)
    bars = ax.bar(np.arange(len(x)), y, tick_label=x, color='#0068c9', width=0.96)

    # show bar values on top
    ax.bar_label(bars, size=10,
                 padding=6, fmt=var_dict['unit'][metric_col],
                 bbox=dict(boxstyle="round, pad=0.3", fc="#0068c9", lw=0, alpha=0.10))
    
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)    
    
    # hide framebox
    ax.set_frame_on(False)
    
    # remove side (x) margins and pad (y) 
    plt.margins(x=0, y=0.15)
    
    plt.subplots_adjust(hspace=0)
    
    
    #plt.show()
    return fig
