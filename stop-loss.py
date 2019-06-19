import pandas as pd


df=pd.read_csv('wikidata.csv')



close=df['Close']
print(close.size)
print(close[0])
stoploss=[]

c_h_value=close[0]
for i in range(0,1323):
    if(i>0):
        if(close[i]>close[i-1]):
            print("condition successful")
            if(close[i]>c_h_value):
             c_h_value=close[i]
             print('calculated high value is ',c_h_value)
    if(close[i]<=(c_h_value-2)):
        print("stoploss in ",i)
        stoploss.append('Stoploss')
    else:
        stoploss.append('Null')


print(len(stoploss))

df['S/L']=stoploss

print(df.head(50))

df2=df.to_csv('wikiSL.csv',columns=['Date','Open','Low','High','Close','S/L'])

