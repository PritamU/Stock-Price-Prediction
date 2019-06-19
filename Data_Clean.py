import pandas as pd

data=pd.read_csv('wikidata.csv')

data1=data['Date']
data2=data['Open']

data3=data['Close']
data4=data['Volume']
high_data=data['High']
low_data=data['Low']

print(data1.head())

data.to_csv('wikiclean.csv',columns=['Date','Open','High','Low','Close'])

clean_data=pd.read_csv('wikiclean.csv')

print(clean_data.shape)

print(clean_data.isnull())

print(clean_data.isnull().sum())

clean_data=clean_data.dropna()

import matplotlib.pyplot as plt

plt.plot(data1,data2)
plt.xlabel('Date')
plt.ylabel('Open value')
plt.show()

plt.plot(data1,data3)
plt.xlabel('Date')
plt.ylabel('Close Value')
plt.show()

plt.plot(data1,high_data)
plt.xlabel('Date')
plt.ylabel('High Value')
plt.show()

plt.plot(data1,low_data)
plt.xlabel('Data')
plt.ylabel('Low Data')
plt.show()

import numpy as np
import seaborn as sb

x=np.linspace(1,1325,100)

plt.plot(data1,data2)
sb.set_style('whitegrid')
plt.show()
