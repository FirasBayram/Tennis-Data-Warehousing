set search_path to td;
select tournamentsdt.tourney_surface, tournamentsdt.tourney_year,   max(gsmatches.minutes)
from gsmatches , tournamentsdt
where gsmatches.tournament_id = tournamentsdt.tournament_id
group by tournamentsdt.tourney_surface, tournamentsdt.tourney_year
order by tournamentsdt.tourney_year