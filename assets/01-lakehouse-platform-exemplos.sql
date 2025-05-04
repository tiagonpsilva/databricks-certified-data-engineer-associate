-- Exemplos SQL - Capítulo 1: Databricks Lakehouse Platform

-- Contar registros em uma tabela temporária
SELECT COUNT(*) FROM tabela_temporaria;

-- Criar tabela temporária
CREATE OR REPLACE TEMP VIEW vendas_temp AS SELECT * FROM vendas WHERE valor > 1000; 