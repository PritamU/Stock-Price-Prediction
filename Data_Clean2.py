import pandas as pd
import re

data=pd.read_csv('book1.csv')
print(data.head())
ticker=data['Ticker']
print(ticker)
pv=input("Enter the picker value:")

#Seperate the integers from the Picker_value
numbers=re.findall('\d',pv)
print(numbers)

#Seperate the letters from the Picker_value
letters=re.findall('[A-Z]',pv)
print(letters)

#Reverse the letters
label=letters[::-1]
print(label)

#Slice the required brand name
r_label=label[2:]
print(r_label)

#Reverse the brand name again to display properly
r_label=r_label[::-1]
print("\nThe Brand name is",r_label)

#Slice the value from the list of integers and print
value=numbers[4:]
print("\nThe value is",value)

#Slice the date and print
date=numbers[:4]
print("\nThe date is",date)




   # ACC17045000PF









