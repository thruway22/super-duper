import numpy as np
import pandas as pd
from datetime import datetime  
from datetime import timedelta
from pandas.tseries.offsets import DateOffset
from pandas.tseries.offsets import MonthEnd
import streamlit as st

tickers = {    
    9999: '',
    4330: '4330: Riyad REIT',
    4331: '4331: Aljazira REIT',
    4332: '4332: Jadwa REIT Alharamain',
    4333: '4333: Taleem REIT',
    4334: '4334: Almaather REIT',
    4335: '4335: Musharaka REIT',
    4336: '4336: Mulkia Gulf REIT',
    4337: '4337: SICO Saudi REIT',
    4338: '4338: Alahli REIT',
    4339: '4339: Derayah REIT',
    4340: '4340: Alrajhi REIT',
    4342: '4342: Jadwa REIT',
    4344: '4344: SEDCO Capital REIT',
    4345: '4345: Alinma Retail REIT',
    4346: '4346: MEFIC REIT',
    4347: '4347: Bonyan REIT',
    4348: '4348: Alkhabeer REIT'
}

def get_pdata():
    pdata = pd.read_csv('data/pdata.csv')
    pdata['date'] = pd.to_datetime(pdata['date'], format='%Y-%m-%d')
    return pdata
# pdata['date'] = pd.to_datetime(pdata['date'], format='%Y-%m-%d')

def get_fdata():
    fdata = pd.read_csv('data/fdata.csv')
    fdata[year_col] = pd.to_datetime(fdata[year_col], format='%Y-%m-%d')
    fdata = fdata.sort_values(by=year_col)
    return fdata


