CREATE DATABASE tennis;


CREATE TABLE tournamentsDT (
tournament_id INT,
tourney_name                    STRING,
tourney_location                STRING,
tourney_conditions				STRING,
tourney_year                  	INT,
tourney_surface                 STRING,
tourney_level            		STRING,
tourney_draw_size				INT,
tourney_prize_money				STRING
)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',';


CREATE TABLE playersDT (
player_id              	INT ,
player_name       		STRING,
country       			STRING,
residence       		STRING,
birthdate       		STRING,
hand					STRING,
turned_pro      		INT,
weight_kg   			INT,
height_cm       		INT
)ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';


CREATE TABLE roundDT (
round_id            INT,
round       		STRING
)ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';




CREATE TABLE matchFT (
tournament_id			INT,
winner_id				INT,
loser_id				INT,
round_id				INT,
aces					INT,
minutes 				INT,
w_1st_won_pctg			FLOAT,
l_df					INT,
w_bpSaved_pctg			FLOAT
)ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';


CREATE TABLE finals (
tournament_id	        INT,
winner_id				INT,
loser_id				INT,
aces					INT,
minutes 				INT,
w_1st_won_pctg			FLOAT,
l_df					INT,
w_bpSaved_pctg			FLOAT
)partitioned BY (round_id		INT)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';

CREATE TABLE semis (
tournament_id	        INT,
winner_id				INT,
loser_id				INT,
aces					INT,
minutes 				INT,
w_1st_won_pctg			FLOAT,
l_df					INT,
w_bpSaved_pctg			FLOAT
)partitioned BY (round_id		INT)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';



CREATE TABLE grass (
tournament_id                   INT,
tourney_name                    STRING,
tourney_location                STRING,
tourney_conditions				STRING,
tourney_year                  	INT,
tourney_level            		STRING,
tourney_draw_size				INT,
tourney_prize_money				STRING
) partitioned BY (tourney_surface  STRING)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',';

CREATE TABLE hard (
tournament_id                   INT,
tourney_name                    STRING,
tourney_location                STRING,
tourney_conditions				STRING,
tourney_year                  	INT,
tourney_level            		STRING,
tourney_draw_size				INT,
tourney_prize_money				STRING
) partitioned BY (tourney_surface  STRING)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',';

CREATE TABLE clay (
tournament_id                   INT,
tourney_name                    STRING,
tourney_location                STRING,
tourney_conditions				STRING,
tourney_year                  	INT,
tourney_level            		STRING,
tourney_draw_size				INT,
tourney_prize_money				STRING
) partitioned BY (tourney_surface  STRING)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',';

CREATE TABLE tournamentsDT_bucket (
tournament_id INT,
tourney_name                    STRING,
tourney_location                STRING,
tourney_conditions				STRING,
tourney_year                  	INT,
tourney_surface                 STRING,
tourney_level            		STRING,
tourney_draw_size				INT,
tourney_prize_money				STRING
)clustered by (tourney_year) into 5 BUCKETS
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',';

create index  country_idx on table playersdt(country) as 'BITMAP' WITH DEFERRED REBUILD ;
alter index country_idx on playersdt rebuild;

create view wimbledon as select tourney_prize_money as prize, tourney_year as year from grass where tourney_name="Wimbledon";


Load DATA LOCAL INPATH '/home/cloudera/Downloads/datasets/matchFT.csv' OVERWRITE INTO TABLE matchft;
Load DATA LOCAL INPATH '/home/cloudera/Downloads/datasets/playerDT.csv' OVERWRITE INTO TABLE playersdt;
Load DATA LOCAL INPATH '/home/cloudera/Downloads/datasets/tournamentDT.csv' OVERWRITE INTO TABLE tournamentsdt;
Load DATA LOCAL INPATH '/home/cloudera/Downloads/datasets/roundDT.csv' OVERWRITE INTO TABLE rounddt;
Load DATA LOCAL INPATH '/home/cloudera/Downloads/datasets/finals.csv' OVERWRITE INTO TABLE finals PARTITION(round_id = 7);
Load DATA LOCAL INPATH '/home/cloudera/Downloads/datasets/semis.csv' OVERWRITE INTO TABLE semis PARTITION(round_id = 6);
Load DATA LOCAL INPATH '/home/cloudera/Downloads/datasets/grass.csv' OVERWRITE INTO TABLE grass PARTITION(tourney_surface = 'Grass');
Load DATA LOCAL INPATH '/home/cloudera/Downloads/datasets/hard.csv' OVERWRITE INTO TABLE hard PARTITION(tourney_surface='Hard');
Load DATA LOCAL INPATH '/home/cloudera/Downloads/datasets/clay.csv' OVERWRITE INTO TABLE clay PARTITION(tourney_surface = 'Clay');
INSERT OVERWRITE table tournamentsdt_bucket select * FROM tournamentsdt;


