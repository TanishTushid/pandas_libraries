"""
1- how to select specific columns
2- how to select specific rows
3- combine multiple comditions
"""
"""
1- square brackets
2- boolean condition

selecting columns
1- a series
2- return dataframe multiple columns of the data

filtering rows
1- boolean condition

columns = df["column_name"]
subset = df[["column_name1","column_name2"]]

row filter based on single condition

filtered_rows = df[df["column_name"] == "value"]

combine multiple conditions

filtered_rows = df[(df['salary']>5000)&(df['age']>30)]

"""
import pandas as pd

data = {
    "name":['ram','shyam','tanish','gyaneshwer','suresh','shankar','rajesh','krishna','rahul','rishi'],
    "age":[23,45,34,23,45,23,45,34,23,45],
    'salary':[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000],
    'city':['delhi','mumbai','pune','banglore','chennai','kolkata','jaipur','bhopal','indore','agra']
}

df = pd.DataFrame(data)
#display the dataframe
print("displaying the data frame")
print(df)

#selecting a single column
print("single column")
print(df["name"])

#selecting multiple columns
print("multiple columns")
print(df[["name","age"]])


