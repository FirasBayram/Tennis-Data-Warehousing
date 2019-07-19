import pandas as pd
import numpy as np
from datetime  import  datetime


p = pd.read_csv("Cleaned_Data/atp_players.csv")
r = pd.read_csv("Cleaned_Data/atp_rankings.csv")
r["Week"] = [str(x) for x in r["Week"]]

r["Week"] =  [datetime.strptime(x, '%Y%m%d').strftime('%m/%d/%Y') for x in r["Week"]]
merged = pd.merge(r.rename(columns={'Player':'player_id'}), p, on='player_id', how='left')\
    .drop(['player_name','hand'], axis=1)
merged["player_age"] = (np.floor((pd.to_datetime(merged['Week'])
                                   - pd.to_datetime(merged["birthdate"])).dt.days / 365.25))

del merged["birthdate"]

merged = merged[~merged[['Week', 'Rank', 'player_id']].apply(frozenset, axis=1).duplicated(keep='first')]


# print(df.set_index(['Week','Rank', "player_name"]).drop_duplicates())
print(merged.set_index(['Week','Rank', "player_id"]).index.is_unique)
print(len(merged))

merged.to_csv("Cleaned_Data/rankings_extended.csv", index=False)
