# NaN (not a number)
# None (for object data types)

# first identify where is data empty

#isnull()   true = NaN is missing, false value is present


import pandas as pd

data = {
    "name":['ram',None,'tanish','gyaneshwer','suresh','shankar','rajesh','krishna','rahul','rishi'],
    "age":[23,None,34,23,45,23,45,34,23,45],
    'salary':[1000,None,3000,4000,5000,6000,7000,8000,9000,10000],
    'city':['delhi',None,'pune','banglore','chennai','kolkata','jaipur','bhopal','indore','agra']
}

df = pd.DataFrame(data)
print(df)
print(df.isnull())
#number of missing value
print(df.isnull().sum())

#missing value drop 
#dropna() r 0 , c 1 
#df.dropna(axis = 0, inplace = True)

#df.dropna(inplace=True)
#print(df)

#fillna(value,inplace = True)
#df.fillna(0,inplace = True)

df['age'].fillna(df['age'].mean(), inplace = True)
print(df)