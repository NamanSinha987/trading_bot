# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 19:13:02 2023

@author: HP
"""

import pandas as pd
import numpy as np
import datetime as dt
import yfinance as yf
import logging 
from pf_rebalance import rebalance_pf, get_portfolio_value

class ExcludeYfinanceFilter(logging.Filter):
    def filter(self, record):
        msg = record.getMessage()
        return not ("requests.packages.urllib3.connectionpool" in msg and "Starting new HTTPS connection" in msg)

# Add filter to logger


logging.basicConfig(filename="../logs/backtester"+str(dt.datetime.now().strftime("%Y%m%d%H%M%S"))+".log",
               format='%(asctime)s %(message)s',
                    filemode='w')
 
lg = logging.getLogger()
lg.setLevel(logging.DEBUG)
lg.addFilter(ExcludeYfinanceFilter())


lg.info("****************************** SCRIPT START ********************")
lg.info("----------------------------------------------------------------")

for i in range(300):
    updated_pf= rebalance_pf('nifty_50_pf.csv',dt.datetime.today()-dt.timedelta(360), 
                                dt.datetime.today()-dt.timedelta(299-i), '1d')
    lg.info("portfolio value at end of : "+str(dt.datetime.today()-dt.timedelta(299-i))+ "  :  "+str(get_portfolio_value(updated_pf)))
    print("portfolio value at end of : "+str(dt.datetime.today()-dt.timedelta(299-i))+ "  :  "+ str(get_portfolio_value(updated_pf)))

lg.info("portfolio value : "+ str(get_portfolio_value(updated_pf)))