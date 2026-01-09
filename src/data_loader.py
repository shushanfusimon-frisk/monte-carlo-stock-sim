import yfinance as yf
import pandas as pd
import numpy as np

#Download daily adjusted close prices for a given ticker
def download_price_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    """
    Download daily adjusted close prices for a given ticker.
    """
    data = yf.download(ticker, start=start, end=end)
    data = data[['Adj Close']].rename(columns={'Adj Close': 'price'})
    data.dropna(inplace=True)
    return data

#Compute daily log returns from price data
def compute_log_returns(price_df: pd.DataFrame) -> pd.Series:
    returns = np.log(price_df['price'] / price_df['price'].shift(1))
    return returns.dropna()
