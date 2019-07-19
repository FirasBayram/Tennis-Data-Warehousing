select tournamentsdt.tourney_surface, tournamentsdt.tourney_level, avg(matchft.l_df)
from matchft, tournamentsdt
where matchft.tournament_id = tournamentsdt.tournament_id
group by tournamentsdt.tourney_surface, tournamentsdt.tourney_level with cube
order by tournamentsdt.tourney_surface
