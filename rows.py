import pandas as pd

#head() tail()

df = pd.read_csv("customers-100.csv", encoding='latin1')
print(df)


print("displaying first 5 rows")
print(df.head(5))
print("displaying last 5 rows")
print(df.tail(5))