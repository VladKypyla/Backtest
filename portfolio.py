import numpy as np
import datetime as dt
import yfinance as yf

class Portfolio():
    def __init__(self,dataframe, balance, deposit_amount):
        self.dataframe = dataframe
        self.balance = balance
        self.deposit_amount = deposit_amount







    def update_wallet(self,day,value):
        self.wallet[day] += value

    def update_equity(self,day,value):
        self.invested_equity[day] += value      

    def update_position(self,day,value):
        self.position[day]  += value     



    def recalculate_equity(self,day):
        self.invested_equity[day] = self.position[day] * self.price[day]






    def visualize_risk(self):
        pass

    def visualize_reward(self):
        pass

    def get_stats(self):
        pass

