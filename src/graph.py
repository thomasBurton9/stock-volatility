import matplotlib.pyplot as plt

def graph_volatility(volatility_data):

    
    for vol_data in volatility_data:
        plt.plot(vol_data[0], label=f"{vol_data[1]}: {vol_data[2]} days")
    plt.legend()
    plt.show()
