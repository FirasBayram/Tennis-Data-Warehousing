set search_path to td;
select tournamentsdt.tourney_surface, tournamentsdt.tourney_level, avg(matchft.l_df)
from matchft, tournamentsdt
where matchft.tournament_id = tournamentsdt.tournament_id
group by CUBE (tournamentsdt.tourney_surface, tournamentsdt.tourney_level)
order by tournamentsdt.tourney_surface