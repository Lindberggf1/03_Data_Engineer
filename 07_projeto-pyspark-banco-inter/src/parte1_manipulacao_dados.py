from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Criar uma SparkSession
spark = SparkSession.builder.appName("Parte 1 - Manipulacao de Dados").getOrCreate()

# Dados fornecidos
data = [("Alice", 34, "Data Scientist"),
        ("Bob", 45, "Data Engineer"),
        ("Cathy", 29, "Data Analyst"),
        ("David", 35, "Data Scientist")]

# Definindo as colunas
columns = ["Name", "Age", "Occupation"]

# Criando o DataFrame
df = spark.createDataFrame(data, schema=columns)
print("\nDataFrame original:")
df.show()

# Filtragem e Seleção
# Selecionar apenas "Name" e "Age"
df_select = df.select("Name", "Age")

# Filtrar as idades maiores que 30
df_filtered = df_select.filter(col("Age") > 30)
print("\nDataFrame com Name e Age > 30:")
df_filtered.show()

# Agrupar por "Occupation" e calcular a média de "Age"
df_grouped = df.groupBy("Occupation").avg("Age")
print("\nMédia de Age por Occupation:")
df_grouped.show()

# Ordenar pela média de "Age" de forma decrescente
df_sorted = df_grouped.orderBy(col("avg(Age)").desc())
print("\nOrdenado pela média de Age (decrescente):")
df_sorted.show()