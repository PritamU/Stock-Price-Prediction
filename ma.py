#url=https://towardsdatascience.com/implementing-moving-averages-in-python-1ad28e636f9d

import pandas as pd
import numpy as np
from datetime import datetime

import matplotlib.pyplot as plt
import pyEX as p

ticker='AMD'
timeframe='1y'

df=p.chartDF(ticker,timeframe)
df=df[['close']]
df.reset_index(level=0, inplace=True)
df.columns=['ds','y']

plt.plot(df.ds,df.y)
plt.show()

rolling_mean=df.y.rolling(window=20).mean()
rolling_mean2=df.y.rolling(window=50).mean()

plt.plot(df.ds, df.y,label='AMD')
plt.plot(df.ds,rolling_mean,label='AMD 20 day SMA',color='orange')
plt.plot(df.ds,rolling_mean2,label='AMD 50 day SMA',color='magenta')
plt.legend(loc='upper_left')
plt.show()

exp1=df.y.ewm(span=20,adjust=False).mean()
exp2=df.y.ewm(span=50,adjust=False).mean()

plt.plot(df.ds,df.y,label='AMD')
plt.plot(df.ds,exp1,label='AMD 20 Day EMA')
plt.plot(df.ds,exp2,label='AMD 50 Day EMA')
plt.legend(loc='upper_left')
plt.show()