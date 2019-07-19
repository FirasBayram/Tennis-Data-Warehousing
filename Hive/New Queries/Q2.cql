select tourney_surface, player_name, avg(aces) as averge_aces
from matchft, playersdt,tournamentsdt
where winner_id = player_id and matchft.tournament_id = tournamentsdt.tournament_id
group by tourney_surface ,  player_name
order by averge_aces desc
limit 10
