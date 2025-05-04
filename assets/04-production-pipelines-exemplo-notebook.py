# Databricks Notebook - Capítulo 4: Pipelines de Produção

# COMMAND ----------
# Ingestão de dados
vendas = spark.read.format('csv').option('header', 'true').load('/mnt/dados/vendas/')
display(vendas)

# COMMAND ----------
# Limpeza de dados
vendas_limpo = vendas.dropna(subset=['cliente_id', 'valor'])

# COMMAND ----------
# Agregação
from pyspark.sql.functions import sum as _sum
vendas_agg = vendas_limpo.groupBy('produto_id').agg(_sum('valor').alias('total_vendas'))
display(vendas_agg)

# COMMAND ----------
# Carga em dashboard (simulação)
vendas_agg.write.format('delta').mode('overwrite').save('/mnt/dados/vendas_agg/')

# COMMAND ----------
# Exemplo de agendamento (comentário)
# Este notebook pode ser agendado para rodar toda segunda-feira às 8h via Databricks Jobs. 