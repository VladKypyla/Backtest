from dataclasses import dataclass
import numpy as np
import datetime as dtClose
import yfinance as yf
from indicators import *
from benchmarks import Benchmarks

class Strategy(Benchmarks):


    def populate_indicators(self):
        #Indicators
        self.dataframe['rsi'] = rsi(self.dataframe['Close'])


        return None

    def entry_long_conditions(self):
        self.dataframe['entry_long'] = np.where(


            #Conditions Here
            (crossed_above(self.dataframe['rsi'], 70))


            


        ,1,0)


    def exit_long_conditions(self):
        self.dataframe['exit_long'] = np.where(

            (crossed_below(self.dataframe['rsi'], 30))

        ,-1,0)




        


