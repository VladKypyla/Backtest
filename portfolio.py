import numpy as np
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt

class Portfolio():
    
    def update_wallet(self,day,value):
        self.wallet[day] += value

    def update_equity(self,day,value):
        self.invested_equity[day] += value      

    def update_position(self,day,value):
        self.position[day]  += value     



    def recalculate_equity(self,day):
        self.invested_equity[day] = self.position[day] * self.price[day]






    def visualize(self):
        for i in range(0,len(self.results),3):
            print(self.results[i])
            plt.plot(self.results[i+2] + self.results[i+1] )
        plt.show()
            

    def visualize_reward(self):
        pass

    def get_stats(self):
        pass

