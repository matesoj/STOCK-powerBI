import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date, filename):
    stock = yf.download(ticker, start=start_date, end=end_date)
    

    stock.to_csv(filename)
    print(f"Dane zapisane do {filename}")

ticker_symbol = "ART.WA" 
start_date = "2016-01-01"
end_date = "2025-02-01"
filename = "artifex_stock_data.csv"

fetch_stock_data(ticker_symbol, start_date, end_date, filename)