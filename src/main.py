from graph import graph_volatility
from ticker import get_ticker_volatility

def main():
    
    tickers = ["AAPL", "MSFT"]
    volatility_time_periods = [30, 90]
    time_period = "1y"
    average_volatilities = []
    for ticker in tickers:
        for vol_time_period in volatility_time_periods:
            average_volatilities.append((get_ticker_volatility(ticker, time_period, vol_time_period), ticker, vol_time_period))
    
    graph_volatility(average_volatilities)

if __name__ == "__main__":
    main()