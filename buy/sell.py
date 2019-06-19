import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('wikidata.csv')

df['Date']=pd.to_datetime(df['Date'])
df['SMA5']=df['Close'].rolling(20).mean()
df['SMA20']=df['Close'].rolling(100).mean()

#Using matplotlib to add required columns

plt.plot(df['Date'],df['Close'],linewidth=0.5,color='black')
plt.plot(df['Date'],df['SMA5'],linewidth=0.5,color='blue')
plt.plot(df['Date'],df['SMA20'],linewidth=0.5,color='c')

df['SMA5']=df['SMA5'].fillna(0)
df['SMA20']=df['SMA20'].fillna(0)

#identifying the buy/sell zone
df['Buy']=np.where((df['SMA5']>df['SMA20']),1,0)
df['Sell']=np.where((df['SMA5']<df['SMA20']),1,0)

#identifying the buy/sell signal
df['Buy_ind']=np.where((df['Buy']>df['Buy'].shift(1)),1,0)
df['Sell_ind']=np.where((df['Sell']>df['Sell'].shift(1)),1,0)
print(df.dtypes)
print(df.head(20))

#plotting the buy/sell signals on graph

plt.scatter(df.loc[df['Buy_ind']==1,'Date'].values,df.loc[df['Buy_ind']==1,'Close'].values,label='skitscat',color='green',s='25',marker='^')
plt.scatter(df.loc[df['Sell_ind']==1,'Date'].values,df.loc[df['Sell_ind']==1,'Close'].values,label='skitscat',color='red',s='25',marker='v')

#adding labels

plt.xlabel('Date')
plt.ylabel('Close')
plt.title('HDFC stock price with buy and sell signal')

plt.show()