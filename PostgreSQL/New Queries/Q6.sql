set search_path to td;
SELECT matchft.tournament_id,  matchft.round_id, tournamentsdt.tourney_year, SUM(minutes) 
OVER (PARTITION BY round_id order by tournamentsdt.tourney_year) AS TotalAces
FROM matchft, tournamentsdt
where matchft.tournament_id = tournamentsdt.tournament_id
and tournamentsdt.tourney_surface = 'Grass'