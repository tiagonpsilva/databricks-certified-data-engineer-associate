-- Exemplos SQL - Capítulo 3: Processamento Incremental de Dados

-- Exemplo de transação ACID com Delta Lake
MERGE INTO clientes_destino USING novos_clientes
ON clientes_destino.id = novos_clientes.id
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *;

-- Rollback de uma tabela Delta para uma versão anterior
RESTORE TABLE vendas_managed TO VERSION AS OF 2;

-- Otimização de tabela
OPTIMIZE vendas_managed ZORDER BY (produto_id);

-- Adicionar constraint de unicidade
ALTER TABLE clientes ADD CONSTRAINT email_unico UNIQUE (email); 