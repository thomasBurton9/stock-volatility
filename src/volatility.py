import math
import numpy as np

def get_alltime_logarithmic_return(data):
    close_prices = data["Close"].iloc[0:len(data)-1].to_numpy()
    close_prices2 = data["Close"].iloc[1:].to_numpy()
    
    return np.log(close_prices2 / close_prices)

def get_std(logarithmic_returns):
    return np.std(logarithmic_returns, ddof=1)

def get_annualized_volatility(standard_deviation, days: int):
    return standard_deviation * math.sqrt(252)
