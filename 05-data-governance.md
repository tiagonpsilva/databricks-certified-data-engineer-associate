# 🛡️ 5. Governança de Dados

## 5.1 Áreas de Governança de Dados
A governança de dados abrange segurança, privacidade, qualidade e conformidade. No Databricks, isso inclui controle de acesso, rastreabilidade, segregação de ambientes e uso de catálogos/metastores.

**Exemplo:**
- Controle de acesso por usuário, grupo e service principal.

**Exercício:**
- Liste as quatro áreas principais de governança de dados e dê um exemplo prático para cada uma.

---

## 5.2 Metastores e Catálogos
- **Metastore:** armazena metadados de tabelas, views e permissões.
- **Catálogo:** camada lógica para organizar schemas e tabelas, especialmente com Unity Catalog.
- Metastore pode ser compartilhado entre workspaces; catálogos permitem segregação por domínio de negócio.

**Exemplo:**
```sql
CREATE CATALOG vendas;
CREATE SCHEMA vendas.marketing;
CREATE TABLE vendas.marketing.campanhas (...);
```

**Exercício:**
- Explique a diferença entre metastore e catálogo no contexto do Unity Catalog.

---

## 5.3 Unity Catalog e Securables
- **Securables:** objetos protegidos por permissões (catálogos, schemas, tabelas, views).
- **Service principal:** identidade para automação e integrações.
- Modos de segurança de cluster: single user, shared, no isolation.
- Criação de cluster all-purpose habilitado para UC e DBSQL warehouse.
- Namespace de três camadas: catalog.schema.tabela

**Exemplo:**
```sql
GRANT SELECT ON TABLE vendas.marketing.campanhas TO `analista@empresa.com`;
```

**Exercício:**
- Crie um cluster all-purpose habilitado para Unity Catalog e conceda permissão de leitura a um grupo.

---

## 5.4 Controle de Acesso e Boas Práticas
- Implemente controle de acesso a objetos de dados via GRANT/REVOKE.
- Coloque metastores junto ao workspace para performance e segurança.
- Use service principals para conexões automatizadas.
- Segregue unidades de negócio por catálogo para governança e compliance.

**Exemplo:**
```sql
GRANT USAGE ON CATALOG vendas TO `grupo_vendas`;
GRANT SELECT ON ALL TABLES IN SCHEMA vendas.marketing TO `grupo_marketing`;
```

**Exercício:**
- Liste três boas práticas de governança de dados ao estruturar um ambiente Databricks corporativo. 

```
[Metastore]
    |
    v
[Catálogo] -> [Schema] -> [Tabela]
``` 