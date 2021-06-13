import requests
from bs4 import BeautifulSoup

#definição da fonte base (que usaremos para navegar pelas páginas)
source_0 = "http://www.ans.gov.br"
#definição da fonte inicial
source_1 = "http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar"

#pegamos o HTML da página que usaremos e definimos o objeto site no qual trabalharemos
site = BeautifulSoup(requests.get(source_1).text, "lxml")
#definimos uma lista para os links que usaremos para navegar
href_s = []
#buscamos pelos links da primeira página e guardamos todos em uma lista
pag_1 = site.find_all("a", class_="alert-link")
for pag in pag_1:
    href_s.append(pag.get("href"))

#escolhemos o primeiro link da página e atribuimos à source_2
source_2 = source_0 + href_s[0] # automatizar DEPOIS a aquisição desse link

#pegamos o HTML da página que usaremos e definimos o objeto site no qual trabalharemos
site = BeautifulSoup(requests.get(source_2).text, "lxml")
#Limpamos a lista para os links que usaremos para navegar
href_s.clear
#buscamos pelos links da segunda página e guardamos todos em uma lista
pag_2 = site.find_all("a", class_="btn btn-primary btn-sm center-block")
for pag in pag_2:
    href_s.append(pag.get("href"))
    
#escolhemos o primeiro link da página e atribuimos à source_3
source_3 = source_0 +href_s[5] # automatizar DEPOIS a aquisição desse link

with open('/home/matheus/Documentos/python-projects/first-tests/Padrão_TISS_Componente_Organizacional_202103.pdf', 'wb') as f:
    f.write(requests.get(source_3).content)
f.close()
