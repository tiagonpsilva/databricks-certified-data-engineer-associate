# 🏝️ 1. Databricks Lakehouse Platform

## 1.1 Relação entre Data Lakehouse e Data Warehouse

```
+-------------------+         +-------------------+
|   Data Warehouse  |         |   Data Lakehouse  |
+-------------------+         +-------------------+
| Dados estruturados|         | Dados estruturados|
| BI tradicional    |         | + semiestruturados|
| ETL tradicional   |         | + não estruturados|
| Governança forte  |         | Governança forte  |
| Performance alta  |         | Performance alta  |
+-------------------+         +-------------------+
```
O data lakehouse combina a flexibilidade e baixo custo do data lake com a governança, performance e confiabilidade do data warehouse. Enquanto o data warehouse é ótimo para dados estruturados e BI, o lakehouse permite trabalhar com dados estruturados, semiestruturados e não estruturados, suportando workloads de BI, ciência de dados e machine learning em uma única plataforma.

**Exemplo:**
- Data warehouse: tabelas SQL, ETL tradicional, dados limpos e modelados.
- Data lakehouse: arquivos Parquet/Delta, ingestão de dados brutos, processamento incremental, consultas SQL e ML no mesmo ambiente.

**Exercício:**
- Liste três vantagens do lakehouse sobre o data warehouse tradicional.

---

## 1.2 Melhoria da Qualidade de Dados no Lakehouse
O lakehouse melhora a qualidade dos dados em relação ao data lake tradicional por meio de:
- Transações ACID: garante consistência e integridade dos dados.
- Versionamento: permite consultar versões anteriores dos dados (time travel).
- Schema enforcement: impede gravação de dados fora do padrão.

**Exemplo prático:**
```sql
-- Consulta a uma versão anterior de uma tabela Delta
SELECT * FROM vendas VERSION AS OF 2;
```

**Exercício:**
- Explique como o schema enforcement pode evitar problemas de qualidade de dados.

---

## 1.3 Tabelas Bronze, Silver e Gold
- **Bronze:** dados brutos, ingestão inicial.
- **Silver:** dados limpos, transformados e enriquecidos.
- **Gold:** dados prontos para análise, agregados e otimizados para BI.

```
[Raw Data] -> [Bronze] -> [Silver] -> [Gold] -> [BI/Analytics]
```

**Exemplo de pipeline multi-hop:**
```sql
-- Bronze: ingestão
CREATE TABLE bronze AS SELECT * FROM raw_data;
-- Silver: limpeza
CREATE TABLE silver AS SELECT * FROM bronze WHERE status = 'OK';
-- Gold: agregação
CREATE TABLE gold AS SELECT categoria, SUM(valor) FROM silver GROUP BY categoria;
```

**Exercício:**
- Dê um exemplo de workload que consome uma tabela gold.

---

## 1.4 Arquitetura da Plataforma Databricks

```
Usuário
  |
  v
+-------------------+
| Plano de Controle |
| (UI, APIs, Mgmt)  |
+-------------------+
  |
  v
+-------------------+
| Plano de Dados    |
| (Clusters, DBFS)  |
+-------------------+
```
A arquitetura é dividida em plano de controle (UI, APIs, gerenciamento) e plano de dados (clusters, DBFS, dados do cliente). O plano de controle é gerenciado pela Databricks; o plano de dados reside na cloud do cliente.

**Desenho simplificado:**
```
[Usuário] -> [Plano de Controle (UI, APIs)] -> [Plano de Dados (Clusters, DBFS, Dados)]
```

**Exercício:**
- Explique a diferença entre plano de controle e plano de dados.

---

## 1.5 Clusters
- **All-purpose cluster:** uso interativo, notebooks, colaboração.
- **Jobs cluster:** criado sob demanda para execução de jobs agendados.
- O Databricks Runtime define a versão do Spark e bibliotecas.
- Clusters podem ser filtrados por permissões do usuário.
- Clusters são terminados para liberar recursos; jobs em execução são interrompidos.
- Reiniciar cluster é útil após atualização de bibliotecas ou erro de ambiente.

**Exemplo prático:**
```python
# Criação de cluster via API (exemplo simplificado)
import requests
requests.post('https://<workspace-url>/api/2.0/clusters/create', json={...})
```

**Exercício:**
- Quando é melhor usar um job cluster em vez de um all-purpose cluster?

---

## 1.6 Notebooks
- Suporte a múltiplas linguagens: use comandos mágicos (%python, %sql, %scala, %r).
- Para rodar um notebook dentro de outro: `%run ./outro_notebook`
- Notebooks podem ser compartilhados via link, permissões ou exportação.

**Exemplo:**
```python
# Alternando linguagens
%python
df = spark.read.csv('/tmp/dados.csv')
%sql
SELECT COUNT(*) FROM tabela_temporaria
```

**Exercício:**
- Importe um notebook externo e execute comandos em duas linguagens diferentes.

---

## 1.7 Databricks Repos e Versionamento
- Databricks Repos permite integração com GitHub/GitLab para CI/CD.
- Operações disponíveis: clone, commit, push, pull, branch, merge.
- Limitações: versionamento de notebooks nativo não suporta branches, merge ou histórico detalhado como o Git.

**Exemplo prático:**
- Adicione um repositório Git ao Databricks Repos e faça um commit de alteração em um notebook.

**Exercício:**
- Liste duas vantagens de usar Repos em vez do versionamento nativo de notebooks. 