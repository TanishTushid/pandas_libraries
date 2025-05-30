"""
1- how big is your data set
2- how many columns are there
3- shape and columns
"""



import pandas as pd
data = {
    "name":['ram','shyam','tanish','gyaneshwer','suresh','shankar','rajesh','krishna','rahul','rishi'],
    "age":[23,45,34,23,45,23,45,34,23,45],
    'salary':[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000],
    'city':['delhi','mumbai','pune','banglore','chennai','kolkata','jaipur','bhopal','indore','agra']
}
df = pd.DataFrame(data)
print(df)
print(f'shape: {df.shape}')
print(f'columns name: {df.columns}')