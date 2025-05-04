-- Exemplos SQL Extras - Capítulo 1

-- Selecionar todos os dados de uma tabela
SELECT * FROM vendas;

-- Filtrar registros com valor acima de 500
SELECT * FROM vendas WHERE valor > 500;

-- Agrupar por categoria e somar valores
SELECT categoria, SUM(valor) as total_vendas FROM vendas GROUP BY categoria; 