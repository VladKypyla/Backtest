import numpy as np
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt


from strategy import Strategy
from portfolio import Portfolio
from investor import Investor


ticker = "SPY"
start = "1990-01-01"
end = dt.date.today()
assets  = yf.download(ticker, start, end)


inv = Investor(assets,balance=1000, deposit_amount=100)
inv.run_strat()

#Should be inside library
inv.dataframe['position'] = inv.position
inv.dataframe['wallet'] = inv.wallet
inv.dataframe['equity'] = inv.equity

plt.plot(inv.dataframe['equity'])
#plt.plot(inv.dataframe['wallet'])
print(inv.dataframe)
plt.show()


