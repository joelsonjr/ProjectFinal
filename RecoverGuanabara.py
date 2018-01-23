import re
import requests
import numpy as np
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('products.db')

cursor = conn.cursor()

def recoverGuanabara(site):
    page = requests.get(site)
    soup = BeautifulSoup(page.content, 'html.parser')
    products = soup.find('div', class_="products-list").find_all('div', class_="row")
    for product in products:
        try:
            title = product.find('div', class_="name").string.strip()
            price = product.find('span', class_="number").string.strip()
            weight = re.findall(r'(\d+g|\d+kg|\d+\,?\d*kg|\d+ml|\d+L)', title)
            print(title)
            print(price)
            print(weight)
            #cursor.execute("""
            #               INSERT INTO Produtos(id_empresa, nome, categoria, preco, peso)
            #               VALUES (3,?,'comida',?,?)
            #               """, (title, price, weight))
        except AttributeError as e:
            print("ERROROROO ============================")
            
    
#Recover Foods Guanabara
def recoverFoodGuanabara():
    foodsSites = {"https://www.supermercadosguanabara.com.br/produtos/42"}

    for foodsSite in foodsSites:
        recoverGuanabara(foodsSite)


#Recover Drinks Guanabara
def recoverDrinksGuanabara():
    drinksSites = {"https://www.supermercadosguanabara.com.br/produtos/82"}
 
    for drinksSite in drinksSites:
        recoverGuanabara(drinksSite)

#recoverFoodGuanabara()

recoverDrinksGuanabara()