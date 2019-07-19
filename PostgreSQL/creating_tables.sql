CREATE DATABASE tennis;
CREATE SCHEMA td;

SET search_path = td;
SET client_encoding = 'ISO-8859-1';

/* TOURNAMENTS */
CREATE TABLE tournamentsDT (
tournament_id                   integer NOT NULL,
tourney_name                    varchar(60),
tourney_location                varchar(40),
tourney_conditions				varchar(40),
tourney_year                  	integer,
tourney_surface                 varchar(10),
tourney_level            		varchar(10),
tourney_draw_size				integer,
tourney_prize_money				varchar(30)
);

copy tournamentsDT FROM '~/datasets/tournamentDT.csv' DELIMITER ',' CSV;

/* PLAYERS */
CREATE TABLE playersDT (
player_id              	integer NOT NULL,
player_name       		varchar(80),
country       			varchar(10),
residence       		varchar(60),
birthdate       		varchar(15),
hand					varchar(10),
turned_pro      		numeric,
weight_kg   			numeric,
height_cm       		numeric
);


copy playersDT FROM '~/datasets/playerDT.csv' DELIMITER ',' CSV;

/* ROUNDS */
CREATE TABLE roundDT (
round_id            integer NOT NULL,
round       		varchar(10)
);


copy roundDT FROM '~/datasets/roundDT.csv' DELIMITER ',' CSV;


/* MATCHES */
CREATE TABLE matchFT (
tournament_id			integer NOT NULL,
winner_id				integer NOT NULL,
loser_id				integer NOT NULL,
round_id				integer NOT NULL,
aces					numeric,
minutes 				numeric,
w_1st_won_pctg			real,
l_df					numeric,
w_bpSaved_pctg			real
);

copy matchFT FROM '~/datasets/matchFT.csv' DELIMITER ',' CSV;
