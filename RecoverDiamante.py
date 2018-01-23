import re
import requests
import numpy as np
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('products.db')

cursor = conn.cursor()
    
def recoverDiamante(site):
    page = requests.get(site)
    print(site)
    if page.status_code != 200:
        return 
    soup = BeautifulSoup(page.content, 'html.parser')
    products = soup.find_all('div', class_="produto")
    for product in products:
        #print(product)
        product.find('div', class_="box-produtos-nome nomeProduto")
        product.find('div', class_="box-produtos-de valorDesconto")
        #try:
            #div class="box-produtos-nome nomeProduto"
            #title = product.a.get('title')
            #price = re.findall(r'\d+\,?\d*', product.get_text())
            #weight = re.findall(r'\d+', product.a.get('title'))
            #print(title)
            #print(price)
            #print(weight)
            #cursor.execute("""
            #               INSERT INTO Produtos(id_empresa, nome, categoria, preco, peso)
            #               VALUES (1,?,'comida',?,?)
            #               """, (title, price, weight))
        #except AttributeError as e:
            #print("ERROROROO ============================")
    
#Recover Foods Diamante
def recoverFoodDiamente():
    foodsSites = {"https://www.mercadodiamante.com.br/categoria/carnes-carnes-bovinas/53"}#,
                  #"https://www.mercadodiamante.com.br/categoria/-aves/54",
                  #"https://www.mercadodiamante.com.br/categoria/-carnes-suinas/52",
                  #"https://www.mercadodiamante.com.br/categoria/-embutidos-de-carnes/57"}

    for foodsSite in foodsSites:
        recoverDiamante(foodsSite)

#Recover Drinks Diamante
def recoverDrinksDiamante():
    drinksSites = {"https://www.mercadodiamante.com.br/categoria/bebidas-cervejas/1",
                   "https://www.mercadodiamante.com.br/categoria/-aguas/5",
                   "https://www.mercadodiamante.com.br/categoria/-refrigerantes/28",
                   "https://www.mercadodiamante.com.br/categoria/-whisky-amp-destilados/7",
                   "https://www.mercadodiamante.com.br/categoria/-sucos-amp-refrescos/42/suco"}

    for drinksSite in drinksSites:
        recoverDiamante(drinksSite)
        
recoverFoodDiamente() 
#recoverDrinksDiamante() 