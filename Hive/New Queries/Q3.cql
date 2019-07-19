select country, wins_count from
(select country, count(*) as wins_count, 
rank() over (order by count(*)) as ranking
from matchft, playersdt, tournamentsdt
where winner_id = player_id and matchft.tournament_id= tournamentsdt.tournament_id and tourney_level='G'
group by country)c
where c.ranking =1
;
