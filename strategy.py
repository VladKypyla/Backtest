import numpy as np
import datetime as dt
import yfinance as yf

class Strategy():
    def __init__(self,assets):
        self.dataframe = assets
    
    def populate_indicators(self,dataframe):
        #Indicators
        #dataframe['mean']= dataframe['Adj Close'].rolling(200).mean()

        return None

    def entry_long_conditions(self,dataframe):
        dataframe['enter_long'] = np.where(


            #Conditions Here
            (dataframe['Close'] > 46) &
            (dataframe['Close'] < 47) 


        ,1,0)

        return None



    def entry_long_condition(self,day):
        if (
            



        ):  self.enter_long[day] = 1
        else: self.enter_long[day] = 0