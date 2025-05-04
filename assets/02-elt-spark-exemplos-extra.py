# Exemplos Python Extras - Capítulo 2

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max as max_, min as min_

spark = SparkSession.builder.getOrCreate()

# Leitura de dados em Parquet
clientes_df = spark.read.parquet('/mnt/dados/clientes/')

# Join entre DataFrames
vendas_df = spark.read.csv('/mnt/dados/vendas.csv', header=True)
joined = vendas_df.join(clientes_df, vendas_df['cliente_id'] == clientes_df['id'], 'inner')

# Agregação: média, máximo e mínimo
stats = vendas_df.agg(avg('valor').alias('media'), max_('valor').alias('maximo'), min_('valor').alias('minimo'))
stats.show()

# Seleção de colunas e filtro
vendas_df.select('produto', 'valor').filter(vendas_df['valor'] > 1000).show() 