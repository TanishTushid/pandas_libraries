import pandas as pd



df = pd.read_csv("customers-100.csv", encoding='latin1')

print("displaying the infomation of the data")
print(df.info())


