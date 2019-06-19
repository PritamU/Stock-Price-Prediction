import pandas as pd
import re
data=pd.read_csv('prices.csv')

print(data.head())

filter=data.symbol=='WLTW'

#print(data[filter])

df=data[filter]

print(df)

data=df.sort_index(ascending=True,axis=0)




#creating a seperate database

new_data=pd.DataFrame(index=range(0,len(df)),columns=['date','close'])

print(new_data.head())

#Inserting values
for i in range(0,len(new_data)):
    new_data['date'][i]=data['date'][i]
    new_data['close'][i]=data['close'][i]

print(new_data.head())


#Create Features
'''new_data['mon_fri']=0
for i in range(0,len(new_data)):
    if(new_data['Dayofweek'][i]==0 or new_data['Dayofweek'][i]==4):
        new_data['mon_fri'][i]=1
    else:
        new_data['mon_fri']=0 '''




from sklearn.model_selection import train_test_split

#new_data['date']=pd.to_datetime(new_data['date'])
X=new_data['date']

#for i in range(0,len(X)):
   # X[i]=str(X[i])
y=new_data['close']
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

new_data['date']=nf_list
print(new_data.dtypes)

X=new_data[['date']]
y=new_data['close']


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20)

from sklearn.svm import SVR

svr=SVR(kernel='linear')

svr.fit(X_train,y_train)

y_pred=svr.predict(X_test)

pred=pd.DataFrame({'Actual':y_test,'Predicted':y_pred})
pred.to_csv('svm_result.csv')

pred1=pred.head(25)
import matplotlib.pyplot as plt
pred1.plot(kind='bar',figsize=(16,10))
plt.xlabel('Close')
plt.ylabel('Date')
plt.title('Stock Price Prediction Using Support Vector Regression')
plt.grid(which='major',linestyle='-',linewidth='0.5',color='green')
plt.grid(which='minor',linestyle=':',linewidth='0.5',color='black')
plt.show()

pred_list=y_pred.tolist()

print(pred_list)



