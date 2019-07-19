select finals.tournament_id, playersdt.player_name, max(finals.aces)  as aces_max
from finals, playersdt
where finals.winner_id = playersdt.player_id 
group by finals.tournament_id , playersdt.player_name
order by aces_max desc
