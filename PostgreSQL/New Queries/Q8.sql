set search_path to td;
SELECT tournamentsdt.tourney_name, tourney_year,  minutes,
SUM(minutes) OVER(PARTITION BY tournamentsdt.tournament_id order by tourney_year
				  Rows UNBOUNDED PRECEDING) AS CumMIn
FROM matchft, tournamentsdt
where matchft.tournament_id = tournamentsdt.tournament_id
and winner_id = 103819 