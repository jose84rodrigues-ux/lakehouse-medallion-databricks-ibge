# Databricks notebook source
from pyspark.sql.functions import count

silver_df = spark.table("medallion.silver.ibge_estados")

gold_df = (
    silver_df
    .groupBy("nome_regiao")
    .agg(
        count("id_estado").alias("quantidade_estados")
    )
)

display(gold_df)

gold_df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("medallion.gold.ibge_estados_regiao")