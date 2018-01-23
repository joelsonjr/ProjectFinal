import re
import requests
import numpy as np
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('products.db')

cursor = conn.cursor()
    
def recoverPrix(site):
    page = requests.get(site)
    if page.status_code != 200:
        return 
    soup = BeautifulSoup(page.content, 'html.parser')
    
    products = soup.find_all('div', class_="price")
    for product in products:
        try:
            title = product.a.get('title')
            price = re.findall(r'\d+\,?\d*', product.get_text())
            weight = re.findall(r'\d+', product.a.get('title'))
            print(title)
            print(price)
            print(weight)
            #cursor.execute("""
            #               INSERT INTO Produtos(id_empresa, nome, categoria, preco, peso)
            #               VALUES (1,?,'comida',?,?)
            #               """, (title, price, weight))
        except AttributeError as e:
            print("ERROROROO ============================")
    
#Recover Foods Prix
def recoverFoodPrix():
    foodsSites = {#"https://www.superprix.com.br/carnes-e-pescados/bovinas",
                  #"https://www.superprix.com.br/carnes-e-pescados/aves",
                  #"https://www.superprix.com.br/carnes-e-pescados/suinas",
                  "https://www.superprix.com.br/carnes-e-pescados/linguicas"}

    for foodsSite in foodsSites:
        recoverPrix(foodsSite)

#Recover Drinks Prix
def recoverDrinksPrix():
    drinksSites = {"https://www.superprix.com.br/bebidas/cervejas/cervejas-especiais",
                   "https://www.superprix.com.br/bebidas/cervejas/cervejas",
                   "https://www.superprix.com.br/bebidas/vinhos",
                   "https://www.superprix.com.br/bebidas/destilados",
                   "https://www.superprix.com.br/bebidas/refrigerantes/refrigerantes",
                   "https://www.superprix.com.br/bebidas/sucos-e-refrescos",
                   "https://www.superprix.com.br/bebidas/agua",
                   "https://www.superprix.com.br/bebidas/isotonicos-e-energeticos"}

    for drinksSite in drinksSites:
        recoverPrix(drinksSite)
        
#recoverFoodPrix() 
recoverDrinksPrix() 