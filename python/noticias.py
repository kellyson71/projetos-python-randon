import requests
from bs4 import BeautifulSoup

def obter_noticias(url):
    resposta = requests.get(url)
    soup = BeautifulSoup(resposta.text, 'html.parser')
    manchetes = soup.find_all('h2')

    for manchete in manchetes:
        print(manchete.text)

url_noticias = "https://www.exemplo.com/noticias"
obter_noticias(url_noticias)
