from typing import List, Dict

from telebot import TeleBot

from src.obsevardores.observador import Observador
from ..config.config import Config


class ObservadorTelegram(Observador):

    def __init__(self):
        self.__TOKEN_TELEGRAM = Config.TOKEN_TELEGRAM
        self.__CHAT_ID = Config.CHAT_ID
        self.__bot = TeleBot(self.__CHAT_ID)

    def atualizar(self, dado: List[Dict]):
        self.__bot.send_message(self.__CHAT_ID, dado, parse_mode="MarkdownV2")
