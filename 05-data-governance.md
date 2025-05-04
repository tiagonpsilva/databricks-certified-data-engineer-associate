# 🛡️ 5. Governança de Dados

## 5.1 Áreas de Governança de Dados

A governança de dados é um conjunto de práticas e políticas que garantem a segurança, privacidade, qualidade e conformidade dos dados em uma organização. No Databricks, isso inclui controle de acesso, rastreabilidade, segregação de ambientes e uso de catálogos/metastores para garantir que apenas pessoas autorizadas possam acessar, modificar ou compartilhar dados sensíveis.

Exemplo:
- Controle de acesso por usuário, grupo e service principal.

## 5.2 Metastores e Catálogos

O **Metastore** armazena metadados de tabelas, views e permissões, funcionando como um "catálogo central" de informações sobre os dados. O **Catálogo** é uma camada lógica para organizar schemas e tabelas, especialmente com o Unity Catalog, permitindo separar ambientes e domínios de negócio.

```
┌────────────┐
│ Metastore  │
└─────┬──────┘
      |
┌─────▼──────┐
│ Catálogo   │
└─────┬──────┘
      |
┌─────▼──────┐
│  Schema    │
└─────┬──────┘
      |
┌─────▼──────┐
│  Tabela    │
└────────────┘
```

Exemplo:
```sql
CREATE CATALOG vendas;
CREATE SCHEMA vendas.marketing;
CREATE TABLE vendas.marketing.campanhas (...);
```

## 5.3 Unity Catalog e Securables

O Unity Catalog traz uma governança centralizada e granular para o Databricks, permitindo definir permissões em diferentes níveis (catálogo, schema, tabela, view). Os **securables** são os objetos protegidos por permissões. O uso de service principals permite automação e integrações seguras. Os clusters podem operar em diferentes modos de segurança (single user, shared, no isolation), e o namespace de três camadas (catalog.schema.tabela) facilita a organização.

Exemplo:
```sql
GRANT SELECT ON TABLE vendas.marketing.campanhas TO `analista@empresa.com`;
```

## 5.4 Controle de Acesso e Boas Práticas

O controle de acesso é feito via comandos GRANT/REVOKE, garantindo que apenas usuários ou grupos autorizados possam acessar determinados dados. É recomendável manter metastores próximos ao workspace para performance e segurança, usar service principals para automação e segregar unidades de negócio por catálogo para facilitar governança e compliance.

Exemplo:
```sql
GRANT USAGE ON CATALOG vendas TO `grupo_vendas`;
GRANT SELECT ON ALL TABLES IN SCHEMA vendas.marketing TO `grupo_marketing`;
```
