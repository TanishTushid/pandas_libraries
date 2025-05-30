#step 1 sample data frame

import pandas as pd
data = {
    "name":['ram','shyam','tanish','gyaneshwer','suresh','shankar','rajesh','krishna','rahul','rishi'],
    "age":[23,45,34,23,45,23,45,34,23,45],
    'salary':[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000],
    'city':['delhi','mumbai','pune','banglore','chennai','kolkata','jaipur','bhopal','indore','agra']
}
df = pd.DataFrame(data)

print('sample data frame')
print(df)

#step 2 describe the data frame
print("displaying the description of the data")
print(df.describe())
