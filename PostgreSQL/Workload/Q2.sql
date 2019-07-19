set search_path to td;
select tournamentsdt.tourney_level,  playersdt.player_name, avg(matchft.w_1st_won_pctg) as first_avg
from matchft, playersdt, tournamentsdt
where matchft.winner_id = playersdt.player_id and matchft.tournament_id= tournamentsdt.tournament_id
group by tournamentsdt.tourney_level, playersdt.player_name
order by first_avg desc