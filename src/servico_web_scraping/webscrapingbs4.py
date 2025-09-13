import locale
from typing import Generator

import requests
from bs4 import BeautifulSoup, Tag

from .web_scraping_base import WebScrapingBase

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')


class WebScrapingBs4(WebScrapingBase[BeautifulSoup]):

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

    def obter_dados(self, dados: BeautifulSoup) -> Generator[str, None, None]:
        """
        Método para obter dados
        :param dados: dados de retorno
        :type dados: BeautifulSoup
        """

        noticias = dados.find_all("article", class_="elementor-post")

        for noticia in noticias:
            if not isinstance(noticia, Tag):
                continue

            titulo_tag = noticia.find('h3', class_='elementor-post__title')
            data_tag = noticia.find('span', class_='elementor-post-date')
            resumo_tag = noticia.select_one(".elementor-post__excerpt p")
            link_tag = noticia.find('a', class_='elementor-post__thumbnail__link')

            href = link_tag.get('href') if isinstance(link_tag, Tag) else None
            link_noticia = href if isinstance(href, str) else None

            if not titulo_tag or not data_tag or not resumo_tag or not link_noticia:
                continue

            texto: str = (
                f"<b>Título:</b> {titulo_tag.get_text(strip=True)}\n"
                f"<b>Data da Noticia:</b> {data_tag.get_text(strip=True)}\n"
                f"<b>Resumo noticia:</b> {resumo_tag.get_text(strip=True)}\n"
                f"<b>Link:</b> {link_noticia}"
            )
            yield texto
