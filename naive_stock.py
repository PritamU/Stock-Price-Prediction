import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

df=pd.read_csv('wikiclean.csv')
df['Close']=df['Close'].astype(int)
X=df[['Date']]
y=df['Close']

print(y.dtype)
print(X.head())

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25)

from sklearn.naive_bayes import GaussianNB

gnb=GaussianNB()

gnb.fit(X_train,y_train)

y_pred=gnb.predict(X_test)

pred=pd.DataFrame({'Actual':y_test, 'Predicted':y_pred.flatten()})

print(pred)

import matplotlib.pyplot as plt

pred1=pred.head(25)

pred1.plot(kind='bar',figsize=(16,10))

plt.grid(which='major',linestyle='-',linewidth='0.5',color='green')
plt.grid(which='minor',linestyle=':',linewidth='0.5',color='black')
plt.xlabel('Close')
plt.ylabel('Date')
plt.title('Stock Price Prediction Using Naive Bayes')

plt.show()


from sklearn import metrics

print(metrics.accuracy_score(y_test,y_pred)*100)