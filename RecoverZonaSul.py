import re
import requests
import numpy as np
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('products.db')

cursor = conn.cursor()

def recoverZonaSulFood(site):
    cursor.execute("""
                   delete from Acougue where id_empresa = 1;
                   """)
    page = requests.get(site[0])
    soup = BeautifulSoup(page.content, 'html.parser')
    products = soup.find_all('div', class_="bloco_informacoes")
    for product in products:
        try:
            title = product.find('a')['title']
            price = product.find('div', class_="prod_preco_qtd_peso").find('div', class_="prod_preco").find('p', class_="preco").string.strip()
            weight = product.find('div', class_="prod_preco_qtd_peso").find('div', class_="prod_preco").find('p', class_="peso").string.strip()
            cursor.execute("""
                           INSERT INTO Acougue(id_empresa, nome, preco, peso, categoria, especial)
                           VALUES (1,?,?,?,?,?)
                           """, (title, price, weight, site[2], site[1]))
        except AttributeError as e:
            continue
            

def recoverZonaSulDrink(site):
    print(site[0])
    print(site[1])
    print(site[2])
    cursor.execute("delete from Bebidas where id_empresa = 1;")
    page = requests.get(site[0])
    soup = BeautifulSoup(page.content, 'html.parser')
    products = soup.find_all('div', class_="bloco_informacoes")
    for product in products:
        try:
            title = product.find('a')['title']
            price = re.findall(r'\d+\,?\d*',product.find('div', class_="prod_preco_qtd").find('div', class_="prod_preco").find('p', class_="preco").string.strip())
            w = re.findall(r'\d+', title)
            weight = w[len(w) - 1]
            cursor.execute("""
                           INSERT INTO Bebidas(id_empresa, nome, preco, peso, categoria, especial)
                           VALUES (1,?,?,?,?,?)
                           """, (title, price, weight, site[2], site[1]))
        except AttributeError as e:
            continue

#Recuperando itens de açougue do supermercado Zona Sul
def recoverFoodZonaSul():
    foodsSites = {"https://www.zonasul.com.br/SubSecao/Bovinas--124",
                  "https://www.zonasul.com.br/SubSecao/Aves--125",
                  "https://www.zonasul.com.br/SubSecao/Salsichas_e_Linguicas--128",
                  "https://www.zonasul.com.br/SubSecao/Suinas--123"}
    for foodsSite in foodsSites:
        recoverZonaSulFood(foodsSite, 0)
        page = requests.get(foodsSite)
        soup = BeautifulSoup(page.content, 'html.parser')
        try:
            pages = soup.find('div', class_="paginas").find('span', id="ctl00_cphMasterPage1_dpgPromocaoTopo").find_all('a', class_='num')
            for page in pages:
                p = foodsSite + "?Pagina=" + page.get_text()
                recoverZonaSulFood(p, 0)
        except AttributeError as e:
            ""
            
#Recuperando itens Especiais de açougue do supermercado Zona Sul
def recoverSpecialFoodZonaSul():
    foodsSites = {"https://www.zonasul.com.br/SubSecao/Exoticas--126",
                  "https://www.zonasul.com.br/SubSecao/Racas_Britanicas--311"}
    for foodsSite in foodsSites:
        recoverZonaSulFood(foodsSite, 1)
        page = requests.get(foodsSite)
        soup = BeautifulSoup(page.content, 'html.parser')
        try:
            pages = soup.find('div', class_="paginas").find('span', id="ctl00_cphMasterPage1_dpgPromocaoTopo").find_all('a', class_='num')
            for page in pages:
                p = foodsSite + "?Pagina=" + page.get_text()
                recoverZonaSulFood(p, 1)
        except AttributeError as e:
            ""


#Recupoerando Bebidas do supermercado Zona Sul
def recoverDrinksZonaSul():
    drinksSites = {("https://www.zonasul.com.br/SubSecao/Aguas--18", 0, "Aguas"),
                   "https://www.zonasul.com.br/SubSecao/Refrigerantes--19", 0, "Refrigerantes"),
                   "https://www.zonasul.com.br/SubSecao/Chas_Mate_e_Guarana--20", 0, "Refrigerantes"),
                   "https://www.zonasul.com.br/SubSecao/Sucos_e_Refrescos--21", 0, "Sucos"),
                   "https://www.zonasul.com.br/SubSecao/Cervejas--25", 0, "Cervejas")}
    for drinksSite in drinksSites:
        recoverZonaSulDrink(drinksSite, 0)
        page = requests.get(drinksSite)
        soup = BeautifulSoup(page.content, 'html.parser')
        try:
            pages = soup.find('div', class_="paginas").find('span', id="ctl00_cphMasterPage1_dpgPromocaoTopo").find_all('a', class_='num')
            for page in pages:
                p = drinksSite + "?Pagina=" + page.get_text()
                recoverZonaSulDrink(p, 0)
        except AttributeError as e:
            ""

#Recupoerando Bebidas Importadas do supermercado Zona Sul
def recoverSpecialDrinksZonaSul():
    drinksSites = {("https://www.zonasul.com.br/SubSecao/Cachacas_e_Vodkas--29", 1, "Vodkas")}#,
                   #"https://www.zonasul.com.br/SubSecao/Cervejas_Artesanais--269", 1, "Cervejas Artesanais"),
                   #"https://www.zonasul.com.br/SubSecao/Vinhos--209", 1, "Vinhos"),
                   #"https://www.zonasul.com.br/SubSecao/Whisky_e_Destilados--28", 1, "Whisky")}
    for drinksSite in drinksSites:
        recoverZonaSulDrink(drinksSite)
        '''
        page = requests.get(drinksSite)
        soup = BeautifulSoup(page.content, 'html.parser')
        try:
            pages = soup.find('div', class_="paginas").find('span', id="ctl00_cphMasterPage1_dpgPromocaoTopo").find_all('a', class_='num')
            for page in pages:
                p = drinksSite + "?Pagina=" + page.get_text()
                recoverZonaSulDrink(p, 1)
        except AttributeError as e:
            ""
        '''
            
#recoverFoodZonaSul()
#recoverSpecialFoodZonaSul()
#recoverDrinksZonaSul()
recoverSpecialDrinksZonaSul()

conn.commit()
print('Dados inseridos com sucesso.')
conn.close()