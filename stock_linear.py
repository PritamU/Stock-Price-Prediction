import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

df=pd.read_csv('wikidata.csv')



#setting index as date values
#df['Date']=pd.to_datetime(df.Date,format='%m/%d/%Y')
#df.index=df['Date']

#sorting
data=df.sort_index(ascending=True,axis=0)
print(data.dtypes)

#creating a seperate database

new_data=pd.DataFrame(index=range(0,len(df)),columns=['Date','Close'])

print(new_data.head())

#Inserting values
for i in range(0,len(data)):
    new_data['Date'][i]=data['Date'][i]
    new_data['Close'][i]=data['Close'][i]

print(new_data.head())
print(data.head())

#Create Features
'''new_data['mon_fri']=0
for i in range(0,len(new_data)):
    if(new_data['Dayofweek'][i]==0 or new_data['Dayofweek'][i]==4):
        new_data['mon_fri'][i]=1
    else:
        new_data['mon_fri']=0 '''




from sklearn.model_selection import train_test_split

X=new_data['Date']
#for i in range(0,len(X)):
   # X[i]=str(X[i])
y=new_data['Close']
number_found=[]
for i in range(0,len(X)):
    found=re.findall('/',X[i])
    number_f=re.findall('[0-9]',X[i])
    number_found.append(number_f)
    print(found)
print(number_found)

nf_list=[]
for i in number_found:
    nf="".join(map(str,i))
    nf_list.append(nf)
print(nf_list)

new_data['Date']=nf_list
print(new_data.head())
print(new_data.dtypes)
X=new_data['Date'].head(1322)
y=new_data['Close'].head(1322)
X=X.values
y=y.values

X=X.reshape(661,2)
y=y.reshape(661,2)

print(type(X))
print(y.shape)






'''X_arr=np.array(X)
print(X_arr)

y_arr=np.array(y)
print(y_arr)

X_arr.reshape(661,2)
y_arr.reshape(661,2)'''

#print(X.head())
#print(y.head())


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

from sklearn.linear_model import LinearRegression
from sklearn import metrics

linreg=LinearRegression()

linreg.fit(X_train,y_train)

y_pred=linreg.predict(X_test)


pred=pd.DataFrame({'Date': X_test.flatten(),'Actual': y_test.flatten(),'Predicted':y_pred.flatten()})
print(pred)
pred.to_csv('linear_result.csv')

pred1=pred.head(25)
pred1.plot(kind='bar',figsize=(16,10))
plt.xlabel('Close')
plt.ylabel('Date')
plt.title('Stock Price Prediction Using Linear Regression')
plt.grid(which='major',linestyle='-',linewidth='0.5',color='green')
plt.grid(which='minor',linestyle=':',linewidth='0.5',color='black')
plt.show()

from sklearn import metrics

print(metrics.mean_absolute_error(y_test,y_pred))
print(metrics.mean_squared_error(y_test,y_pred))
print(np.sqrt(metrics.mean_squared_error(y_test,y_pred)))




