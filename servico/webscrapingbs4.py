from .i_web_scraping import IWebScraping
from bs4 import BeautifulSoup
from typing import Dict


class WebScrapingBs4(IWebScraping[BeautifulSoup, Dict]):

    def __init__(self):
        pass

    def conectar_site(self) -> BeautifulSoup:
        pass

    def obter_dados(self, dados: BeautifulSoup) -> Dict:
        pass
