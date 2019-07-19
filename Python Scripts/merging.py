import pandas as pd
import re


matches = pd.read_csv("atp_matches.csv", encoding= "iso-8859-1")
tourneys = pd.read_csv("tournaments_1877-2017_unindexed.csv", encoding= "iso-8859-1")
tourney_slug = [x for x in tourneys["tourney_slug"] if str(x) != 'nan']
mapping =  [ ('-', ' ')]
for k, v in mapping:
        tourney_slug = str(tourney_slug).replace(k, v)
print(tourney_slug)


