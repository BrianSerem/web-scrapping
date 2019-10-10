import bs4
import os
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

watches_url = os.environ.get('URL')
filename = 'watches.csv'
f = open(filename, 'w')

headers = 'brand, description, price\n'
f.write(headers)

uClient = uReq(watches_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')

containers = page_soup.find_all('div', {'class':'s-item-container'})

brands = []

for container in containers:
    
    brand = container.find('span',{'class':'a-color-secondary s-overflow-ellipsis s-size-mild'})
    description = container.find('h2',{'class':'a-size-small a-color-base s-inline s-access-title a-text-normal'})
    price = container.find('span',{'class':'sx-price-whole'})
    
    if brand and description and price:
        print(brand.text)
        print(description.text)
        print(price.text.replace(",",""))
        f.write(brand.text + "," +description.text + "," +price.text.replace(",","")+"\n")
