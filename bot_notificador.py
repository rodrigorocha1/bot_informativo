from time import sleep
from typing import List, TypeVar, Generic
from utlis.pacote_log import logger
from src.core.isujeito import ISujeito
from src.core.sujeito_concreto import SujeitoConcreto
from src.obsevardores.iobservador import IObservador
from src.obsevardores.observador_email import ObservadorGmailEmail
from src.obsevardores.observador_telegram import ObservadorTelegram
from src.servico_web_scraping.i_web_scraping import IWebScraping
from src.servico_web_scraping.webscrapingbs4 import WebScrapingBs4

T = TypeVar('T')


class NotificadorBot(Generic[T]):

    def __init__(
            self,
            sujeito: ISujeito,
            observadores: List[IObservador],
            servico_web_scraping: IWebScraping[T]
    ):
        self.__sujeito = sujeito
        self.__observadores = observadores
        self.__servico_web_scraping = servico_web_scraping

    def executar_bot(self):
        [self.__sujeito.anexar(observador) for observador in self.__observadores]
        dado = self.__servico_web_scraping.conectar_site()
        for texto in self.__servico_web_scraping.obter_dados(dados=dado):

            self.__sujeito.notificar(dado=texto)
            sleep(2)
            if texto is None:
                logger.info('SEM NOTICIA COLETADA ENCERRANDO')
                break


if __name__ == '__main__':
    logger.info('Iniciando bot')
    sujeito = SujeitoConcreto()
    observador_telegram = ObservadorTelegram()
    observador_email = ObservadorGmailEmail(assunto='Sem noticia')
    lista_observadores = [
        observador_telegram,
        observador_email
    ]
    notificador_bot = NotificadorBot(
        sujeito=sujeito,
        observadores=lista_observadores,
        servico_web_scraping=WebScrapingBs4()
    )
    notificador_bot.executar_bot()
    logger.info('Encerrando execução bot')
