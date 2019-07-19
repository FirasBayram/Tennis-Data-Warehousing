import pandas as pd

df = pd.read_csv("atp_players.csv" ,encoding="iso-8859-1")
df["player_name"]  = df["name_first"] +" "+ df["name_list"]
df = df[["player_id" , "player_name" ,"hand" , "birthdate" ,"country"]]
df.to_csv("atp_player.csv")
print(df)
