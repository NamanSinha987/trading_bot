# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 00:25:01 2023

@author: HP
"""
import pandas as pd
import yfinance as yf
import datetime as dt
closing_price=yf.download('BHARTIARTL.NS',dt.datetime.today()-dt.timedelta(1) ,
                            dt.datetime.today(), '1d')['Adj Close'][0]



stock='BHARTIARTL.NS'

stock_price = get_stock_price(stock)
max_stocks_bought = int(available_funds / (5 * stock_price))
num_stocks = min(int(available_funds / stock_price), max_stocks_bought)
if num_stocks == 0:
    print(f"Not enough funds to buy {stock}.")
    continue
if stock in portfolio_df['stocks'].tolist():
    stock_index = portfolio_df[portfolio_df['stocks'] == stock].index[0]
    portfolio_df.at[stock_index, 'NO_of_Stocks_hold'] += num_stocks
else:
    new_row = {'stocks': stock, 'NO_of_Stocks_hold': num_stocks}
    portfolio_df = portfolio_df.append(new_row, ignore_index=True)
available_funds -= num_stocks * stock_price
portfolio_df.at[portfolio_df.index[0], 'NO_of_Stocks_hold'] = available_funds

print("hello_"+str(dt.datetime.now().strftime("%Y%m%d%H%M%S"))+".txt")


import logging 

logging.basicConfig(filename='bh.txt')
+str(dt.datetime.now().strftime("%Y%m%d%H%M%S"))+".txt")
    
def get_pe_ratio(ticker):
    stock = yf.Ticker(ticker)
    pe_ratio = stock.info.get('forwardPE')
    return stock

INFO=get_pe_ratio("ITC.NS").info
print (INFO)


msft = yf.Ticker("MSFT")

# get all stock info (slow)
print(msft.earnings)

pip install yfinance