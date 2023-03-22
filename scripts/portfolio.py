# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 20:43:35 2023

@author: HP
"""

import pandas as pd
import yfinance as yf

sample_pf={'stocks' : ['INR','HDFC.NS','TCS.NS','ITC.NS','INFY.NS'],
 'in_portfolio' : 'N',
 'NO_of_Stocks_hold' : 0 ,
 'stock_price':0,
 'value':0}

df=pd.DataFrame(sample_pf)

df.to_csv('sample_pf.csv')

nifty50_tickers = ['INR','ADANIPORTS.NS', 'ASIANPAINT.NS', 'AXISBANK.NS', 'BAJAJ-AUTO.NS', 'BAJAJFINSV.NS',                   'BPCL.NS', 'BHARTIARTL.NS', 'BRITANNIA.NS', 'CIPLA.NS', 'COALINDIA.NS', 'DIVISLAB.NS',                   'DRREDDY.NS', 'EICHERMOT.NS', 'GAIL.NS', 'GRASIM.NS', 'HCLTECH.NS', 'HDFCBANK.NS',                   'HDFCLIFE.NS', 'HEROMOTOCO.NS', 'HINDALCO.NS', 'HINDUNILVR.NS', 'HDFC.NS', 'ICICIBANK.NS',                   'IOC.NS', 'INDUSINDBK.NS', 'INFY.NS', 'ITC.NS', 'JSWSTEEL.NS', 'KOTAKBANK.NS', 'LT.NS',                   'M&M.NS', 'MARUTI.NS', 'NESTLEIND.NS', 'NTPC.NS', 'ONGC.NS', 'POWERGRID.NS', 'RELIANCE.NS',                   'SHREECEM.NS', 'SBIN.NS', 'SBILIFE.NS', 'SUNPHARMA.NS', 'TCS.NS', 'TATACONSUM.NS', 'TATAMOTORS.NS',                   'TATASTEEL.NS', 'TECHM.NS', 'TITAN.NS', 'ULTRACEMCO.NS', 'UBL.NS', 'WIPRO.NS']
nifty_50 = {'stocks':nifty50_tickers,
            'in_portfolio':'N',
            'NO_of_Stocks_hold':0,
            'stock_price':0,
            'value':0}
nifty_df=pd.DataFrame(nifty_50)

nifty_df.to_csv('nifty_50_pf.csv')

