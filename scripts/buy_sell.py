# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 20:04:38 2023

@author: HP
"""

import pandas as pd
import numpy as np
import datetime as dt
from momentum_strategy import momentum_strategy


def buy_sell(df,start,end,interval):
    stock_list_dict={'stocks':[],'BUY/SELL':[]}
    stock_list_df=pd.DataFrame(stock_list_dict)
    for i in range(len(df.index)):
        stock=df['stocks'][i]
        price_data=momentum_strategy(stock, start, end, interval)
        price_data_last_row=price_data.iloc[-1]
        opinion=price_data_last_row.loc['BUY/SELL']
        stock_entry ={'stocks':stock,'BUY/SELL':opinion}
        stock_list_df=stock_list_df.append(stock_entry,ignore_index=True)
    return stock_list_df

def buy_list(df):
    buy_stocks_list=[]
    for i in range(len(df.index)):
        if (df['BUY/SELL'][i]=='BUY'):
            buy_stocks_list.append(df['stocks'][i])
    
    return buy_stocks_list

def sell_list(df):
    sell_stocks_list=[]
    for i in range(len(df.index)):
        if (df['BUY/SELL'][i]=='SELL'):
            sell_stocks_list.append(df['stocks'][i])
    
    return sell_stocks_list
                

#nifty_50_df=pd.read_csv('nifty_50_pf.csv', index_col=[0])
#nifty_50_df=nifty_50_df.drop(0)
#nifty_50_df=nifty_50_df.reset_index()
#todays_opinion=buy_sell(nifty_50_df, dt.datetime.today()-dt.timedelta(360), 
#                            dt.datetime.today(), '1d')

#buy_stock_list=buy_list(todays_opinion)
#sell_stock_list=sell_list(todays_opinion)