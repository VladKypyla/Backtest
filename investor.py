from dataclasses import dataclass
import numpy as np
import datetime as dt
import yfinance as yf

from portfolio import Portfolio
from strategy import Strategy


class Investor(Strategy,Portfolio):
    def __init__(self, assets, balance=1000, min_share = 1, deposit_amount = 300, fractional_shares = 0,
                    ):
        self.fractional_shares = fractional_shares

        Strategy.__init__(self,assets)
        self.populate_indicators(self.dataframe)
        self.entry_long_conditions(self.dataframe)
        self.dataframe = self.dataframe.dropna()

        Portfolio.__init__(self,self.dataframe, balance, deposit_amount)
        self.min_share = min_share

        self.df_length = len(self.dataframe)
        
        #STATS

        

        #####ONLY INVEST DAY 1
        self.enter_long = np.zeros(self.df_length)
        self.enter_long[0] = 1
        self.dataframe['enter_long'] = self.enter_long
        #####





    def buy(self,day):
        if self.fractional_shares == 1:
            shares = self.wallet[day]/self.price[day]
        else:
            shares = int(self.wallet[day]/self.price[day])
        
        self.update_position(day,shares)
        self.update_wallet(day, -shares*self.price[day])

    def sell(self,day):
        pass


    

    def next(self,day):

        if day != 0:
            self.wallet[day] = self.wallet[day-1]
            self.position[day] = self.position[day-1]

            #Check if deposit day 
            if (self.dataframe.index.month[day] > self.date_month) or (self.dataframe.index.year[day] >self.date_year):
                self.date_month = self.dataframe.index.month[day]
                self.date_year = self.dataframe.index.year[day]
                self.update_wallet(day, self.deposit_amount)


        if self.trigger[day] == 1:
            if int(self.wallet[day]/self.price[day]) >= self.min_share:
                self.buy(day)
        elif self.trigger[day] == -1:
            #SELL CODE
            pass

        self.recalculate_equity(day)
        #self.get_stats(day)

    def benchmarks(self,type = 'lump_sum'):
        if type == 'lump_sum':
            pass


    def run_strat(self):
        self.wallet = np.zeros(self.df_length)
        self.update_wallet(0,self.balance)
        self.position = np.zeros(self.df_length)

        self.date_month = self.dataframe.index.month[0]
        self.date_year = self.dataframe.index.year[0]
        
        self.equity = np.zeros(self.df_length)


        self.price = self.dataframe['Adj Close'].to_numpy()
        self.trigger = self.dataframe['enter_long'].to_numpy()

        for i in range(self.df_length):
            self.next(i)

    def run_benchmarks(self):
        pass
        

        