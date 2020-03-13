import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com.br/Seagate-STEA1000400-Expans%C3%A3o-Externo-Port%C3%A1til/dp/B00TKFEEAS?ref_=BSellerC&pf_rd_p=69932fd2-df2c-55b9-9028-136c32cfbe36&pf_rd_s=merchandised-search-10&pf_rd_t=101&pf_rd_i=17351089011&pf_rd_m=A1ZZFT5FULY4LN&pf_rd_r=MA31C9SW1X92VGBS74SP&pf_rd_r=MA31C9SW1X92VGBS74SP&pf_rd_p=69932fd2-df2c-55b9-9028-136c32cfbe36'
headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
page = requests.get(url, headers = headers)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find(id = "productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()

print("")
print(title.strip())
print(price.strip())

nw_price = int(price[2:5])

if nw_price < 190:
    print("Good Price!")
else:
    print("Expensive!")