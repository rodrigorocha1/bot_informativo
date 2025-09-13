from src.servico_web_scraping.webscrapingbs4 import WebScrapingBs4
from src.obsevardores.observador_telegram import ObservadorTelegram

wsbs4 = WebScrapingBs4()
dados = wsbs4.conectar_site()

mensageiro_telegram = ObservadorTelegram()

for dado in wsbs4.obter_dados(dados=dados):
    texto = (
        f'Título: {dado["titulo"]}\n'
        f'Data: {dado["data"]}\n'
        f'Resumo:{dado["resumo"]}\n'
        f'Link Noticia{dado["link_noticia"]}'
    )

    print(texto)
    print('===' * 30)
