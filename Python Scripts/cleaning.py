import pandas as pd
df1 = pd.read_csv("D:/MSC UNIGE/2nd Sem/DW Project/Data/atp_matches.csv", encoding= "iso-8859-1")
df1 = df1[~(df1["tourney_level"] == 'D')]
a = df1.groupby(['tourney_name','tourney_level']).size().reset_index()
print(a[a.duplicated(["tourney_name"],keep=False)])
a.to_csv("grouped.csv")