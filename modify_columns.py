# hadding columns 

import pandas as pd
data = {
    "name":['ram','shyam','tanish','gyaneshwer','suresh','shankar','rajesh','krishna','rahul','rishi'],
    "age":[23,45,34,23,45,23,45,34,23,45],
    'salary':[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000],
    'city':['delhi','mumbai','pune','banglore','chennai','kolkata','jaipur','bhopal','indore','agra']
}
 
df = pd.DataFrame(data)

# adding columns by assign
# square brackcets df["column_name"] = some_data

print(df)

#print('*********new column add*********')

df['bonus']= df['salary']*0.1
#print(df)

#2 method using insert method (full freedom)
#df.insert(loc, "column_name", some_data)

#print('*********new column add by insert method*********')

df.insert(0, "Employee ID", [1,2,3,4,5,6,7,8,9,10])
#print(df)


#updating 
#.loc[]   for the access
#df.loc[row_index,"column_name"] = new value

print('*********update single value*********')
df.loc[0,"salary"] = 15000
#print(df)

print('*********update multiple *********')
df['salary'] = df['salary'] * 0.5
#print(df)

#removing columns
#df.drop(columns = ["columnName"], implace = True)
#multiple use [ ,  , ]
#single column
print('*********drop city *********')
df.drop(columns= ['city'], inplace=True)
print(df)
