import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
from investor import Investor


ticker = "SPY"
start = "2000-01-01"
end = dt.date.today()
assets  = yf.download(ticker, start, end)
assets = assets.drop(columns = ['Open','High','Volume'])


inv = Investor(assets,balance=1000, deposit_amount=100)
inv.run_strat()
inv.dca()

inv.visualize()


