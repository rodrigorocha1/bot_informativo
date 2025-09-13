import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    TOKEN_TELEGRAM = os.environ['TOKEN_TELEGRAM']
    CHAT_ID = os.environ['CHAT_ID']
