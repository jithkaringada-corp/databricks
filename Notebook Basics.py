# Databricks notebook source
print("Hello World")

# COMMAND ----------

# MAGIC %md
# MAGIC # Hello
# MAGIC | User Id | Name |
# MAGIC |--------|---------|
# MAGIC |1| Adam| 

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello World from SQL!"

# COMMAND ----------

# MAGIC %run ./Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets/')
print(files)

# COMMAND ----------

display(files)
