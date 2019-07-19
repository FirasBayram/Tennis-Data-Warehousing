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

joined = matches.join(tournaments.select("_c0", "_c5").withColumnRenamed('_c5', '_c9'), on = matches._c0 == tournaments._c0)
joined.groupby("_c9").agg(F.avg("_c6").alias("serve_average")).show()
spark.stop()
