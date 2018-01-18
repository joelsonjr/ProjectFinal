import re
import requests
import numpy as np
from bs4 import BeautifulSoup

def recoverGuanabara(site):
    page = requests.get(site)
    soup = BeautifulSoup(page.content, 'html.parser')
    products = soup.find('div', class_="products-list").find_all('div', class_="row")
    for product in products:
        try:
            print(product.find('div', class_="name").string.strip())
            print(product.find('span', class_="number").string.strip())
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

recoverDrinksGuanabara()