# Databricks notebook source

# Import SparkSession
from pyspark.sql import SparkSession

# Create SparkSession 
spark = SparkSession.builder \
      .master("local[1]") \
      .appName("SparkSimplePipeline") \
      .getOrCreate() 


# COMMAND ----------


# Create RDD from parallelize    
dataList = [("Java", 20000), ("Python", 100000), ("Scala", 3000)]
rdd=spark.sparkContext.parallelize(dataList)


# COMMAND ----------



# COMMAND ----------


