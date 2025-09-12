from abc import abstractmethod
from typing import TypeVar

from src.core.sujeito import Sujeito
from src.servico_web_scraping.i_web_scraping import IWebScraping

T = TypeVar("T")  # Tipo do objeto retornado por conectar_site
R = TypeVar("R")  # Tipo do resultado final (ex: Dict[str, Any])


class WebScrapingBase(IWebScraping[T, R], Sujeito):
    @abstractmethod
    def conectar_site(self) -> T:
        pass

    @abstractmethod
    def obter_dados(self, dados: T) -> R:
        pass
