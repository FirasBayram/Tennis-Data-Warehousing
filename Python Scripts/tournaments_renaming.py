import pandas as pd
import numpy as np

df = pd.read_csv("atp_tournaments.csv", encoding='ISO-8859-1', nrows=147779)
f = pd.read_csv("atp_matches.csv", encoding='ISO-8859-1')
m = f[["tourney_id", "tourney_name"]]
dict = m.set_index('tourney_id')['tourney_name'].to_dict()

for key, value in dict.items():
    df["tourney_name"] = np.where(df['tourney_year_id'] == key, value, df["tourney_name"])

a = df[["tourney_id", "tourney_name"]][:3718]
dic = a.set_index('tourney_id')['tourney_name'].to_dict()

for key, value in dic.items():
    df["tourney_name"] = np.where(df['tourney_id'] == key, value, df["tourney_name"])

del df['tourney_slug']

merged = df.rename(columns={'tourney_singles_draw': 'tourney_draw_size'
    , 'tourney_fin_commit': 'tourney_prize_money'})
merged["tourney_id"] = np.where(merged['tourney_name'] == "Nice", 305, merged["tourney_id"])
merged["tourney_year_id"] = np.where(merged['tourney_name'] == "Nice", merged["tourney_year_id"] + str(305),
                                     merged["tourney_year_id"])
merged["tourney_id"] = np.where(merged['tourney_name'] == "Tokyo WCT", 329, merged["tourney_id"])
merged["tourney_year_id"] = np.where(merged['tourney_name'] == "Tokyo WCT", merged["tourney_year_id"] + str(329),
                                     merged["tourney_year_id"])

merged["tourney_location"] = np.where(
    (merged['tourney_year'] >= 2009) & (merged['tourney_year'] <= 2018) & (merged["tourney_name"] == "Tour Finals"),
    "London", merged["tourney_location"])


merged["tourney_location"] = np.where(
    (merged['tourney_year'] >= 2005) & (merged['tourney_year'] <= 2008) & (merged["tourney_name"] == "Tour Finals"),
    "Shanghai", merged["tourney_location"])

merged["tourney_location"] = np.where(
    (merged['tourney_year'] >= 2003) & (merged['tourney_year'] <= 2004) & (merged["tourney_name"] == "Tour Finals"),
    "Houston", merged["tourney_location"])

merged["tourney_location"] = np.where(
    (merged['tourney_year'] >= 2002) & (merged['tourney_year'] <= 2002) & (merged["tourney_name"] == "Tour Finals"),
    "Shanghai", merged["tourney_location"])

merged["tourney_location"] = np.where(
    (merged['tourney_year'] >= 2001) & (merged['tourney_year'] <= 2001) & (merged["tourney_name"] == "Tour Finals"),
    "Sydney", merged["tourney_location"])

merged["tourney_location"] = np.where(
    (merged['tourney_year'] >= 2000) & (merged['tourney_year'] <= 2000) & (merged["tourney_name"] == "Tour Finals"),
    "Lisbon", merged["tourney_location"])

merged["tourney_location"] = np.where(
    (merged['tourney_year'] >= 1996) & (merged['tourney_year'] <= 1999) & (merged["tourney_name"] == "Tour Finals"),
    "Hanover", merged["tourney_location"])

merged["tourney_location"] = np.where(
    (merged['tourney_year'] >= 1990) & (merged['tourney_year'] <= 1995) & (merged["tourney_name"] == "Tour Finals"),
    "Frankfurt", merged["tourney_location"])


merged["tourney_location"] = np.where(
    (merged['tourney_year'] >= 1990) & (merged['tourney_year'] <= 1995) & (merged["tourney_name"] == "Tour Finals"),
    "Frankfurt", merged["tourney_location"])

merged["tourney_location"] = np.where(
    (merged['tourney_year'] >= 1977) & (merged['tourney_year'] <= 1989) & (merged["tourney_name"] == "Tour Finals"),
    "New York City", merged["tourney_location"])

merged["tourney_location"] = np.where(
    (merged['tourney_year'] >= 1976) & (merged['tourney_year'] <= 1976) & (merged["tourney_name"] == "Tour Finals"),
    "Houston", merged["tourney_location"])


merged["tourney_location"] = np.where(
    (merged['tourney_year'] >= 1975) & (merged['tourney_year'] <= 1975) & (merged["tourney_name"] == "Tour Finals"),
    "Stockholm", merged["tourney_location"])

merged["tourney_location"] = np.where(
    (merged['tourney_year'] >= 1974) & (merged['tourney_year'] <= 1974) & (merged["tourney_name"] == "Tour Finals"),
    "Melbourne", merged["tourney_location"])

merged["tourney_location"] = np.where(
    (merged['tourney_year'] >= 1973) & (merged['tourney_year'] <= 1973) & (merged["tourney_name"] == "Tour Finals"),
    "Boston", merged["tourney_location"])
merged["tourney_location"] = np.where(
    (merged['tourney_year'] >= 1972) & (merged['tourney_year'] <= 1972) & (merged["tourney_name"] == "Tour Finals"),
    "Barcelona", merged["tourney_location"])
merged["tourney_location"] = np.where(
    (merged['tourney_year'] >= 1971) & (merged['tourney_year'] <= 1971) & (merged["tourney_name"] == "Tour Finals"),
    "Paris", merged["tourney_location"])
merged["tourney_location"] = np.where(
    (merged['tourney_year'] >= 1970) & (merged['tourney_year'] <= 1970) & (merged["tourney_name"] == "Tour Finals"),
    "Tokyo", merged["tourney_location"])
merged["tourney_level"] = ""

c = f[["tourney_name" , "tourney_level"]]
dict = c.set_index('tourney_name')['tourney_level'].to_dict()

for key, value in dict.items():
    merged["tourney_level"] = np.where(merged['tourney_name'] == key, value, merged["tourney_level"])
filter = merged["tourney_level"] != ""
merged = merged[filter]

merged.to_csv("tournaments_renamed.csv", index=False, encoding="ISO-8859-1")

# print(merged.describe())
