# Exemplos Python Extras - Capítulo 4

import logging
from time import sleep

# Configuração de logging
logging.basicConfig(level=logging.INFO)

# Função simulando task com retry
for tentativa in range(3):
    try:
        logging.info(f'Tentativa {tentativa+1}: executando task crítica...')
        # Simule uma falha na primeira tentativa
        if tentativa < 1:
            raise Exception('Falha simulada')
        logging.info('Task executada com sucesso!')
        break
    except Exception as e:
        logging.error(f'Erro: {e}')
        sleep(10)  # Espera 10 segundos antes do retry
else:
    logging.critical('Todas as tentativas falharam! Enviando alerta para equipe de dados.')
    # Aqui você poderia integrar com um sistema de alertas real 