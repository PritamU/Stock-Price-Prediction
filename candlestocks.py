import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

import datetime as dt
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot');
#start=dt.datetime(2015,1,1)
#end=dt.datetime(2017,1,1)
#df=web.DataReader('^NSEI','yahoo',start,end)
#print(df.head())
#print(df.describe())
#print(df.dtypes)

#df.to_csv('nse.csv')

data=pd.read_csv('wikidata.csv',parse_dates=True, index_col=0)
print(data[['Open','Low']].head())
data['Adj. Close'].plot()
plt.show()

df_ohlc=data['Adj. Close'].resample('10D').ohlc()
df_volume=data['Volume'].resample('10D').sum()
df_ohlc.reset_index(inplace=True)

df_ohlc['Date']=df_ohlc['Date'].map(mdates.date2num)

print(df_ohlc.head())
print(df_volume.head())


ax1=plt.subplot2grid((6,1),(0,0), rowspan=5,colspan=1)
plt.title('Candlestick Graph')
ax2=plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1)



ax1.xaxis_date()

candlestick_ohlc(ax1,df_ohlc.values,width=5,colorup='g')

ax2.fill_between(df_volume.index.map(mdates.date2num),df_volume.values,0)
plt.show()
