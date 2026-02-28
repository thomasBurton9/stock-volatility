from volatility import get_alltime_logarithmic_return, get_std, get_annualized_volatility
import math

import yfinance as yf
import numpy as np
import pandas as pd


def get_ticker_volatility(ticker: str, time_period: str, volatility_time_period: int) -> pd.DataFrame:
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
    ticker_data_history.columns.get_loc("Close")
    
    columns = ticker_data_history.columns.drop("Close")
    ticker_data_history = ticker_data_history.drop(columns=columns)
    
    # Validate data to prevent Nan
    ticker_data_history = ticker_data_history.dropna()
    avg_log_return = get_alltime_logarithmic_return(ticker_data_history) # Note: the data starts the day after the initial data 

    # Implement - for each window from just [0] to [len(data)-window, len(data)]
    avg_volatility = np.zeros_like(avg_log_return)

    for i in range(2, len(avg_log_return)+1):
        initial_index = i - volatility_time_period
        initial_index = max(initial_index, 0)
        standard_deviation = get_std(avg_log_return[initial_index: i])
        volatility = get_annualized_volatility(standard_deviation, volatility_time_period)
        avg_volatility[i-1] = volatility


    ticker_data_history["AvgVolatility"] = np.append([0], avg_volatility)
    ticker_data_history = ticker_data_history.drop(columns="Close")

    return ticker_data_history

def get_multiple_volatilities(tickers: list[str], time_period: str, volatility_time_periods: list[int]) -> list[tuple[pd.DataFrame, str, int]]:
    average_volatilities = []
    for ticker in tickers:
            for vol_time_period in volatility_time_periods:
                average_volatilities.append((get_ticker_volatility(ticker, time_period, vol_time_period), ticker, vol_time_period))
    
    return average_volatilities