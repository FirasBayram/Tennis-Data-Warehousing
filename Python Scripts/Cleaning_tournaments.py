import pandas as pd
import glob
import numpy as np
import os

df = pd.read_csv("Tournaments/tournaments_2018.csv")
df["tourney_name"] = df["tourney_name"].str[2:].str[:-1]
df["tourney_location"] = df["tourney_location"].str[2:].str[:-1]
mask = df['tourney_fin_commit'].str.contains("xe2")
df["tourney_fin_commit"][~mask] = df["tourney_fin_commit"].str[2:].str[:-1]
# df['tourney_fin_commit'] = df['tourney_fin_commit'].apply(lambda x: x.str[2:].str[:-1]if '\'$' in x else x)
df["tourney_fin_commit"][mask] = '$' + df["tourney_fin_commit"].str.partition("xac")[2].str[:-1]


df.to_csv("Tournaments/tournaments_2018.csv", index=False)


path = 'Tournaments'
all_files = glob.glob(os.path.join(path, '*.csv'))
all_matches = pd.concat((pd.read_csv(f, header=0) for f in all_files), ignore_index=True)

all_matches = all_matches[["tourney_year"  , "tourney_name" , "tourney_id" ,"tourney_slug" , "tourney_location"  , "tourney_dates" , "tourney_singles_draw"
                , "tourney_conditions" , "tourney_surface" , "tourney_fin_commit" , "tourney_year_id"]]




all_matches.to_csv("atp_tournaments.csv", index=False)
