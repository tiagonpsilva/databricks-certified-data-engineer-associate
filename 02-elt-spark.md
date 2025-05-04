# ⚡ 2. ELT com Apache Spark

## 2.1 Extração de Dados
O Apache Spark é uma poderosa engine de processamento distribuído que permite extrair dados de diversas fontes e formatos, como CSV, Parquet, JSON, entre outros. Ele pode ler tanto arquivos individuais quanto diretórios inteiros, facilitando a ingestão de grandes volumes de dados.

Exemplo em Python:
```python
df = spark.read.csv('/mnt/dados/arquivo.csv')
df_dir = spark.read.parquet('/mnt/dados/parquet_dir/')
```
Exemplo em SQL:
```sql
SELECT * FROM parquet.`/mnt/dados/parquet_dir/`;
```
- O prefixo após FROM (ex: parquet, csv) indica o tipo de dado.

```
┌───────────────────────────────┐
│ Arquivos CSV/Parquet/JSON    │
└───────────────┬───────────────┘
                |
                v
           ┌────────┐
           │ Spark  │
           └────────┘
                |
                v
          ┌────────────┐
          │DataFrame(s)│
          └────────────┘
```

## 2.2 Criação de Views e CTEs
Views e CTEs (Common Table Expressions) facilitam a reutilização de queries, a organização do código e a legibilidade. Views temporárias permitem criar "tabelas" intermediárias na sessão Spark, enquanto CTEs estruturam consultas complexas em etapas lógicas.

Exemplo:
```sql
-- View temporária
df.createOrReplaceTempView('vendas_temp')
-- CTE
WITH vendas_filtradas AS (
  SELECT * FROM vendas_temp WHERE valor > 100
)
SELECT * FROM vendas_filtradas;
```

## 2.3 Tabelas Externas e JDBC
Tabelas externas são criadas a partir de arquivos externos (como CSV, Parquet) ou conexões JDBC (bancos de dados relacionais). Elas não utilizam Delta Lake e são úteis para integração com sistemas legados ou ingestão de dados brutos.

Exemplo:
```sql
CREATE TABLE clientes_ext USING CSV OPTIONS (path '/mnt/clientes.csv', header 'true');
CREATE TABLE pedidos_jdbc USING JDBC OPTIONS (
  url 'jdbc:mysql://...', dbtable 'pedidos', user '...', password '...');
```

## 2.4 Funções de Contagem e Deduplicação
Funções como `count_if`, `count(where x is null)` e `count(row)` permitem contar registros, ignorando ou considerando valores nulos. A deduplicação pode ser feita com DISTINCT ou funções específicas, garantindo unicidade dos dados.

Exemplo:
```sql
SELECT COUNT(*) FROM vendas WHERE valor IS NULL;
SELECT COUNT(DISTINCT cliente_id) FROM vendas;
CREATE TABLE vendas_unicas AS SELECT DISTINCT * FROM vendas;
```

## 2.5 Validações e Casts
Validações são essenciais para garantir a qualidade dos dados. Por exemplo, validar unicidade de chave primária com COUNT DISTINCT, ou converter tipos de dados (cast) para garantir consistência.

Exemplo:
```sql
SELECT COUNT(DISTINCT id) = COUNT(id) FROM clientes; -- Valida PK
SELECT CAST(data_compra AS TIMESTAMP) FROM vendas;
SELECT year(data_compra), month(data_compra) FROM vendas;
```

## 2.6 Manipulação de Dados Complexos
Spark SQL permite manipular dados aninhados (structs, arrays, JSON) usando dot syntax e funções específicas. Isso é útil para trabalhar com dados semiestruturados e listas.

Exemplo:
```sql
SELECT endereco.cidade FROM clientes;
SELECT explode(itens) FROM pedidos;
SELECT from_json(json_col, 'struct<campo1:string,campo2:int>') FROM tabela_json;
```

## 2.7 Joins, Explode, Pivot
Joins relacionam tabelas, explode transforma arrays em linhas e pivot converte dados de formato longo para largo. Essas operações são fundamentais para análises relacionais e transformação de dados.

```
┌──────────────┐      ┌──────────────┐
│ Tabela       │      │ Tabela       │
│  Vendas      │      │  Clientes    │
└───────┬──────┘      └───────┬──────┘
        |                     |
        +---------+-----------+
                  |
                [JOIN]
                  |
           ┌──────────────┐
           │Tabela Final  │
           └──────────────┘
```

Exemplo:
```sql
SELECT * FROM vendas v JOIN clientes c ON v.cliente_id = c.id;
SELECT produto, SUM(valor) FROM vendas GROUP BY produto PIVOT (SUM(valor) FOR produto IN ('A', 'B', 'C'));
```

## 2.8 UDFs e CASE/WHEN
UDFs (User Defined Functions) permitem criar funções customizadas em Python e utilizá-las em SQL. O CASE/WHEN implementa lógica condicional diretamente nas queries.

Exemplo em Python:
```python
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

def dobro(x):
    return x * 2
spark.udf.register('dobro', dobro, IntegerType())
```
Exemplo em SQL:
```sql
SELECT CASE WHEN valor > 1000 THEN 'VIP' ELSE 'Normal' END AS tipo_cliente FROM vendas;
SELECT dobro(valor) FROM vendas;
```

**Exercício:**
- Crie uma UDF para classificar clientes por faixa de valor de compra. 