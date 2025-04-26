from pyspark.sql import SparkSession

# Criar uma SparkSession
spark = SparkSession.builder.appName("Parte 4 - Integracao").getOrCreate()

# Leitura de um arquivo CSV
csv_df = spark.read.csv("data/input/arquivo.csv", header=True, inferSchema=True)

# Escrita em Parquet
csv_df.write.parquet("data/output/arquivo_parquet")


# O PySpark se conecta ao Hadoop HDFS usando o Hadoop client instalado no cluster. O Spark entende URIs como hdfs://.
# Leitura de arquivo do HDFS
hdfs_df = spark.read.csv("hdfs://namenode:9000/dados/arquivo.csv", header=True, inferSchema=True)

# Escrevendo de volta para o HDFS
hdfs_df.write.parquet("hdfs://namenode:9000/dados/saida_parquet")