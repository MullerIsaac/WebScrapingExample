import requests
import csv
from bs4 import BeautifulSoup


f = csv.writer(open('mlproducts.csv', 'w'))
f.writerow(['Title','Price', 'LastPrice','Link'])

page = requests.get('https://www.mercadolivre.com.br/ofertas?container_id=MLB779362-2&page=1')

soup = BeautifulSoup(page.text, 'html.parser')

products_list = soup.find_all(class_='promotion-item')

for products in products_list:
    title = products.find(class_='promotion-item__title').getText()
    preco = products.find_all(class_='andes-money-amount__fraction')
    atual = preco[0].text
    antigo = preco[1].text if len(preco)>1 else " "
    link = products.find('a').get('href')

    f.writerow([title, atual, antigo, link])