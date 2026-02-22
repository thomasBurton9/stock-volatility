import yfinance as yf
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

data = yf.Ticker("AAPL")

data_history = data.history(period="1y")
def get_alltime_logarithmic_return(data):
    close_prices = data["Close"].iloc[0:len(data)-1].to_numpy()
    close_prices2 = data["Close"].iloc[1:].to_numpy()
    
    return np.log(close_prices2 / close_prices)
        
def get_logarithmic_return(final_value, initial_value):
    return math.log(final_value / initial_value)

def get_std(logarithmic_returns):
    return np.std(logarithmic_returns)

def get_annualized_volatility(standard_deviation, days: int):
    return standard_deviation * math.sqrt((days / 365) * 252)

def graph_volatility(volatility):
    plt.plot(volatility)
    plt.show()
    
def main(ticker: str, time_period: str, volatility_time_period: int):
    data = yf.Ticker(ticker)
    
    data_history = data.history(time_period)
    print(data_history)
    avg_log_return = get_alltime_logarithmic_return(data_history) # Note: the data starts the day after the initial data 
    print(avg_log_return)
    # Implement - for each window from just [0] to [len(data)-window, len(data)]
    avg_volatility = np.zeros_like(avg_log_return)
    for i in range(1, len(avg_log_return)+1):
        initial_index = i - 30
        initial_index = max(initial_index, 0)
        standard_deviation = get_std(avg_log_return[initial_index: i])
        volatility = get_annualized_volatility(standard_deviation, volatility_time_period)
        avg_volatility[i-1] = volatility
    avg_volatility = avg_volatility[1:]
    print(avg_volatility)
    graph_volatility(avg_volatility)
    
        
if __name__ == "__main__":
    main("AAPL", "1y", 30)