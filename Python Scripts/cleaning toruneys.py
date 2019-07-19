import pandas as pd
import numpy as np

df = pd.read_csv("D:/MSC UNIGE/2nd Sem/DW Project/Data/atp_tournaments.csv" ,encoding="iso-8859-1")

mask = df['tourney_fin_commit'].str.startswith("A")
# mask  = mask.bool()
# df["tourney_fin_commit"][mask] = df["tourney_fin_commit"].str[1:]
print (sum(mask == True))