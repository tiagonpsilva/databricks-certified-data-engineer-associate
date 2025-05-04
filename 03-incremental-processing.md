# 🔄 3. Processamento Incremental de Dados

## 3.1 ACID Transactions e Delta Lake

O Delta Lake é uma camada de armazenamento que traz transações ACID (Atomicidade, Consistência, Isolamento, Durabilidade) para o mundo do big data. Isso significa que operações de leitura e escrita são seguras, consistentes e recuperáveis, mesmo em caso de falhas. O transaction log do Delta Lake permite rollback, time travel e garante integridade dos dados.

Diagrama ASCII:
```
+-------------------+
|   Delta Lake      |
+-------------------+
| ACID Transactions |
| Time Travel       |
| Rollback          |
+-------------------+
```

Exemplo:
- Operações de merge, update e delete em tabelas Delta são ACID.
- Time travel e rollback são possíveis graças ao transaction log.

## 3.2 Tabelas e Metadados

No Databricks, os dados são organizados em tabelas, que podem ser gerenciadas (controladas pelo Databricks) ou externas (armazenadas em local definido pelo usuário). Cada tabela possui dados (arquivos Parquet/Delta) e metadados (estrutura, histórico, permissões).

Exemplo:
```sql
CREATE TABLE vendas_managed (id INT, valor DOUBLE) USING DELTA;
CREATE TABLE vendas_ext (id INT, valor DOUBLE) USING DELTA LOCATION '/mnt/dados/vendas';
```

## 3.3 Versionamento e Histórico

O Delta Lake mantém o histórico de todas as operações realizadas em uma tabela, permitindo auditoria, rollback e time travel. Cada alteração gera uma nova versão da tabela, que pode ser consultada a qualquer momento.

Diagrama ASCII:
```
[Operação 1] -> [Operação 2] -> [Operação 3]
      |             |             |
   Versão 1      Versão 2      Versão 3
```

Exemplo:
```sql
DESCRIBE HISTORY vendas_managed;
SELECT * FROM vendas_managed VERSION AS OF 2;
```

## 3.4 Otimização e Manutenção

Para garantir performance e economia de recursos, o Delta Lake oferece comandos de otimização:
- **Z-Ordering:** organiza dados para acelerar queries multidimensionais.
- **Vacuum:** remove arquivos antigos e libera espaço.
- **Optimize:** compacta arquivos pequenos em arquivos maiores.

Exemplo:
```sql
OPTIMIZE vendas_managed ZORDER BY (cliente_id);
VACUUM vendas_managed RETAIN 168 HOURS;
```

## 3.5 Criação e Modificação de Tabelas

O Databricks permite criar tabelas a partir de SELECTs (CTAS), adicionar colunas geradas, documentar tabelas e sobrescrever dados de forma eficiente.

Exemplo:
```sql
CREATE TABLE vendas_top AS SELECT * FROM vendas WHERE valor > 1000;
ALTER TABLE vendas ADD COLUMN valor_com_imposto DOUBLE GENERATED ALWAYS AS (valor * 1.1);
COMMENT ON TABLE vendas IS 'Tabela de vendas processadas';
```

## 3.6 MERGE, COPY INTO e DLT

Essas operações facilitam ingestão incremental e deduplicação:
- **MERGE:** faz upsert/deduplicação ao escrever.
- **COPY INTO:** carrega dados de arquivos externos sem duplicar.
- **DLT (Delta Live Tables):** pipelines declarativos para ingestão e transformação.

Diagrama ASCII:
```
[Novos Dados] ---> [MERGE] ---> [Tabela Destino]
[Arquivos Externos] ---> [COPY INTO] ---> [Tabela Destino]
```

Exemplo:
```sql
MERGE INTO vendas_destino USING vendas_novas ON vendas_destino.id = vendas_novas.id
WHEN MATCHED THEN UPDATE SET valor = vendas_novas.valor
WHEN NOT MATCHED THEN INSERT *;

COPY INTO vendas_destino FROM '/mnt/novos_dados/' FILEFORMAT = CSV;
```

## 3.7 Delta Live Tables e Auto Loader

O Delta Live Tables (DLT) permite criar pipelines de dados declarativos, com validação, monitoramento e automação. O Auto Loader facilita a ingestão incremental e escalável de arquivos, suportando modos triggered (mais barato) e continuous (menor latência).

Exemplo:
```python
import dlt
@dlt.table
def bronze():
    return spark.read.format('cloudFiles').option('cloudFiles.format', 'csv').load('/mnt/bronze/')
```

## 3.8 Constraints e CDC

Constraints garantem integridade dos dados (PK, FK, NOT NULL). O CDC (Change Data Capture) permite capturar e aplicar mudanças em tabelas, facilitando integrações e auditoria.

Exemplo:
```sql
ALTER TABLE clientes ADD CONSTRAINT pk_id PRIMARY KEY (id) ENFORCED;
APPLY CHANGES INTO clientes_destino FROM changes_source;
```

## 3.9 Auditoria e Troubleshooting

O event log do Databricks permite consultar métricas, auditoria e lineage de pipelines. Para troubleshooting, é possível identificar notebooks com erro, uso de LIVE e STREAM, e analisar logs detalhados.

Exemplo:
```sql
SELECT * FROM event_log('/pipelines/<pipeline_id>') WHERE level = 'ERROR';
``` 