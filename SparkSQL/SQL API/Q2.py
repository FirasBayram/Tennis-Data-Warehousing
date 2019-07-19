from pyspark.sql import functions as F
from pyspark.sql import SparkSession


# Initialize SparkSession
spark = SparkSession \
    .builder \
    .appName("Tennis App") \
    .getOrCreate()
	
	
	
matches = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql:http://127.0.0.1:61714") \
    .option("dbtable", "td.matchft") \
    .option("user", "postgres") \
    .load()

players = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql:http://127.0.0.1:61714") \
    .option("dbtable", "td.playersdt") \
    .option("user", "postgres") \
    .load()
	
tournaments = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql:http://127.0.0.1:61714") \
    .option("dbtable", "td.tournamentsdt") \
    .option("user", "postgres") \
    .load()	


finals = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql:http://127.0.0.1:61714") \
    .option("dbtable", "td.finals") \
    .option("user", "postgres") \
    .load()	

sqlContext.sql(""" select tournamentsdt.tourney_level,  playersdt.player_name, avg(matchft.w_1st_won_pctg) as first_avg
from matchft, playersdt, tournamentsdt
where matchft.winner_id = playersdt.player_id and matchft.tournament_id= tournamentsdt.tournament_id
group by tournamentsdt.tourney_level, playersdt.player_name
order by first_avg desc """).show()

spark.stop()

