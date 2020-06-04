import requests
from bs4 import BeautifulSoup
import urllib.request
import random


def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

i = 1

soup = make_soup('https://busca.magazineluiza.com.br/busca?q=l340')

for img in soup.find_all('img', class_ = "nm-product-img"):
            temp = img.get('src')
print(temp)  
         


   
