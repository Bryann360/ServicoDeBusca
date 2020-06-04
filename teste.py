import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import random



page_url = "https://busca.magazineluiza.com.br/busca?q=l340"

uClient = uReq(page_url)

page_soup = soup(uClient.read(), "html.parser")
uClient.close()
price = 'Erro'


for container in soup.find_all('nm-offer'):

    price = container.div.select("nm-price-container").text
    if price[:1] == "/":
        
   
   
    

        
print(price)
