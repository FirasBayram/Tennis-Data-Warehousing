select tournamentsdt.tourney_surface, tournamentsdt.tourney_year,   max(matchft.minutes)
from matchft , tournamentsdt
where matchft.tournament_id = tournamentsdt.tournament_id
and tournamentsdt.tourney_level = 'G'
group by tournamentsdt.tourney_surface, tournamentsdt.tourney_year
order by tournamentsdt.tourney_year
