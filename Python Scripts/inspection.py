import pandas as pd
import numpy as np

df = pd.read_csv("atp_tournaments.csv", encoding='ISO-8859-1')
m = pd.read_csv("atp_matches (3).csv", encoding='ISO-8859-1', nrows=147779)
m = m[["tourney_id", "tourney_name"]]
dict = m.set_index('tourney_id')['tourney_name'].to_dict()
# print(df)

for key, value in dict.items():
    df["tourney_name"] = np.where(df['tourney_year_id'] == key, value, df["tourney_name"])

a = df[["tourney_id", "tourney_name"]][:3718]
dic = a.set_index('tourney_id')['tourney_name'].to_dict()

for key, value in dic.items():
    df["tourney_name"] = np.where(df['tourney_id'] == key, value, df["tourney_name"])
df["tourney_level"]= ""
m = pd.read_csv("atp_matches (3).csv", encoding='ISO-8859-1')
m = m[["tourney_name", "tourney_level"]]
dict = m.set_index('tourney_name')['tourney_level'].to_dict()

for key, value in dict.items():
    df["tourney_level"] = np.where(df['tourney_name'] == key, value, df["tourney_level"])

df.to_csv("a.csv",encoding="ISO-8859-1", index=False)

# print(len(dict))
# print(len(set(df["tourney_name"])))