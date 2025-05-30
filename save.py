import pandas as pd

data = {
    "name": ["tanish","gyaneshwar","rahul"],
    "city": ['delhi',"uttarpradesh","rajasthan"],
    "age": [20,19,21]
}
df = pd.DataFrame(data)
print(df)

#df.to_csv("output.csv",index=False)
df.to_excel("output.xlsx",index=False)
df.to_json("output.json",index=False)

