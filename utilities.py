import numpy as np
import pandas as pd
from datetime import datetime  
from datetime import timedelta
from pandas.tseries.offsets import DateOffset
from pandas.tseries.offsets import MonthEnd
import streamlit as st

tickers = {    
    9999: '',
    4330: '4330: Riyad REIT الرياض ريت',
    4331: '4331: Aljazira REIT الجزيرة ريت',
    4332: '4332: Jadwa REIT Alharamain جدوى ريت الحرمين',
    4333: '4333: Taleem REIT تعليم ريت',
    4334: '4334: Almaather REIT المعذر ريت',
    4335: '4335: Musharaka REIT مشاركة ريت',
    4336: '4336: Mulkia Gulf REIT ملكية الخليج ريت',
    4337: '4337: SICO Saudi REIT سيكو السعودية ريت',
    4338: '4338: Alahli REIT الأهلي ريت',
    4339: '4339: Derayah REIT دراية ريت',
    4340: '4340: Alrajhi REIT الراجحي ريت',
    4342: '4342: Jadwa REIT جدوى ريت',
    4344: '4344: SEDCO Capital REIT سدكو كابيتال ريت',
    4345: '4345: Alinma Retail REIT الإنماء ريت التجزئة',
    4346: '4346: MEFIC REIT ميفك ريت',
    4347: '4347: Bonyan REIT بنيان ريت',
    4348: '4348: Alkhabeer REIT الخبير ريت'
}