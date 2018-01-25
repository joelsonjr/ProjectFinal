import re
import requests
import numpy as np
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('products.db')

cursor = conn.cursor()
    
def recoverPrix(site):
    page = requests.get(site[0])
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
            cursor.execute("""
                           INSERT INTO Acougue(id_empresa, nome, preco, peso, categoria, especial)
                           VALUES (2,?,?,?,?,?)
                           """, (title, price[0], weight, site[2], site[1]))
        except AttributeError as e:
            print("ERROROROO ============================")
    
#Recover Foods Prix
def recoverFoodPrix():
    foodsSites = {#"https://www.superprix.com.br/carnes-e-pescados/bovinas", 0, "Carnes"),
                  #("https://www.superprix.com.br/carnes-e-pescados/aves", 0, "Aves"),
                  #("https://www.superprix.com.br/carnes-e-pescados/suinas", 0, "Suinas"),
                  ("https://www.superprix.com.br/carnes-e-pescados/linguicas", 0, "Linguicas")}

    for foodsSite in foodsSites:
        recoverPrix(foodsSite)

#Recover Drinks Prix
def recoverDrinksPrix():
    drinksSites = {("https://www.superprix.com.br/bebidas/cervejas/cervejas-especiais", 1, "Cervejas"),
                   ("https://www.superprix.com.br/bebidas/cervejas/cervejas", 0, "Cervejas"),
                   ("https://www.superprix.com.br/bebidas/vinhos", 1, "Vinhos"),
                   ("https://www.superprix.com.br/bebidas/destilados", 1, "Cachaças"),
                   ("https://www.superprix.com.br/bebidas/refrigerantes/refrigerantes", 0, "Refrigerantes"),
                   ("https://www.superprix.com.br/bebidas/sucos-e-refrescos", 1, "Sucos"),
                   ("https://www.superprix.com.br/bebidas/agua", 1, "Aguas"),
                   ("https://www.superprix.com.br/bebidas/isotonicos-e-energeticos", 1, "Energeticos")}

    for drinksSite in drinksSites:
        recoverPrix(drinksSite)
        
#recoverFoodPrix() 
recoverDrinksPrix() 