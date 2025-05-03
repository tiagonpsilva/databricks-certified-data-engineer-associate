# 4. Pipelines de Produção

## 4.1 Benefícios de Múltiplas Tasks em Jobs
Jobs com múltiplas tasks permitem orquestrar pipelines complexos, dividir etapas (ingestão, transformação, carga), facilitar reuso e paralelismo, além de simplificar o monitoramento e a recuperação de falhas.

**Exemplo:**
- Um job com tasks para ingestão de dados, limpeza, agregação e carga em dashboard.

**Exercício:**
- Desenhe um pipeline de produção com pelo menos três tasks encadeadas.

---

## 4.2 Predecessores em Jobs
Tasks predecessoras garantem que uma etapa só inicie após a conclusão (com sucesso) de outra, permitindo dependências explícitas e controle de fluxo.

**Exemplo:**
- Task de agregação só roda após task de limpeza concluir.

**Exercício:**
- Configure um job com uma task predecessora e explique o fluxo de execução.

---

## 4.3 Execução e Monitoramento de Tasks
- O histórico de execução permite auditar execuções passadas, identificar falhas e analisar performance.
- Agendamento pode ser feito via CRON para execuções periódicas (ex: todo dia às 2h).
- Debug de task com falha envolve análise de logs, outputs e dependências.

**Exemplo:**
```python
# Agendamento CRON: todo dia às 2h
schedule = {"quartz_cron_expression": "0 0 2 * * ?"}
```

**Exercício:**
- Programe um job para rodar toda segunda-feira às 8h e simule uma falha para analisar os logs.

---

## 4.4 Políticas de Retry e Alertas
- Políticas de retry permitem reexecutar tasks automaticamente em caso de falha, aumentando a robustez do pipeline.
- Alertas podem ser configurados para notificar por e-mail em caso de falha, facilitando resposta rápida.

**Exemplo:**
- Configuração de retry: até 3 tentativas com intervalo de 10 minutos.
- Alerta por e-mail: notificar equipe de dados em caso de erro crítico.

**Exercício:**
- Configure uma política de retry e um alerta por e-mail para um job crítico. 