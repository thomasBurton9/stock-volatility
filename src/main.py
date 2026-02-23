import sys

from graph import graph_volatilities
from ticker import get_multiple_volatilities

def quit_app():
    print("Thank you for using the stock volatility grapher")
    sys.exit()
    
def user_interface():
    print("Welcome to the stock volatility grapher, enter 'q' at any time to quit")
    while True:
        tickers = []
        volatility_time_periods = []
        available_time_periods = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
        time_period = ""
        while True:
            user_entry = input("Enter ticker to add or press enter to continue: ").strip()
            if user_entry == "":
                if tickers == []:
                    print("You need to enter at least one ticker")
                    continue
                break 
            elif user_entry.lower() == "q":
                quit_app()
            else:
                tickers.append(user_entry.strip())
                
        while True:
            user_entry = input("Enter a time period for the moving average to add or press enter to continue: ").strip()
            if user_entry == "":
                if volatility_time_periods == []:
                    print("You need to enter at least one time period")
                    continue
                break
            elif user_entry.lower() == "q":
                quit_app()
            else:
                try:
                    user_entry = int(user_entry.strip())
                except ValueError:
                    print("You need to enter a number")
                    continue
                volatility_time_periods.append(user_entry)
        while True: 
            user_entry = input("Please enter an overall time period for the graph: ").strip()
            if user_entry == "":
                print("You need to enter a time period")
            elif user_entry.lower() == "q":
                quit_app()
            else:
                if user_entry not in available_time_periods:
                    print("Time period must be one of these: ")
                    print("1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd or max")
                    continue
                time_period = user_entry
                break
        
    
        average_volatilities = get_multiple_volatilities(tickers, time_period, volatility_time_periods)
        
        graph_volatilities(average_volatilities)
        user_input = input("Do you want to graph another ticker/time period? Y/n: ").strip().lower()
        if user_input == "n":
            quit_app()

def main():
    user_interface()
if __name__ == "__main__":
    main()