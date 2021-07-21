from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.climatempo.com.br/').content
#Objeto site recebe todo o conteúdo da requisição http do site...

soup = BeautifulSoup(site, 'html.parser')
#Objeto soup baixa o HTML do site

#print(soup.prettify())
#Transforma o HTML em string e o print exibe na tela

titulo = soup.title

print(titulo.string)