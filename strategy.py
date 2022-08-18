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
        dataframe['trigger'] = np.where(


            #Conditions Here
            (dataframe['Close'] > 46) &
            (dataframe['Close'] < 47) 


        ,1,0)

        return None

    def exit_long_conditions(self,dataframe):
        dataframe['trigger'] = np.where(


            #Conditions Here
            (dataframe['Close'] > 200) &
            (dataframe['Close'] < 201)


        ,-1,0)

        return None

