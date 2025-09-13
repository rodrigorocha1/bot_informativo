import logging

# Configura o logger
logger = logging.getLogger("meu_logger")
logger.setLevel(logging.INFO)

# Handler para exibir no console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formato das mensagens
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Adiciona handler ao logger
logger.addHandler(console_handler)