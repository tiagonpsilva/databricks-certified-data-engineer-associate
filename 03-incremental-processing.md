# 3. Processamento Incremental de Dados

## 3.1 ACID Transactions e Delta Lake
O Delta Lake garante transações ACID (Atomicidade, Consistência, Isolamento, Durabilidade) para operações de leitura e escrita, protegendo a integridade dos dados mesmo em cenários de falha.

**Exemplo:**
- Operações de merge, update e delete em tabelas Delta são ACID.
- Time travel e rollback são possíveis graças ao transaction log.

**Exercício:**
- Explique por que transações ACID são importantes em pipelines de dados.

---

## 3.2 Tabelas e Metadados
- **Dados:** conteúdo real armazenado (linhas, arquivos Parquet).
- **Metadados:** informações sobre estrutura, histórico, permissões.
- **Tabelas gerenciadas:** Databricks controla o local dos dados.
- **Tabelas externas:** dados ficam em local definido pelo usuário.

**Exemplo:**
```sql
CREATE TABLE vendas_managed (id INT, valor DOUBLE) USING DELTA;
CREATE TABLE vendas_ext (id INT, valor DOUBLE) USING DELTA LOCATION '/mnt/dados/vendas';
```

**Exercício:**
- Liste vantagens e desvantagens de tabelas externas.

---

## 3.3 Versionamento e Histórico
O Delta Lake mantém histórico de todas as operações, permitindo auditoria, rollback e time travel.

**Exemplo:**
```sql
DESCRIBE HISTORY vendas_managed;
SELECT * FROM vendas_managed VERSION AS OF 2;
```

**Exercício:**
- Faça rollback de uma tabela Delta para uma versão anterior.

---

## 3.4 Otimização e Manutenção
- **Z-Ordering:** organiza dados para acelerar queries multidimensionais.
- **Vacuum:** remove arquivos antigos e libera espaço.
- **Optimize:** compacta arquivos pequenos em arquivos maiores.

**Exemplo:**
```sql
OPTIMIZE vendas_managed ZORDER BY (cliente_id);
VACUUM vendas_managed RETAIN 168 HOURS;
```

**Exercício:**
- Explique quando usar Z-Ordering e Optimize.

---

## 3.5 Criação e Modificação de Tabelas
- **CTAS:** cria tabela a partir de SELECT.
- **Coluna gerada:** coluna cujo valor é calculado.
- **Comentários:** documentam tabelas e colunas.
- **CREATE OR REPLACE TABLE:** substitui tabela existente.
- **INSERT OVERWRITE:** sobrescreve dados da tabela.

**Exemplo:**
```sql
CREATE TABLE vendas_top AS SELECT * FROM vendas WHERE valor > 1000;
ALTER TABLE vendas ADD COLUMN valor_com_imposto DOUBLE GENERATED ALWAYS AS (valor * 1.1);
COMMENT ON TABLE vendas IS 'Tabela de vendas processadas';
```

**Exercício:**
- Crie uma tabela com coluna gerada e comentário.

---

## 3.6 MERGE, COPY INTO e DLT
- **MERGE:** faz upsert/deduplicação ao escrever.
- **COPY INTO:** carrega dados de arquivos externos sem duplicar.
- **DLT:** pipelines declarativos para ingestão e transformação.

**Exemplo:**
```sql
MERGE INTO vendas_destino USING vendas_novas ON vendas_destino.id = vendas_novas.id
WHEN MATCHED THEN UPDATE SET valor = vendas_novas.valor
WHEN NOT MATCHED THEN INSERT *;

COPY INTO vendas_destino FROM '/mnt/novos_dados/' FILEFORMAT = CSV;
```

**Exercício:**
- Implemente um MERGE para deduplicar dados de clientes.

---

## 3.7 Delta Live Tables e Auto Loader
- **DLT:** pipelines com validação, monitoramento e automação.
- **Auto Loader:** ingestão incremental e escalável de arquivos.
- **Triggered vs Continuous:** triggered é mais barato, continuous tem menor latência.

**Exemplo:**
```python
import dlt
@dlt.table
def bronze():
    return spark.read.format('cloudFiles').option('cloudFiles.format', 'csv').load('/mnt/bronze/')
```

**Exercício:**
- Crie um pipeline DLT com Auto Loader para ingestão contínua.

---

## 3.8 Constraints e CDC
- **Constraints:** garantem integridade dos dados (PK, FK, NOT NULL).
- **ON VIOLATION DROP ROW:** descarta linhas inválidas.
- **ON VIOLATION FAIL UPDATE:** falha a operação.
- **CDC:** captura e aplica mudanças em tabelas.

**Exemplo:**
```sql
ALTER TABLE clientes ADD CONSTRAINT pk_id PRIMARY KEY (id) ENFORCED;
APPLY CHANGES INTO clientes_destino FROM changes_source;
```

**Exercício:**
- Adicione uma constraint de unicidade e teste o comportamento ao inserir duplicatas.

---

## 3.9 Auditoria e Troubleshooting
- **Event log:** permite consultar métricas, auditoria e lineage.
- **Troubleshooting DLT:** identifique notebooks com erro, uso de LIVE e STREAM.

**Exemplo:**
```sql
SELECT * FROM event_log('/pipelines/<pipeline_id>') WHERE level = 'ERROR';
```

**Exercício:**
- Consulte o event log de um pipeline DLT e identifique falhas recentes. 