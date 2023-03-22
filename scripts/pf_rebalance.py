# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 21:00:23 2023

@author: HP
"""

import pandas as pd
import numpy as np
import datetime as dt
from buy_sell import buy_sell,buy_list,sell_list
import yfinance as yf
import logging 


logging.basicConfig(filename="../logs/pf_rebalance"+str(dt.datetime.now().strftime("%Y%m%d%H%M%S"))+".log",
               format='%(asctime)s %(message)s',
                    filemode='w')
 
lg = logging.getLogger()
lg.setLevel(logging.DEBUG)

lg.info("****************************** SCRIPT START ********************")
lg.info("----------------------------------------------------------------")

def get_stock_price(stock):
    closing_price=yf.download(stock,dt.datetime.today()-dt.timedelta(1) ,
                                dt.datetime.today(), '1d')['Adj Close'][0]
    return closing_price

def stocks_value(portfolio_df):
    lg.info("function stocks_value running ")
    for i in range(1,len(portfolio_df.index)):
        lg.info("stock : "+ portfolio_df['stocks'][i])
        portfolio_df['stock_price'][i]=get_stock_price(portfolio_df['stocks'][i])
        lg.info(" stock price :"+ str(portfolio_df['stock_price'][i]))
        portfolio_df['value'][i]=(portfolio_df['stock_price'][i]*(portfolio_df['NO_of_Stocks_hold'][i]))
        lg.info("value :"+ str(portfolio_df['value'][i]))
    return portfolio_df

def get_portfolio_value(portfolio_df):
    value=0
    for i in range(len(portfolio_df.index)):
        value+=portfolio_df['value'][i]
    return value


def sell_stocks(portfolio_df, stocks_to_sell):
    lg.info("********** Selling Stocks ************")
    for stock in stocks_to_sell:
        lg.info(" Sell Stock : "+stock)
        # Check if the stock is in the portfolio dataframe
        if stock in portfolio_df['stocks'].tolist():
            # Get the index of the row corresponding to the stock in the portfolio dataframe
            stock_index = portfolio_df[portfolio_df['stocks'] == stock].index[0]
            # Update the INR row with the value of the stocks sold
            
            lg.info("value of stocks being sold "+str(portfolio_df.at[stock_index, 'value']))
            portfolio_df.at[portfolio_df.index[0], 'NO_of_Stocks_hold'] += portfolio_df.at[stock_index, 'value']
            portfolio_df.at[portfolio_df.index[0], 'value'] += portfolio_df.at[stock_index, 'value']
            # Sell all the stocks of this stock
            portfolio_df.at[stock_index, 'NO_of_Stocks_hold'] = 0
            portfolio_df.at[stock_index,'value']=0
            
          
        else:
            lg.info(f"{stock} is not in the portfolio.")
    return portfolio_df

def buy_stocks(portfolio_df,stocks_to_buy):
    lg.info("****** Buy stocks ********")
    available_funds=portfolio_df.at[portfolio_df.index[0], 'NO_of_Stocks_hold']
    lg.info("Available funds : "+str(available_funds))
    total_funds=get_portfolio_value(portfolio_df)
    lg.info ("total fund: "+ str(total_funds))
    for stock in stocks_to_buy:
        lg.info("stock: "+stock+"--------")
        lg.info ("fund: "+ str(available_funds))
        
        stock_price = get_stock_price(stock)
        
        lg.info("price: "+str(stock_price))
        
        max_stocks_bought = int(total_funds / (5 * stock_price))
        lg.info("max_stocks_bought: "+str(max_stocks_bought))
        
        num_stocks = min(int(available_funds / stock_price), max_stocks_bought)
        lg.info("num_stocks: "+str(num_stocks))
        if num_stocks == 0:
            lg.info(f"Not enough funds to buy {stock}.")
            continue
        if stock in portfolio_df['stocks'].tolist():
            stock_index = portfolio_df[portfolio_df['stocks'] == stock].index[0]
            portfolio_df.at[stock_index, 'NO_of_Stocks_hold'] += num_stocks
            portfolio_df.at[stock_index,'stock_price']= stock_price
            portfolio_df.at[stock_index,'value']= portfolio_df.at[stock_index, 'NO_of_Stocks_hold']*stock_price
        else:
            new_row = {'stocks': stock, 'NO_of_Stocks_hold': num_stocks}
            portfolio_df = portfolio_df.append(new_row, ignore_index=True)
        available_funds -= num_stocks * stock_price
        portfolio_df.at[portfolio_df.index[0], 'NO_of_Stocks_hold'] = available_funds
        portfolio_df.at[portfolio_df.index[0], 'value'] = available_funds
    return portfolio_df


def rebalance_pf(portfolio_csv,start,end,interval):
    # returns rebalanced portfolio dataframe and updates the portfolio csv
    df= pd.read_csv(portfolio_csv,index_col=[0])
    df_upd=df.drop(0)
    df_upd=df_upd.reset_index()
    todays_opinion=buy_sell(df_upd,start,end, interval)
    buy_stock_list=buy_list(todays_opinion)
    sell_stock_list=sell_list(todays_opinion)
    lg.info("buy stock list : " +str(buy_stock_list))
    lg.info("sell stock list : " +str(sell_stock_list))
    updated_pf=stocks_value(df)            
    updated_pf= sell_stocks(updated_pf, sell_stock_list)
    updated_pf = buy_stocks(updated_pf, buy_stock_list)    
    updated_pf.to_csv(portfolio_csv)
    return updated_pf

#nifty_50_df=pd.read_csv('nifty_50_pf.csv', index_col=[0])

#nifty_50_df_upd=nifty_50_df.drop(0)
#nifty_50_df_upd=nifty_50_df_upd.reset_index()
#todays_opinion=buy_sell(nifty_50_df_upd, dt.datetime.today()-dt.timedelta(360), 
#                            dt.datetime.today()-dt.timedelta(0), '1d')

#buy_stock_list=buy_list(todays_opinion)
#sell_stock_list=sell_list(todays_opinion)


#lg.info("buy stock list : " +str(buy_stock_list))
#lg.info("sell stock list : " +str(sell_stock_list))

#updated_pf=stocks_value(nifty_50_df)
        
#updated_pf= sell_stocks(updated_pf, sell_stock_list)
#updated_pf = buy_stocks(updated_pf, buy_stock_list)
#updated_pf.to_csv('nifty_50_pf.csv')

#updated_pf= rebalance_pf('nifty_50_pf.csv',dt.datetime.today()-dt.timedelta(360), 
 #                           dt.datetime.today(), '1d')

#lg.info("portfolio value : "+ str(get_portfolio_value(updated_pf)))

lg.info("********************* END *********************************")