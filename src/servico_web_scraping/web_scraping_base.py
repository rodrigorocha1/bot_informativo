from abc import abstractmethod
from typing import TypeVar

from src.servico_web_scraping.i_web_scraping import IWebScraping

T = TypeVar("T")


class WebScrapingBase(IWebScraping[T]):

    @abstractmethod
    def conectar_site(self) -> T:
        pass

    @abstractmethod
    def obter_dados(self, dados: T):
        pass
