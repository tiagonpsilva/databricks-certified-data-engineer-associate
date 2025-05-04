-- Exemplos SQL Extras - Capítulo 3

-- Atualizar valor em lote
UPDATE vendas_managed SET valor = valor * 1.05 WHERE data_compra < '2023-01-01';

-- Deletar registros antigos
DELETE FROM vendas_managed WHERE data_compra < '2022-01-01';

-- Consultar histórico de versões
DESCRIBE HISTORY vendas_managed;

-- Selecionar dados de uma versão específica
SELECT * FROM vendas_managed VERSION AS OF 5; 