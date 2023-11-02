# equal-weight S&P 500 Index Fund
import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math

stocks = pd.read_csv('sp_500_stocks.csv')
import yfinance as yf

aapl = yf.Ticker("AAPL")
data = yf.download("AMZN AAPL GOOG MSFT TSLA", start="2019-01-01", end="2023-10-20", group_by="tickers")
print(data)

msft = yf.Ticker("MSFT")
msft.info
hist = msft.history(period="1mo")
msft.history_metadata
msft.actions
msft.dividends
msft.splits
msft.capital_gains

stock_names = []
for index, row in stocks.iterrows():
    stock_name = row['Ticker']
    stock_names.append(stock_name)

reduced_list = []
for element in stock_names:
    if yf.Ticker(element).info["forwardPE"] < 25 and yf.Ticker(element).info["marketCap"] < 5000000000:
        reduced_list.append(element)