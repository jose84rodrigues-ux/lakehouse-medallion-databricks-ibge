# Databricks notebook source
import requests
import pandas as pd

url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

response = requests.get(url)

data = response.json()

df = pd.DataFrame(data)

spark_df = spark.createDataFrame(df)

display(spark_df)

spark_df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("medallion.bronze.ibge_estados")