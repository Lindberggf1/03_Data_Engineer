from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Criar uma SparkSession
spark = SparkSession.builder.appName("Parte 5 - Processamento de Logs").getOrCreate()

# Carregar o arquivo de log
df_logs = spark.read.csv("data/input/logs.csv", header=True, inferSchema=True)

# Contar o número de ações por usuário
user_actions = df_logs.groupBy("user_id").count()

# Top 10 usuários mais ativos
top_10_users = user_actions.orderBy(col("count").desc()).limit(10)

# Verificar o DataFrame
top_10_users.show()

# Salvar o resultado em CSV
top_10_users.write.csv("data/output/top_10_users", header=True)