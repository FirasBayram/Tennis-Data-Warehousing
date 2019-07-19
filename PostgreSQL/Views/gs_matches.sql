set search_path to td;
CREATE VIEW gsmatches AS
    SELECT matchft.tournament_id, matchft.winner_id, matchft.loser_id, matchft.round_id,
	matchft.aces, matchft.minutes, matchft.w_1st_won_pctg, matchft.w_bpsaved_pctg, matchft.l_df
    FROM matchft, tournamentsdt
    WHERE matchft.tournament_id = tournamentsdt.tournament_id
	and tournamentsdt.tourney_level='G';