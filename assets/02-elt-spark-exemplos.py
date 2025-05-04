# Exemplos Python - Capítulo 2: ELT com Apache Spark

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()

# Carregar todos os arquivos de um diretório em um DataFrame
vendas_df = spark.read.format('csv').option('header', 'true').load('/mnt/dados/vendas/')

# Criar uma view temporária para filtrar vendas acima de R$ 500
vendas_df.filter(col('valor') > 500).createOrReplaceTempView('vendas_filtradas')

# Remover duplicatas de uma tabela baseada em múltiplas colunas
vendas_unicas = vendas_df.dropDuplicates(['cliente_id', 'produto_id'])

# Exemplo de UDF
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

def classificar_cliente(valor):
    if valor >= 1000:
        return 'Premium'
    elif valor >= 500:
        return 'Ouro'
    else:
        return 'Padrão'

classificar_cliente_udf = udf(classificar_cliente, StringType())
vendas_df.withColumn('categoria', classificar_cliente_udf(col('valor'))) 