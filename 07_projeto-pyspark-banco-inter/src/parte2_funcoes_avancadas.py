from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, avg
from pyspark.sql.types import StringType
from pyspark.sql.window import Window

# Criar uma SparkSession
spark = SparkSession.builder.appName("Parte 2 - Funcoes Avancadas").getOrCreate()

# Dados fornecidos
data = [("Alice", 34, "Data Scientist"),
        ("Bob", 45, "Data Engineer"),
        ("Cathy", 29, "Data Analyst"),
        ("David", 35, "Data Scientist")]

# Definindo as colunas
columns = ["Name", "Age", "Occupation"]

# Criando o DataFrame
df = spark.createDataFrame(data, schema=columns)

# Função Python para categorizar idade
def age_category(age):
    if age < 30:
        return "Jovem"
    elif 30 <= age <= 40:
        return "Adulto"
    else:
        return "Senior"

# Registrando a função como UDF
age_category_udf = udf(age_category, StringType())

# Aplicando no DataFrame
df_with_category = df.withColumn("Age_Category", age_category_udf(col("Age")))
print("\nDataFrame com categoria de idade:")
df_with_category.show()

# Criar uma janela por "Occupation"
windowSpec = Window.partitionBy("Occupation")

# Calcular a média de idade dentro da janela
occupation_avg = avg(col("Age")).over(windowSpec)

# Nova coluna com a diferença de idade para a média
df_with_diff = df.withColumn("Age_Diff_From_Avg", col("Age") - occupation_avg)
print("\nDataFrame com diferença de idade para a média:")
df_with_diff.show()