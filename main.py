from bs4 import BeautifulSoup
import requests

url = 'https://aacep.com.br/noticias/'
req = requests.get(url=url)

html = req.text

soup = BeautifulSoup(html, "html.parser")

# Pega todos os títulos das manchetes
noticias = soup.find_all("article", class_="elementor-post")
print(noticias[2].find('h3', class_='elementor-post__title').get_text(strip=True))

print("noticia")
print(len(noticias))
for t in noticias:
    print('=' * 200)
    texto = t.find('h3', class_='elementor-post__title').get_text(strip=True)
    data = t.find('span', class_='elementor-post-date').get_text(strip=True)
    resumo = t.select_one(".elementor-post__excerpt p").get_text(strip=True)
    print(texto)
    print(data)
    print(resumo)
    print('=' * 200)
