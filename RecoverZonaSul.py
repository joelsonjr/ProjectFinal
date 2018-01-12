import re
import requests
import numpy as np
from bs4 import BeautifulSoup

#re_number = re.compile(r"\d*\.?\d+")
#str = "JOELSO  VIALLE 10.4kg"
#print (re_number.match(str))
#print (re.findall(r'\d+\.\d*', str))

def recoverZonaSul(site):
    page = requests.get(site)
    soup = BeautifulSoup(page.content, 'html.parser')
    products = soup.find_all('div', class_="bloco_informacoes")
    print(products[0].find('div', class_='prod_preco_qtd_peso').find('div', class_='prod_preco').find('p', class_='preco').string.strip())
    #for product in products:
        #print (product.find('a')['title'])
        #print(product.find('div', class_='prod_preco_qtd_peso').find('div', class_='prod_preco'))#.find('p', class_='preco').string.strip())
        #print(product.find('div', class_='prod_preco_qtd_peso').find('div', class_='prod_preco').find('p', class_='peso').string.strip())

#Recover Foods ZOna Sul
def recoverFoodZonaSul():
    foodsSites = {"https://www.zonasul.com.br/SubSecao/Bovinas--124",
                  "https://www.zonasul.com.br/SubSecao/Aves--125",
                  "https://www.zonasul.com.br/SubSecao/Exoticas--126",
                  "https://www.zonasul.com.br/SubSecao/Suinas--123"}

    for foodsSite in foodsSites:
        recoverZonaSul(foodsSite)


#Recover Drinks Zona Sul
def recoverDrinksZonaSul():
    drinksSites = {"https://www.zonasul.com.br/SubSecao/Cachacas_e_Vodkas--29",
                   "https://www.zonasul.com.br/SubSecao/Cervejas--25",
                   "https://www.zonasul.com.br/SubSecao/Cervejas_Artesanais--269",
                   "https://www.zonasul.com.br/SubSecao/Vinhos--209",
                   "https://www.zonasul.com.br/SubSecao/Whisky_e_Destilados--28"}

    for drinksSite in drinksSites:
        recoverZonaSul(drinksSite)

recoverFoodZonaSul()