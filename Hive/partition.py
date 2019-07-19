import  pandas as pd

matches  = pd.read_csv("datasets/matchFT.csv",names = ["tournament_id", "winner_id", "loser_id", "round_id", "aces", "minutes", "w_1st_won_pctg", "l_df", "w_bpSaved_pctg"]
                       ,  header= None)
tournaments =  pd.read_csv("datasets/tournamentDT.csv",
                           names = ['tourney_year_id','tourney_name',  'tourney_location','tourney_conditions','tourney_year', 'tourney_surface',
                           'tourney_level','tourney_draw_size','tourney_prize_money']
                       ,  header= None, encoding='iso-8859-1')

finals = matches[matches['round_id']==7]
semis = matches[matches['round_id']==6]
del finals['round_id']
del semis['round_id']


grass  = tournaments[tournaments["tourney_surface"]== 'Grass']
hard  = tournaments[tournaments["tourney_surface"]== 'Hard']
clay  = tournaments[tournaments["tourney_surface"]== 'Clay']
del grass['tourney_surface']
del hard['tourney_surface']
del clay['tourney_surface']


finals.to_csv("datasets/finals.csv", index=False, header = None)
semis.to_csv("datasets/semis.csv", index=False, header = None)
hard.to_csv("datasets/hard.csv", index=False, header = None)
grass.to_csv("datasets/grass.csv", index=False, header = None)
clay.to_csv("datasets/clay.csv", index=False, header = None)


print(clay)