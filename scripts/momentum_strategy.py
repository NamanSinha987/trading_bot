# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 17:32:14 2023

@author: HP
"""

import yfinance as yf
import datetime as dt
import pandas as pd
from returns import get_ret_data

def momentum_strategy(ticker,start,end,interv):
    df=get_ret_data(ticker,start,end,interv)
    df['Price_Moving_Avg'] = df['Adj Close'].rolling(window=7).mean()
    df['Vol_Moving_Avg'] = df['Volume'].rolling(window=7).mean()
    df=df.dropna()
    df['Price_lower_than_avg']=df['Price_Moving_Avg'].gt(df['Adj Close'])
    df['vol_higher_than_avg']=df['Volume'].gt(df['Vol_Moving_Avg'])
    df = df.set_index(pd.DatetimeIndex(df.index))
    df.loc[(df['Price_lower_than_avg']==False), 'BUY/SELL']='BUY'
    df.loc[(df['Price_lower_than_avg']==True), 'BUY/SELL']='SELL'
    return df

        
#AMZN_data = momentum_strategy('AMZN', dt.datetime.today()-dt.timedelta(360), 
 #                           dt.datetime.today(), '1d')
