from abc import abstractmethod
from typing import TypeVar, Union, Optional

from src.servico_web_scraping.i_web_scraping import IWebScraping

T = TypeVar("T")


class WebScrapingBase(IWebScraping[T]):

    @abstractmethod
    def conectar_site(self) -> T | str:
        pass

    @abstractmethod
    def obter_dados(self, dados: T):
        pass
