# Databricks notebook source
# MAGIC %md
# MAGIC ### Data Reading 
# MAGIC

# COMMAND ----------

dbutils.fs.ls('/Volumes/practice/default/test_volumn/')

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *
df= spark.read.format('csv').option('inferSchema',True).option('header',True).load('/Volumes/practice/default/test_volumn/BigMart Sales.csv')
df.schema

# COMMAND ----------

df.display()

# COMMAND ----------

df.select(col('Item_Identifier').alias('Item_id')).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Filter / Where
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Senario -1 

# COMMAND ----------

df.filter((col('Item_Fat_Content') == 'Regular') & (col('Item_Type') == 'Soft Drinks')).display()

# COMMAND ----------

# MAGIC %md 
# MAGIC ### Senario -2 

# COMMAND ----------

df.filter((col('Outlet_Size').isNull()) & (col('Outlet_Location_type') == 'Tier 1')).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###
