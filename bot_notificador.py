from typing import TypeVar, Generic

from src.servico_web_scraping.i_web_scraping import IWebScraping
from src.servico_web_scraping.webscrapingbs4 import WebScrapingBs4
from src.obsevardores.observador_telegram import ObservadorTelegram

T = TypeVar("T")


class NotificadorBot(Generic[T]):

    def __init__(self, servico_web_scraping: IWebScraping[T]):
        self.__servico_web_scraping = servico_web_scraping

    def executar(self) -> None:
        dados = self.__servico_web_scraping.conectar_site()
        self.__servico_web_scraping.obter_dados(dados=dados)


wsbs4 = WebScrapingBs4()
wsbs4.anexar(observador=ObservadorTelegram())

notificador = NotificadorBot(wsbs4)
notificador.executar()
