set search_path to td;
SELECT player_name, aces,
RANK() OVER (ORDER BY aces DESC) as ranking
FROM matchft, playersdt
where winner_id = player_id
and round_id = 7
