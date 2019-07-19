select winner_id, player_name, count(*) as titles_count
from finals,playersdt
where winner_id = player_id
group by winner_id ,  player_name
order by titles_count desc
Limit 10
