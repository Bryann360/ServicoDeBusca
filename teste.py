import requests
from bs4 import BeautifulSoup
import urllib.request
import random
import os, ssl
import json
import jsonpickle
from json import JSONEncoder
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

i = 1



soup = make_soup('https://busca.magazineluiza.com.br/busca?q=l340')

l = soup.find_all('li', class_="nm-product-item")


url = l[0].a.get('data-product')


urlobj = jsonpickle.decode(url)

print(url)

print(urlobj.get('price'))


#/produto/' + productId  + '/preco.json'

   
