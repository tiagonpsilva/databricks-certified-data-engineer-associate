# 2. ELT com Apache Spark

## 2.1 Extração de Dados
O Apache Spark permite extrair dados de arquivos individuais ou diretórios inteiros, suportando múltiplos formatos (CSV, Parquet, JSON, etc).

**Exemplo em Python:**
```python
df = spark.read.csv('/mnt/dados/arquivo.csv')
df_dir = spark.read.parquet('/mnt/dados/parquet_dir/')
```
**Exemplo em SQL:**
```sql
SELECT * FROM parquet.`/mnt/dados/parquet_dir/`;
```
- O prefixo após FROM (ex: parquet, csv) indica o tipo de dado.

**Exercício:**
- Carregue todos os arquivos de um diretório em um DataFrame Spark.

---

## 2.2 Criação de Views e CTEs
Views e CTEs facilitam a reutilização de queries e a organização do código.

**Exemplo:**
```sql
-- View temporária
df.createOrReplaceTempView('vendas_temp')
-- CTE
WITH vendas_filtradas AS (
  SELECT * FROM vendas_temp WHERE valor > 100
)
SELECT * FROM vendas_filtradas;
```

**Exercício:**
- Crie uma view temporária para filtrar vendas acima de R$ 500.

---

## 2.3 Tabelas Externas e JDBC
Tabelas externas não são Delta Lake e podem ser criadas a partir de conexões JDBC ou arquivos externos.

**Exemplo:**
```sql
CREATE TABLE clientes_ext USING CSV OPTIONS (path '/mnt/clientes.csv', header 'true');
CREATE TABLE pedidos_jdbc USING JDBC OPTIONS (
  url 'jdbc:mysql://...', dbtable 'pedidos', user '...', password '...');
```

**Exercício:**
- Crie uma tabela externa a partir de um arquivo Parquet.

---

## 2.4 Funções de Contagem e Deduplicação
- `count_if`, `count(where x is null)`, `count(row)` ignora NULLs.
- Deduplicação pode ser feita com DISTINCT ou funções específicas.

**Exemplo:**
```sql
SELECT COUNT(*) FROM vendas WHERE valor IS NULL;
SELECT COUNT(DISTINCT cliente_id) FROM vendas;
CREATE TABLE vendas_unicas AS SELECT DISTINCT * FROM vendas;
```

**Exercício:**
- Remova duplicatas de uma tabela baseada em múltiplas colunas.

---

## 2.5 Validações e Casts
- Valide unicidade de chave primária com COUNT DISTINCT.
- Cast de coluna para timestamp, extração de partes de data.

**Exemplo:**
```sql
SELECT COUNT(DISTINCT id) = COUNT(id) FROM clientes; -- Valida PK
SELECT CAST(data_compra AS TIMESTAMP) FROM vendas;
SELECT year(data_compra), month(data_compra) FROM vendas;
```

**Exercício:**
- Valide se todos os emails em uma tabela são únicos.

---

## 2.6 Manipulação de Dados Complexos
- Use dot syntax para acessar campos aninhados.
- Funções de array facilitam manipulação de listas.
- Parse JSON em struct para análise de dados semiestruturados.

**Exemplo:**
```sql
SELECT endereco.cidade FROM clientes;
SELECT explode(itens) FROM pedidos;
SELECT from_json(json_col, 'struct<campo1:string,campo2:int>') FROM tabela_json;
```

**Exercício:**
- Extraia todos os itens de pedidos usando explode.

---

## 2.7 Joins, Explode, Pivot
- Joins relacionam tabelas; explode transforma arrays em linhas; flatten "achata" arrays aninhados.
- PIVOT converte dados de formato longo para largo.

**Exemplo:**
```sql
SELECT * FROM vendas v JOIN clientes c ON v.cliente_id = c.id;
SELECT produto, SUM(valor) FROM vendas GROUP BY produto PIVOT (SUM(valor) FOR produto IN ('A', 'B', 'C'));
```

**Exercício:**
- Faça um join entre vendas e produtos e crie uma tabela pivoteada por categoria.

---

## 2.8 UDFs e CASE/WHEN
- UDFs permitem lógica customizada em SQL.
- CASE/WHEN implementa controle de fluxo.

**Exemplo em Python:**
```python
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

def dobro(x):
    return x * 2
spark.udf.register('dobro', dobro, IntegerType())
```
**Exemplo em SQL:**
```sql
SELECT CASE WHEN valor > 1000 THEN 'VIP' ELSE 'Normal' END AS tipo_cliente FROM vendas;
SELECT dobro(valor) FROM vendas;
```

**Exercício:**
- Crie uma UDF para classificar clientes por faixa de valor de compra. 