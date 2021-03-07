# import matplotlib
import yfinance as yf

# Get the data for the stock AAPL

datas = []

ticker = 'NDX'

for i in range(10):
    datas.append( yf.download(ticker, f'201{i}-03-15',f'201{i}-04-15') )


# Import the plotting library
import matplotlib.pyplot as plt
# %matplotlib inline

# Plot the close price of the AAPL
for i in range(10):
    plt.plot([x/list(datas[i]['Adj Close'])[-1] for x in list(datas[i]['Adj Close'])], label=f"{ticker} 201{i}")


plt.legend()
plt.savefig("ndx.png")