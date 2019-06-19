import pandas as pd

data=pd.read_csv('wikidata.csv')

print(data.head())

data['Date']=pd.to_datetime(data['Date'])

data.index=data['Date']

X=data['Date']
y=data['Close']

import matplotlib.pyplot as plt
from matplotlib.pyplot import rcParams
rcParams['figure.figsize']=20,10

plt.figure(figsize=(16,8))
plt.plot(data['Close'],label='Close Price')
plt.show()

data2=data.sort_index(ascending=True,axis=0)
new_data=pd.DataFrame(index=range(0,len(data)),columns=['Date','Close'])

for i in range(0,len(data2)):
    new_data['Date'][i]=data2['Date'][i]
    new_data['Close'][i]=data2['Close'][i]


print(new_data.shape)

train=new_data[:1000]
valid=new_data[1000:]

print(train.shape)
print(valid.shape)

print(train['Date'].min())
print(train['Date'].max())
print(valid['Date'].min())
print(valid['Date'].max())

#make Predictions

new_data['SMA20']=new_data['Close'].rolling(20).mean()
new_data['LMA100']=new_data['Close'].rolling(100).mean()

plt.plot(new_data['Date'],new_data['Close'],linewidth=0.8,label='Close Curve')
plt.plot(new_data['Date'],new_data['SMA20'],linewidth=0.9,label='SMA20 Curve')
plt.plot(new_data['Date'],new_data['LMA100'],linewidth=1.0,label='LMA100 curve')

plt.legend()
plt.show()

print(new_data['SMA20'])

#save moving average for the day before
prev_short_sma20=new_data['SMA20'].shift(1)
#print(prev_short_sma20)
prev_long_lma100=new_data['LMA100'].shift(1)

#select buying and selling signals:where moving averages cross
buys=new_data.loc[(new_data['SMA20']<=new_data['LMA100'])&(prev_short_sma20>=prev_long_lma100)]
sells=new_data.loc[(new_data['SMA20']>=new_data['LMA100'])& (prev_short_sma20<=prev_long_lma100)]

plt.plot(new_data['Date'],new_data['Close'],label='Close Curve')
plt.plot(new_data['Date'],new_data['SMA20'],label='20-day MA')
plt.plot(new_data['Date'],new_data['LMA100'],label='100-day MA')

#plotting the buy/sell signals on graph
plt.scatter(data.loc[data['Buy_ind']==1,'Date'].values,data.loc[data['Buy_ind']==1,'Close'].values, label='Buy',color='green',s=25,marker="^")
plt.scatter(data.loc[data['Sell_ind']==1,'Date'].values,data.loc[data['Sell_ind']==1,'Close'].values, label='Sell',color='red',s=25,marker="v")

plt.plot(buys.index,new_data.loc[buys.index]['SMA20'],'^',markersize=10,color='g')
plt.plot(sells.index,new_data.loc[sells.index]['LMA100'],'v',markersize=10,color='r')

plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend(loc=0)
plt.show()

