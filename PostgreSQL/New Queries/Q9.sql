set search_path to td;
SELECT  tourney_name, tourney_year, aces,
AVG(aces) OVER (PARTITION BY tourney_name ORDER BY tourney_year ROWS 4 PRECEDING)AS MobileAvg
FROM matchft, tournamentsdt
where matchft.tournament_id = tournamentsdt.tournament_id
and winner_id = 103819 and tourney_level = 'G'