
import pandas as pd

data = {
    "name":['ram','shyam','tanish','gyaneshwer','suresh','shankar','rajesh','krishna','rahul','rishi'],
    "age":[23,45,34,23,45,23,45,34,23,45],
    'salary':[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000],
    'city':['delhi','mumbai','pune','banglore','chennai','kolkata','jaipur','bhopal','indore','agra']
}

df = pd.DataFrame(data)
print(df)

print("*********************************************")
print("high salary")
print("*********************************************")
high_salary = df[df['salary']>5000]
print(high_salary)
print("*********************************************")
print("salary<5000 and age >30")
print("*********************************************")
filterd = df[(df['salary']<5000)&(df['age']>30)]
print(filterd)
print("*********************************************")
filtered = df[(df['age']>34)|(df['salary']<5000)]
print(filtered)
