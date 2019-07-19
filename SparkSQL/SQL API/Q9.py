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

sqlContext.sql(""" 
select * from 
(
select t.winner_id, t.loser_id ,t1.birthdate as winner_dob, t2.birthdate as loser_dob 
from matchft t
inner join playersdt t1 on t1.player_id = t.winner_id
inner join playersdt t2 on t2.player_id = t.loser_id) c
where to_timestamp(winner_dob, 'MM/DD/YYYY') > to_timestamp(loser_dob, 'MM/DD/YYYY')
""").show()

spark.stop()

