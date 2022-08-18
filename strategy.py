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
        dataframe['entry_long'] = np.where(


            #Conditions Here
            (dataframe['Close'] > 250) 


        ,1,0)

    def exit_long_conditions(self,dataframe):
        dataframe['exit_long'] = np.where(


            #Conditions Here
            (dataframe['Close'] > 300) &
            (dataframe['Close'] < 301)


        ,-1,0)




        

    def benchmark(self,type):
        self.df_length = len(self.dataframe)
        #####LUMP SUM
        if type == 'bench_lump':
            self.trigger = np.zeros(self.df_length)
            self.trigger[0] = 1
            self.dataframe['trigger'] = self.trigger

        elif type == 'bench_min_dca':
            pass

        elif type == 'bench_random_entry':
            self.trigger = np.zeros(self.df_length)
            for i in range(self.df_length):
                self.trigger[i] = np.random.choice([0,0,0,0,0,0,0,0,0,1]) #1/9 days
