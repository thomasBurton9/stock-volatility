import matplotlib.pyplot as plt

def graph_volatilities(volatility_data):

    
    for vol_data in volatility_data:
        plt.plot(vol_data[0][2:], label=f"{vol_data[1]}: {vol_data[2]} days")
    plt.title(f"Stock volatility moving average")
    plt.xticks(rotation=60)
    plt.legend()
    plt.show()
