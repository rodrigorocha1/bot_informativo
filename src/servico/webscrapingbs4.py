from typing import Dict, List

import requests
from bs4 import BeautifulSoup, Tag

from .i_web_scraping import IWebScraping


class WebScrapingBs4(IWebScraping[BeautifulSoup, List[Dict]]):

    def __init__(self):
        self.__url = 'https://aacep.com.br/noticias/'

    def conectar_site(self) -> BeautifulSoup:
        """
        Método para conectar no site
        :return: objeto de conexão
        :rtype: BeautifulSoup
        """
        req = requests.get(self.__url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def obter_dados(self, dados: BeautifulSoup) -> List[Dict]:
        lista_noticias: List[Dict] = []

        noticias = dados.find_all("article", class_="elementor-post")

        for noticia in noticias:
            if not isinstance(noticia, Tag):
                continue

            titulo_tag = noticia.find('h3', class_='elementor-post__title')
            data_tag = noticia.find('span', class_='elementor-post-date')
            resumo_tag = noticia.select_one(".elementor-post__excerpt p")

            if not titulo_tag or not data_tag or not resumo_tag:
                continue

            lista_noticias.append(
                {
                    'texto': titulo_tag.get_text(strip=True),
                    'data': data_tag.get_text(strip=True),
                    'resumo': resumo_tag.get_text(strip=True)
                }
            )

        return lista_noticias