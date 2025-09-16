from datetime import datetime, timedelta
from typing import Generator, Optional, Union

import dateparser
import requests
from bs4 import BeautifulSoup, Tag, FeatureNotFound
from requests import RequestException

from .web_scraping_base import WebScrapingBase


class WebScrapingBs4(WebScrapingBase[BeautifulSoup]):

    def __init__(self):
        super().__init__()
        self.__url = 'https://aacep.com.br/noticias/'
        self.__data_atual = datetime.now().date()
        self.__intervalo_dias = 1

    def conectar_site(self) -> BeautifulSoup | str:
        """
        Método para conectar no site
        :return: objeto de conexão
        :rtype:  BeautifulSoup | str
        """
        try:
            req = requests.get(self.__url)
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
            return soup
        except FeatureNotFound as e:
            return f'parse de html: {str(e)}'
        except RequestException as m:
            return f'Erro de Requisição {str(m)}'
        except Exception as e:
            return f'Erro inesperado: {str(e)}'

    def obter_dados(self, dados: BeautifulSoup) -> Generator[Optional[str], None, None]:
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
            data_str = data_tag.get_text(strip=True)
            data_basedt:  datetime | None = dateparser.parse(data_str, languages=['pt'])
            if data_basedt is None:
                continue

            data_base = data_basedt.date()


            if (self.__data_atual - timedelta(days=self.__intervalo_dias)) <= data_base <= self.__data_atual:
                texto: str = (
                    f"<b>Título:</b> {titulo_tag.get_text(strip=True)}\n"
                    f"<b>Data da Noticia:</b> {data_tag.get_text(strip=True)}\n"
                    f"<b>Resumo noticia:</b> {resumo_tag.get_text(strip=True)}\n"
                    f"<b>Link:</b> {link_noticia}"
                )
                yield texto
            yield None
