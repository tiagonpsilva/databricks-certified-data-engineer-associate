-- Exemplos SQL Extras - Capítulo 5

-- Revogar permissão de acesso
REVOKE SELECT ON TABLE marketing.vendas.campanhas FROM `usuario@empresa.com`;

-- Adicionar comentário em tabela
COMMENT ON TABLE marketing.vendas.campanhas IS 'Tabela de campanhas de marketing';

-- Listar permissões de um usuário
SHOW GRANTS TO USER `analista@empresa.com`;

-- Exemplo de segregação por catálogo
CREATE CATALOG financeiro;
CREATE SCHEMA financeiro.contabilidade; 