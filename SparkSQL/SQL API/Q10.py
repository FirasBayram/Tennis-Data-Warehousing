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

sqlContext.sql(""" select tournamentsdt.tourney_surface, matchft.round_id, avg(matchft.minutes) as minutes_avg
from matchft, tournamentsdt
where matchft.tournament_id = tournamentsdt.tournament_id
GROUP BY cube (tournamentsdt.tourney_surface, matchft.round_id)

""").show()


spark.stop()
