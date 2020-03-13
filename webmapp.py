import requests
import webbrowser
import time
from bs4 import BeautifulSoup

url = 'https://www.amazon.com.br/s?k=notebook&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1XGE2FMTGB3TO&sprefix=note%2Caps%2C258&ref=nb_sb_ss_i_3_4'
headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
chromedir= 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' # Google Chrome Dir
pagina = requests.get(url, headers = headers)
soup = BeautifulSoup(pagina.content, 'html.parser') 
notebook_price = soup.find_all('span',class_ = 'a-price-whole') # Find all notebook prices  in Amazon Link and put in a list
maximum_spend = float(input("How much do you want to spend on a new notebook?:  ")) / 1000 
notebook_1 = notebook_price[2].get_text() # Get a element from the list and only take the text
notebook_2 = notebook_price[7].get_text()
notebook_3 = notebook_price[6].get_text()
notebook_1_new_price = float(notebook_1[0:5]) #remove a "," and convert to a float number
notebook_2_new_price = float(notebook_2[0:5])
notebook_3_new_price = float(notebook_3[0:5])
notebook_list = [notebook_1_new_price, notebook_2_new_price, notebook_3_new_price] # Put all elementes on a list to find the min()

if notebook_1_new_price and notebook_2_new_price and notebook_3_new_price < maximum_spend:
    print(f'We have option for you starting on! R$: {min(notebook_list)} ')
    time.sleep(3)  # wait 3 seconds
    webbrowser.get(chromedir).open("encurtador.com.br/cdgW9") # Shorter Link
else:
    print('We dont have nothing for your budget!')
