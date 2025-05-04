# 🏝️ 1. Databricks Lakehouse Platform

## 1.1 Relação entre Data Lakehouse e Data Warehouse

O Data Warehouse tradicional é focado em dados estruturados, com forte governança, performance otimizada para BI e processos ETL bem definidos. Já o Data Lakehouse surge como uma evolução, unificando a flexibilidade do Data Lake (que armazena qualquer tipo de dado) com a governança e performance do Data Warehouse. Assim, o Lakehouse permite que empresas trabalhem com dados estruturados, semiestruturados e não estruturados, suportando desde relatórios até machine learning, tudo em uma única plataforma.

Exemplo:
- Data warehouse: tabelas SQL, ETL tradicional, dados limpos e modelados.
- Data lakehouse: arquivos Parquet/Delta, ingestão de dados brutos, processamento incremental, consultas SQL e ML no mesmo ambiente.

```
┌─────────────────────┐         ┌──────────────────────┐
│   Data Warehouse   │         │   Data Lakehouse     │
├─────────────────────┤         ├──────────────────────┤
│ Dados estruturados │         │ Dados estruturados   │
│ BI tradicional     │         │ Semiestruturados     │
│ ETL tradicional    │         │ Não estruturados     │
│ Governança forte   │         │ Governança forte     │
│ Performance alta   │         │ Performance alta     │
└─────────────────────┘         └──────────────────────┘
```

---

## 1.2 Melhoria da Qualidade de Dados no Lakehouse

O Lakehouse resolve problemas clássicos do Data Lake, como falta de controle de esquema e dificuldade de garantir integridade dos dados. Com transações ACID, versionamento e enforcement de esquema, o Lakehouse garante que os dados estejam sempre consistentes, auditáveis e prontos para uso analítico ou operacional.

Exemplo prático:
```sql
-- Consulta a uma versão anterior de uma tabela Delta
SELECT * FROM vendas VERSION AS OF 2;
```

---

## 1.3 Tabelas Bronze, Silver e Gold

A arquitetura Bronze, Silver e Gold organiza o fluxo de dados em camadas:
- **Bronze:** Dados brutos, ingestão inicial, sem tratamento.
- **Silver:** Dados limpos, validados e enriquecidos, prontos para análises intermediárias.
- **Gold:** Dados agregados e otimizados para relatórios, dashboards e consumo por áreas de negócio.

```
        [Raw Data]
             |
             v
   ┌───────┐   ┌───────┐   ┌─────┐
   │Bronze │-->|Silver │-->|Gold │
   └───────┘   └───────┘   └─────┘
       |           |           |
       v           v           v
   Ingestão    Limpeza    Agregação
```

Exemplo de pipeline multi-hop:
```sql
-- Bronze: ingestão
CREATE TABLE bronze AS SELECT * FROM raw_data;
-- Silver: limpeza
CREATE TABLE silver AS SELECT * FROM bronze WHERE status = 'OK';
-- Gold: agregação
CREATE TABLE gold AS SELECT categoria, SUM(valor) FROM silver GROUP BY categoria;
```

---

## 1.4 Arquitetura da Plataforma Databricks

A arquitetura do Databricks é dividida em dois planos:
- **Plano de Controle:** Responsável pela interface, APIs, gerenciamento e autenticação. É gerenciado pela própria Databricks.
- **Plano de Dados:** Onde ficam os clusters, arquivos e dados do cliente, hospedados na nuvem do próprio cliente.

```
   [Usuário]
       |
       v
┌───────────────────────┐
│ Plano de Controle     │
│ (UI, APIs, Mgmt)      │
└───────────────────────┘
       |
       v
┌───────────────────────┐
│ Plano de Dados        │
│ (Clusters, DBFS)      │
└───────────────────────┘
```

---

## 1.5 Clusters

- **All-purpose cluster:** Ideal para uso interativo, desenvolvimento e colaboração em notebooks.
- **Jobs cluster:** Criado sob demanda para execução de jobs agendados, otimizando recursos.
- O Databricks Runtime define o ambiente de execução, incluindo a versão do Spark e bibliotecas.
- Clusters podem ser reiniciados para atualizar dependências ou corrigir erros de ambiente.
- Clusters podem ser filtrados por permissões do usuário.
- Clusters são terminados para liberar recursos; jobs em execução são interrompidos.

Exemplo prático:
```python
# Criação de cluster via API (exemplo simplificado)
import requests
requests.post('https://<workspace-url>/api/2.0/clusters/create', json={...})
```

---

## 1.6 Notebooks

Notebooks no Databricks suportam múltiplas linguagens e facilitam a prototipação, documentação e execução de pipelines de dados. É possível alternar entre Python, SQL, Scala e R usando comandos mágicos, além de importar e exportar notebooks facilmente.

Exemplo:
```python
# Alternando linguagens
%python
df = spark.read.csv('/tmp/dados.csv')
%sql
SELECT COUNT(*) FROM tabela_temporaria
```

---

## 1.7 Databricks Repos e Versionamento

O Databricks Repos integra o ambiente com sistemas de controle de versão como GitHub e GitLab, permitindo versionar notebooks, scripts e pipelines. Isso facilita o trabalho colaborativo, CI/CD e o rastreamento de mudanças no código.

Exemplo prático:
- Adicione um repositório Git ao Databricks Repos e faça um commit de alteração em um notebook.

--- 