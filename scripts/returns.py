# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 02:27:03 2023

@author: HP
"""

import numpy as np
import pandas as pd
import datetime as dt
from stock_data import get_stock_data

def pct_returns(stock_data):
    stock_data['pct_change']=stock_data['Adj Close'].pct_change()
    return stock_data

def log_returns(stock_data):
    stock_data['log_return']=np.log(1+stock_data['pct_change'])
    return stock_data



def tot_pct_return(stock_data):
    stock_data=stock_data.dropna()
    ret=1
    for i in range(1,len(stock_data.index)):
        stock_data['cum_ret'][i]=(stock_data['cum_ret'][i-1])*(1+stock_data['pct_change'][i])
    return stock_data


    


        


def tot_log_return(stock_data):
    stock_data=stock_data.dropna()
    
    for i in range(0,len(stock_data.index)):
        stock_data['cum_log_ret'][i]+=stock_data['cum_log_ret'][i-1]
    return stock_data




def get_ret_data(ticker,start,end,interv):
    stock_data=get_stock_data(ticker, start, end, interval=interv)
    stock_data=pct_returns(stock_data)
    stock_data=log_returns(stock_data)
    stock_data=stock_data.dropna()
    stock_data['cum_ret']=stock_data['pct_change']
    stock_data['cum_log_ret']=stock_data['log_return']
    stock_data['cum_ret'][0]=1+stock_data['cum_ret'][0]
    stock_data=tot_pct_return(stock_data)
    stock_data=tot_log_return(stock_data)
    
    return stock_data

#googl_data=get_ret_data('GOOGL',dt.datetime.today()-dt.timedelta(29+1), 
 #                           dt.datetime.today(), '1d')