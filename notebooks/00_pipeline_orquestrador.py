# Databricks notebook source
dbutils.notebook.run("01_bronze_ingestao_ibge", 0)

dbutils.notebook.run("02_silver_tratamento_ibge", 0)

dbutils.notebook.run("03_gold_agregacao_ibge", 0)