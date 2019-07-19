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
  
  
from pyspark.sql.functions import unix_timestamp
from pyspark.sql.functions import from_unixtime
finals = matches.where("_c3 == 7").select("_c1", "_c2")
joined1 = finals.join(players.select("_c0", from_unixtime(unix_timestamp("_c4", 'MM/dd/yyy')).alias('winner_dob')), on = finals._c1 == players._c0)\
    .select('_c1','_c2', 'winner_dob')
joined = joined1.join(players.select("_c0", from_unixtime(unix_timestamp("_c4", 'MM/dd/yyy')).alias("loser_dob")),  on = joined1._c2 == players._c0)\
    .select('_c1','_c2', 'winner_dob','loser_dob')
results = joined.filter(F.col("winner_dob") > F.col("loser_dob"))

results.show()
spark.stop()
