# ❓ 6. Questões de Exemplo e Gabarito

Estas questões são retiradas de versões anteriores do exame e servem para ilustrar os objetivos do exame e o tipo de pergunta que pode ser cobrada.

---

## Questão 1
**Objetivo:** Descrever os benefícios de um data lakehouse sobre um data warehouse tradicional.

O que é um benefício de um data lakehouse que não está disponível em um data warehouse tradicional?

A. Um data lakehouse fornece um sistema relacional de gerenciamento de dados.
B. Um data lakehouse captura snapshots de dados para controle de versão.
C. Um data lakehouse acopla armazenamento e processamento para controle total.
D. Um data lakehouse utiliza formatos proprietários de armazenamento de dados.
E. Um data lakehouse permite análises batch e streaming.

**Comentário:**
- Resposta correta: **E**. O lakehouse permite análises batch e streaming sobre os mesmos dados, algo que o data warehouse tradicional não faz nativamente.

---

## Questão 2
**Objetivo:** Identificar técnicas de otimização de queries

Uma equipe de engenharia de dados precisa consultar uma tabela Delta para extrair linhas que atendam a uma mesma condição. No entanto, a query está lenta. O tamanho dos arquivos já foi ajustado. Ao investigar, a equipe percebeu que as linhas que atendem à condição estão espalhadas nos arquivos.

Quais técnicas de otimização poderiam acelerar a query?

A. Data skipping
B. Z-Ordering
C. Bin-packing
D. Escrever como arquivo Parquet
E. Ajustar o tamanho dos arquivos

**Comentário:**
- Resposta correta: **B**. O Z-Ordering reorganiza os dados para que linhas com valores semelhantes fiquem próximas, acelerando queries com filtros.

---

## Questão 3
**Objetivo:** Identificar workloads que utilizam tabelas Silver como fonte

Qual workload utilizará uma tabela Silver como fonte?

A. Um job que enriquece dados parseando timestamps para formato legível
B. Um job que consulta dados agregados que já alimentam um dashboard
C. Um job que ingere dados brutos de uma fonte de streaming no Lakehouse
D. Um job que agrega dados limpos para criar estatísticas resumidas
E. Um job que limpa dados removendo registros malformados

**Comentário:**
- Resposta correta: **D**. Tabelas Silver contêm dados limpos e prontos para agregações e análises.

---

## Questão 4
**Objetivo:** Descrever como configurar um agendamento de atualização

Um gerente de engenharia usa uma query SQL no Databricks para monitorar o progresso da equipe em correções de bugs. Ele checa o resultado todo dia, mas está rodando a query manualmente.

Como a query deve ser agendada para garantir atualização diária dos resultados?

A. Atualizar a cada 12h na página da query no Databricks SQL.
B. Atualizar a cada 1 dia na página da query no Databricks SQL.
C. Rodar a cada 12h pela interface de Jobs.
D. Atualizar a cada 1 dia na página do SQL warehouse no Databricks SQL.
E. Atualizar a cada 12h na página do SQL warehouse no Databricks SQL.

**Comentário:**
- Resposta correta: **B**. O agendamento diário deve ser feito na própria página da query no Databricks SQL.

---

## Questão 5
**Objetivo:** Identificar comandos para conceder permissões

Um novo engenheiro de dados foi adicionado ao workspace da empresa como new.engineer@company.com. Ele precisa consultar a tabela sales no banco retail. Já possui USAGE no banco retail.

Qual comando deve ser usado para conceder a permissão correta?

A. GRANT USAGE ON TABLE sales TO new.engineer@company.com;
B. GRANT CREATE ON TABLE sales TO new.engineer@company.com;
C. GRANT SELECT ON TABLE sales TO new.engineer@company.com;
D. GRANT USAGE ON TABLE new.engineer@company.com TO sales;
E. GRANT SELECT ON TABLE new.engineer@company.com TO sales;

**Comentário:**
- Resposta correta: **C**. Para consultar uma tabela, é necessário o privilégio SELECT.

---

## Gabarito
- Questão 1: E
- Questão 2: B
- Questão 3: D
- Questão 4: B
- Questão 5: C

---

## Exercícios Extras de Simulado

1. Explique a diferença entre uma tabela Delta gerenciada e uma tabela Delta externa.
2. Dê um exemplo de uso do comando MERGE para deduplicação de dados.
3. Como garantir que apenas usuários autorizados possam acessar dados sensíveis em um catálogo?
4. Crie uma query SQL para contar o número de clientes únicos por estado em uma tabela de vendas.
5. Descreva um cenário em que o uso de Auto Loader é mais vantajoso que COPY INTO. 