import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    TOKEN_TELEGRAM = os.environ['TOKEN_TELEGRAM']
    CHAT_ID = os.environ['CHAT_ID']
    SENHA_EMAIL = os.environ['SENHA_EMAIL']
    EMAIL_REMENTENTE = os.environ['EMAIL_REMENTENTE']
    EMAIL_DESTINATARIO = os.environ['EMAIL_DESTINATARIO']
    CONF_SMTP = os.environ['CONF_SMTP']
    PORTA_SMTP = os.environ['PORTA_SMTP']
