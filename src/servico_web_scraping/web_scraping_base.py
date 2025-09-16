from abc import abstractmethod
from typing import TypeVar, Tuple

from src.servico_web_scraping.i_web_scraping import IWebScraping

T = TypeVar("T")


class WebScrapingBase(IWebScraping[T]):

    @abstractmethod
    def conectar_site(self) -> Tuple[T, int] | str:
        pass

    @abstractmethod
    def obter_dados(self, dados: T):
        pass
