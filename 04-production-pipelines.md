# 🏭 4. Pipelines de Produção

## 4.1 Benefícios de Múltiplas Tasks em Jobs

Jobs com múltiplas tasks permitem orquestrar pipelines complexos, dividir etapas (ingestão, transformação, carga), facilitar reuso e paralelismo, além de simplificar o monitoramento e a recuperação de falhas. Isso torna o pipeline mais modular, escalável e resiliente a falhas.

```
┌──────────┐   ┌──────────┐   ┌────────────┐   ┌──────────────┐
│Ingestão  │-->| Limpeza  │-->| Agregação  │-->| Dashboard/BI │
└──────────┘   └──────────┘   └────────────┘   └──────────────┘
```

Exemplo:
- Um job com tasks para ingestão de dados, limpeza, agregação e carga em dashboard.

## 4.2 Predecessores em Jobs

Tasks predecessoras garantem que uma etapa só inicie após a conclusão (com sucesso) de outra, permitindo dependências explícitas e controle de fluxo. Isso evita que etapas críticas sejam executadas fora de ordem e facilita o troubleshooting.

```
┌───────┐   ┌───────┐   ┌───────┐
│Task 1 │-->|Task 2 │-->|Task 3 │
└───────┘   └───────┘   └───────┘
```

Exemplo:
- Task de agregação só roda após task de limpeza concluir.

## 4.3 Execução e Monitoramento de Tasks

O histórico de execução permite auditar execuções passadas, identificar falhas e analisar performance. O agendamento pode ser feito via CRON para execuções periódicas (ex: todo dia às 2h). O debug de task com falha envolve análise de logs, outputs e dependências, facilitando a identificação da causa raiz.

Exemplo:
```python
# Agendamento CRON: todo dia às 2h
schedule = {"quartz_cron_expression": "0 0 2 * * ?"}
```

## 4.4 Políticas de Retry e Alertas

Políticas de retry permitem reexecutar tasks automaticamente em caso de falha, aumentando a robustez do pipeline. Alertas podem ser configurados para notificar por e-mail ou outros canais em caso de falha, facilitando resposta rápida e proativa da equipe.

```
┌────────────┐
│Task Falhou │
└─────┬──────┘
      |
  ┌───▼───┐
  │Retry 1│
  └───┬───┘
      |
  ┌───▼───┐
  │Retry 2│
  └───┬───┘
      |
┌─────▼─────┐
│Alerta/E-mail│
└────────────┘
```

Exemplo:
- Configuração de retry: até 3 tentativas com intervalo de 10 minutos.
- Alerta por e-mail: notificar equipe de dados em caso de erro crítico.

**Exercício:**
- Configure uma política de retry e um alerta por e-mail para um job crítico. 