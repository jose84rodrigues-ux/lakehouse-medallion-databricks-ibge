# Databricks notebook source
from pyspark.sql.functions import col, upper, trim

bronze_df = spark.table("medallion.bronze.ibge_estados")

silver_df = (
    bronze_df
    .select(
        col("id").alias("id_estado"),
        upper(trim(col("sigla"))).alias("sigla_estado"),
        trim(col("nome")).alias("nome_estado"),
        
        col("regiao.id").alias("id_regiao"),
        upper(trim(col("regiao.sigla"))).alias("sigla_regiao"),
        trim(col("regiao.nome")).alias("nome_regiao")
    )
    .dropDuplicates()
)

display(silver_df)

silver_df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("medallion.silver.ibge_estados")
    