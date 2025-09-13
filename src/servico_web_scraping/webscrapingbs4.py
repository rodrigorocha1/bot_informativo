import locale
from datetime import datetime
from typing import Dict, List

import requests
from bs4 import BeautifulSoup, Tag

from .web_scraping_base import WebScrapingBase

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')


class WebScrapingBs4(WebScrapingBase[BeautifulSoup, List[Dict]]):

    def __init__(self):
        super().__init__()
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
        """
        Método para obter dados
        :param dados: dados de retorno
        :type dados: BeautifulSoup
        :return: Lista com as noticias
        :rtype: List[Dict]
        """
        lista_noticias: List[Dict] = []

        noticias = dados.find_all("article", class_="elementor-post")

        for noticia in noticias:
            if not isinstance(noticia, Tag):
                continue

            titulo_tag = noticia.find('h3', class_='elementor-post__title')
            data_tag = noticia.find('span', class_='elementor-post-date')
            resumo_tag = noticia.select_one(".elementor-post__excerpt p")
            link_noticia = noticia.find('a', class_='elementor-post__thumbnail__link').get('href')

            if not titulo_tag or not data_tag or not resumo_tag:
                continue

            lista_noticias.append(
                {
                    'texto': titulo_tag.get_text(strip=True),
                    'data': datetime.strptime(data_tag.get_text(strip=True), "%d de %B de %Y").date(),
                    'resumo': resumo_tag.get_text(strip=True),
                    'link_noticia': link_noticia
                }
            )
        self.notificar(dado=lista_noticias)
        return lista_noticias
