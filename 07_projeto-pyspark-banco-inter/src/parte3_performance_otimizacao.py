from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast, col

# Criar uma SparkSession
spark = SparkSession.builder.appName("Parte 3 - Performance e Otimizacao").getOrCreate()

# Dados fornecidos
data = [("Alice", 34, "Data Scientist"),
        ("Bob", 45, "Data Engineer"),
        ("Cathy", 29, "Data Analyst"),
        ("David", 35, "Data Scientist")]

# Definindo as colunas
columns = ["Name", "Age", "Occupation"]

# Criando o DataFrame
large_df = spark.createDataFrame(data, schema=columns)

# DataFrame pequeno
small_data = [("Data Scientist", "Team A"),
              ("Data Engineer", "Team B"),
              ("Data Analyst", "Team C")]

# Definindo as colunas
small_columns = ["Occupation", "Team"]

# Criando o DataFrame
small_df = spark.createDataFrame(small_data, schema=small_columns)

# Particionamento ajuda a dividir o DataFrame fisicamente em vários arquivos ou diretórios. Isso acelera a leitura e escrita, pois o Spark pode processar cada partição em paralelo.
# Particionar o DataFrame por "Occupation" ao salvar
large_df.write.partitionBy("Occupation").parquet("data/output/partitioned_data")

# Broadcast Join é usado quando um dos DataFrames é pequeno e pode ser copiado para todos os nós do cluster, evitando shuffles pesados.
# Broadcast join
joined_df = large_df.join(broadcast(small_df), on="Occupation", how="left")
print("\nResultado do Broadcast Join:")
joined_df.show()