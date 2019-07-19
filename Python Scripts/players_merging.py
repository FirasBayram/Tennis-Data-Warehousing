import pandas as pd

p = pd.read_csv("atp_players.csv")
r = pd.read_csv("player_overviews.csv")

mapping =  [ ('-', ' ')]
p['player_name'] = p['player_name'].str.lower()

for k, v in mapping:
        r['player_slug'] = [x.replace(k, v) for x in r['player_slug']]

for k, v in mapping:
        p['player_name'] = [x.replace(k, v) for x in p['player_name']]

merged = pd.merge(p, r.rename(columns={'player_slug':'player_name', 'player_id':'p_id',
                                       'birthdate':'DOB'}), on='player_name', how='left')

merged = merged[['player_id', 'player_name', 'country','residence', 'birthdate', 'birthplace',
                 'hand',  'backhand', 'turned_pro',  'weight_kg', 'height_cm']]
merged['player_name'] = merged['player_name'].str.title()

merged.to_csv("players_extended.csv" , index=False)