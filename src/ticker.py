import math

import yfinance as yf
import numpy as np

def get_alltime_logarithmic_return(data):
    close_prices = data["Close"].iloc[0:len(data)-1].to_numpy()
    close_prices2 = data["Close"].iloc[1:].to_numpy()
    
    return np.log(close_prices2 / close_prices)

def get_std(logarithmic_returns):
    return np.std(logarithmic_returns)

def get_annualized_volatility(standard_deviation, days: int):
    return standard_deviation * math.sqrt((days / 365) * 252)

def get_ticker_volatility(ticker: str, time_period: str, volatility_time_period: int) -> np.ndarray:
    """Calculates the moving average of a ticker over a specified time period

    Args:
        ticker (str): Symbol of Stock ticker. e.g. "APPL"
        time_period (str): A string of the length of time of data - including: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd or max
        volatility_time_period (int): Amount of days the moving average should be calculated based on

    Returns:
        np.ndarray: Returns an array of shape len(data) - 1
    """
    ticker_data = yf.Ticker(ticker)
    
    ticker_data_history = ticker_data.history(time_period)
    avg_log_return = get_alltime_logarithmic_return(ticker_data_history) # Note: the data starts the day after the initial data 
    # Implement - for each window from just [0] to [len(data)-window, len(data)]
    avg_volatility = np.zeros_like(avg_log_return)
    for i in range(1, len(avg_log_return)+1):
        initial_index = i - 30
        initial_index = max(initial_index, 0)
        standard_deviation = get_std(avg_log_return[initial_index: i])
        volatility = get_annualized_volatility(standard_deviation, volatility_time_period)
        avg_volatility[i-1] = volatility
    avg_volatility = avg_volatility[1:]

    return avg_volatility