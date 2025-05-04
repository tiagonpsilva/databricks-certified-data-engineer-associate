-- Exemplos SQL - Capítulo 5: Governança de Dados

-- Criação de catálogo e schema
CREATE CATALOG marketing;
CREATE SCHEMA marketing.vendas;

-- Criação de tabela com Unity Catalog
CREATE TABLE marketing.vendas.campanhas (
  id INT,
  nome STRING,
  data_inicio DATE
);

-- Conceder permissão de leitura
GRANT SELECT ON TABLE marketing.vendas.campanhas TO `analista@empresa.com`;

-- Controle de acesso em schema
GRANT SELECT ON ALL TABLES IN SCHEMA marketing.vendas TO `grupo_marketing`; 