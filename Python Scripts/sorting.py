import pandas as pd
import dateutil

df = pd.read_csv("Cleaned_Data/atp_matches.csv" , encoding="iso-8859-1")
df = df[~(df["tourney_level"] == 'D')]
df['tourney_date'] = [dateutil.parser.parse(x) for x in df['tourney_date']]
df = df.sort_values("tourney_date")

df.to_csv("sorted.csv")
