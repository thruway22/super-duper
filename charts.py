import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

var_dict = {
    'ffos': '%.2f',
    'ffo_payout': '%.1f%%',
    'ffo_roic': '%.1f%%',
    'ffo_margin': '%.1f%%',
    'ffo_leverage': '%.2fx',
    'ffo_coverage': '%.2fx',
    }

color_dict = {
        'more_than_zero': {
            'navpd': '#ff2b2b',
            'pffo': '#ff2b2b',
            'yield': '#09ab3b'
        },
        'less_than_zero': {
            'navpd': '#09ab3b',
            'pffo': '#09ab3b',
            'yield': '#ff2b2b'
        }
    }

def display_timeseries_chart(ticker_df, sector_df, metric):
    # set defult font and colors
    plt.rcParams['font.size'] = 6
    plt.rcParams['font.family'] = "sans-serif"
    plt.rcParams['text.color'] = "85868B"
    plt.rcParams['xtick.color'] = '85868B'

    if metric == 'price':
        xy = ticker_df['navpd']
    else:
        xy = ((ticker_df[metric] / sector_df[metric]) - 1) * 100

    x_curve = xy.index
    y_curve = xy.values 

    fig, ax = plt.subplots(figsize=(6.4, 1.2))

    ax.plot(ticker_df[metric], linewidth=0)

    ax.fill_between(x_curve, y_curve,
                    where=(y_curve > 0), color=color_dict['more_than_zero'][metric], alpha=0.15)
    ax.fill_between(x_curve, y_curve,
                    where=(y_curve < 0), color=color_dict['less_than_zero'][metric], alpha=0.15)


    # if metric == 'price':
    #     fig, ax = plt.subplots(figsize=(6.4, 2.0))
    #     ax.plot(ticker_df['price'], linewidth=1, color='lightgrey', alpha=1, label='Price')
    #     ax.plot(ticker_df['nav'], linewidth=1, color='#0068c9', alpha=1, label='NAV')

    # else:
    #     fig, ax = plt.subplots(figsize=(6.4, 1.2))
    #     xy = ((ticker_df[metric] / sector_df[metric]) - 1) * 100
    #     x_curve = xy.index
    #     y_curve = xy.values

    #     ax.plot(ticker_df[metric], color='#0068c9', linewidth=0)
    
    #     ax.fill_between(x_curve, y_curve,
    #                     where=(y_curve > 0), color=color_dict['more_than_zero'][metric], alpha=0.15)
    #     ax.fill_between(x_curve, y_curve,
    #                     where=(y_curve < 0), color=color_dict['less_than_zero'][metric], alpha=0.15)

        # ax.plot(ticker_df[metric], linewidth=1, color='#0068c9', alpha=1, label='Ticker')
        # ax.plot(sector_df[metric], linewidth=1, color='lightgrey', alpha=1, label='Sector')

    ax.set_frame_on(False)
    ax.get_yaxis().set_visible(False)
    # ax.get_xaxis().set_visible(False)
    plt.legend(loc='upper left')

    return st.pyplot(fig)

def display_categorical_chart(df, metric):

    # set x and y axis data
    x = df.index
    y = df[metric]

    # set defult font and colors
    plt.rcParams['font.size'] = 8
    plt.rcParams['font.family'] = "sans-serif"
    plt.rcParams['text.color'] = "262730"
    #plt.rcParams['axes.labelcolor'] = 'ffffff'
    plt.rcParams['xtick.color'] = '262730'

    fig, ax = plt.subplots(figsize=(6.4, 4.5))
    bars = ax.bar(np.arange(len(x)), y, tick_label=x, color='#0068c9', width=0.96)
    ax.bar_label(bars, size=10,
                 padding=6, fmt=var_dict[metric],
                 bbox=dict(boxstyle="round, pad=0.3", fc="#0068c9", lw=0, alpha=0.10))
    
    ax.get_yaxis().set_visible(False)    
    ax.set_frame_on(False)
    
    plt.margins(x=0, y=0.15)
    plt.subplots_adjust(hspace=0)
    
    return st.pyplot(fig)
