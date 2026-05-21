
print("Hello  - Git Databricks POC")

from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

data = [("Omkar", 1),("Sahil",1)]
df = spark.createDataFrame(data, ["name", "id"])

df.show()
print("CI/CD automation working 🚀
