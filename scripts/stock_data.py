# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import yfinance as yf
import datetime as dt
import pandas as pd



def get_stock_data(ticker,start_time,end_time, interval):
    stock_data=pd.DataFrame()
    stock_data=yf.download(ticker,start_time,end_time, interval=interval)
    return stock_data

#itc_data=get_stock_data('ITC.NS',dt.datetime.today()-dt.timedelta(360),dt.datetime.today(),'1d')