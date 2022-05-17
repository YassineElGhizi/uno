import json
from itertools import groupby
from typing import List

import requests
from bs4 import BeautifulSoup as BS


from mappers.Helpers.electroplanet import electroplanet_colors, electroplanet_ram, electroplanet_storage, \
    electroplanet_taille_ecrant
from mappers.Helpers.electroplanet_helprs.generale_purposed_functions import mydb




def dictfetchall(cursor):
    """Returns all rows from a cursor as a list of dicts not tuples"""
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()]


def get_cosmoseelectro_products():
    mycursor = mydb.cursor()
    sql = """
           SELECT distinct * FROM ITEMS WHERE id_store = 8
           and (
           category_in_store like 'Bébé'
           or category_in_store like 'Coiffure'
           or category_in_store like 'Rasage pour lui'
           or category_in_store like 'Préparation culinaire'
           or category_in_store like 'Cuisson'
           or category_in_store like 'Cafetière et expresso'
           or category_in_store like 'Aide culinaire'
           or category_in_store like 'Cuisson conviviale'
           or category_in_store like 'Friteuses'
           or category_in_store like 'Réfrigérateur'
           or category_in_store like 'Encastrable'
           or category_in_store like 'Hotte aspirante'
           or category_in_store like 'Cuisinière'
           or category_in_store like 'Pack électroménager'
           or category_in_store like 'Machine à laver'
           or category_in_store like 'Sèche linge'
           or category_in_store like 'Lave-vaisselle'
           or category_in_store like 'Plaque de cuisson'
           or category_in_store like 'Congélateur'
           or category_in_store like 'Entretien du sol'
           or category_in_store like 'Soin du linge'
           or category_in_store like 'Chauffe eau'
           or category_in_store like 'Climatisation'
           or category_in_store like 'Chauffage'
           or category_in_store like 'Traitement air'
           or category_in_store like 'Téléviseur'
           or category_in_store like 'Appareil photo numérique'
           or category_in_store like 'Accessoires tv-vidéo'
           or category_in_store like 'Barre de son'
           or category_in_store like 'Enceinte'
           or category_in_store like 'Casque audio'
           or category_in_store like 'Ecouteurs'
           or category_in_store like 'Home cinéma'
           or category_in_store like 'Article de boisson'
           or category_in_store like 'Ordinateur portable'
           or category_in_store like 'Bagagerie'
           or category_in_store like 'Périphérique informatique'
           or category_in_store like 'Imprimante et scanner'
           or category_in_store like 'Accessoires  gaming'
           or category_in_store like 'Tablettes'
           or category_in_store like 'Accessoires smartphones & tablettes'
           or category_in_store like 'Objets connectes'
           or category_in_store like 'Smartphone'
           );
               """
    mycursor.execute(sql, )
    results = dictfetchall(mycursor)
    return results

def get_item_color_id(color:str):
    try:
        for c in electroplanet_colors:
            if c["value"].title() in color.title() :
                return c['id']
        return None
    except:
        return None

def get_cosmose_category_id(cat_in_store):
    f = open('../mappeed_categories/cosmoseelectro/mapped_products.json')
    data = json.load(f)
    f.close()

    for c in data:
        tmp =cat_in_store.replace('è' , 'e')
        tmp =tmp.replace('é' , 'e')
        tmp = tmp.replace('à' , 'a')
        tmp = tmp.replace('â' , 'a')
        tmp = tmp.replace('É' , 'E')
        tmp = tmp.replace('ê' , 'e')
        tmp = tmp.replace('ë' , 'e')
        tmp = tmp.replace('ç' , 'c')
        tmp = tmp.replace('î' , 'i')
        tmp = tmp.replace('ï' , 'i')
        if tmp in c.keys():
            prod_cat = c[str(tmp)]
            break
    else:
        if cat_in_store == 'Protection Solaire':
            return '389'
        prod_cat= '311'
        print(f'311 FOR: {cat_in_store}')
    return prod_cat



def get_brand_id(brands:List , item_brand : str):
    soup = BS(item_brand, features='html.parser')
    item_brand = (soup.find('tr', {'class': 'marque'}).find('td').getText()).strip()
    if item_brand == 'Apple':
        for x in brands:
            if x['name'] == 'Apple':
                return str(x['id'])
    for x in brands:
        if x['name'].title() in item_brand.title():
            return str(x['id'])
    # print(f'NEW BRAND HAS BEEN DETECTED: {item_brand}')
    for x in brands:
        if x['name'] == 'UNKNOW':
            return str(x['id'])



def get_product_name_id(prod_name_in_store , list_of_mapped_product_names):
    for n in list_of_mapped_product_names:
        if n.title() in prod_name_in_store.title().replace(',' , '.'):
            return n
    # print(f'CANT FIND PRODUCT NAME IN: {prod_name_in_store}')
    return prod_name_in_store.split(' - ')[0]

def extract_digits(sentance:str):
    try:
        return [int(''.join(i)) for is_digit, i in groupby(sentance, str.isdigit) if is_digit]
    except:
        return None

def get_item_ram_id(ram:str):
    ram_digit = extract_digits(ram)[0]
    for c in electroplanet_ram:
        if int(c['value']) == ram_digit:
            return c['id']
    # print(f'NO RAM FOUND FOR: {ram}')
    return None


def get_item_stockage_id(stockage:str):
    stockage_digit = extract_digits(stockage)[0]
    for c in electroplanet_storage:
        if int(c['value']) == stockage_digit:
            return c['id']
    return None



def extract_digits_float(sentance : str):
    sentance = sentance.replace(',' , '.').replace('\'' , '\"')
    try:
        res = re.findall("\d+\.\d+", sentance)
        if len(res) == 0:
            res = extract_digits(sentance)
        if float(res[0]) < 8.0:
            try:
                return float(sentance.split("\"")[0])
            except:
                print(f"the following has digit float : {sentance}")
                return None
    except:
        res = extract_digits(sentance)
    try:
        return res[0]
    except:
        return None

def get_item_screen_size_id(screen_size:str):
    print(screen_size)
    screen_size_digit = extract_digits_float(screen_size)
    for c in electroplanet_taille_ecrant:
        if float(c['value']) == screen_size_digit:
            return c['id']
    return None


def post_list_of_product(res_to_post_fastapi, token):
    url_post = "http://127.0.0.1:9999/products?website=cosmoseelectro"
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
    payload = json.dumps(res_to_post_fastapi)
    response = requests.request("POST", url_post, headers=headers, data=payload)
    print(response.text)
    print(f"response.elapsed.total_seconds() = {response.elapsed.total_seconds()}")



