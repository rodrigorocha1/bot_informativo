from src.servico_web_scraping.webscrapingbs4 import WebScrapingBs4

wsbs4 = WebScrapingBs4()
dados = wsbs4.conectar_site()
print(wsbs4.obter_dados(dados=dados))
