import numpy as np
import datetime as dtClose
import yfinance as yf
from indicators import *

class Benchmarks():

    def lump_sum(self):
        self.trigger = np.zeros(self.df_length)
        self.trigger[0] = 1
        self.run_strat('lump sum')

    def min_dca(self):
        pass


    def dca(self):
        self.trigger = np.zeros(self.df_length)
        month = self.dataframe.index.month[0]
        year = self.dataframe.index.year[0]
        for i in range(len(self.trigger)):
            if self.dataframe.index.month[i] > month or self.dataframe.index.year[i] > year:
                self.trigger[i] = 1
        self.run_strat('dca')


    def random_entry(self):
            self.trigger = np.zeros(self.df_length)
            for i in range(self.df_length):
                self.trigger[i] = np.random.choice([0,0,0,0,0,0,0,0,0,1]) #1/10 days
            self.run_strat('random entry')