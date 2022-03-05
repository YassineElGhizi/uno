import json
from itertools import groupby
import re
from typing import List
from bs4 import BeautifulSoup as BS


##Vars that get populated from FASTAPI
electroplanet_colors =[]
electroplanet_storage =[]
electroplanet_ram =[]
electroplanet_taille_ecrant=[]
electroplanet_type_hd = []
electroplanet_connector_adapter = []
electroplanet_type_stockage = []
electroplanet_power = []
electroplanet_lenght = []
electroplanet_garanties = []

#Vars to be used localy

all_brands = []
item_ref = []
specification_table = []

all_garantie =[]
all_ram = []
all_stockage = []
screen_size = []
connexion_adapter = []
stockage_type = []
length = []
power = []
colors = []
all_keys = []
res_to_post_fastapi = []

#Global Function


def extract_specification(html_table : str):
    soup = BS(html_table , features="html.parser")
    targets = []
    for tag in soup.find_all('td'):
        try:
            d = {}
            txt = tag.get_text().strip()
            if txt != '':
                d[f"{tag.get('data-th').lower().replace('/' , '').replace(' ' , '_').replace('ã' , 'a').replace('š' , 's').replace('©' , '')}"] = txt
                targets.append(d)
        except:
            pass
    return targets

def extract_specification_json(html_table : str) -> dict:
    soup = BS(html_table , features="html.parser")
    d = {}
    for tag in soup.find_all('td'):
        try:
            txt = tag.get_text().strip()
            if txt != '':
                d[f"{tag.get('data-th').lower().replace('/' , '').replace(' ' , '_').replace('ã' , 'a').replace('š' , 's').replace('©' , '')}"] = txt
        except:
            pass
    return d



def extract_digits(sentance:str):
    try:
        return [int(''.join(i)) for is_digit, i in groupby(sentance, str.isdigit) if is_digit]
    except:
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
                print(f"the follwoing has None : {sentance}")
                return None
    except:
        res = extract_digits(sentance)
    try:
        return res[0]
    except:
        return None


def get_item_color_id(color:str):
    for c in electroplanet_colors:
        if color.title() == c["value"]:
            return c['id']
    return None

def get_item_garantie_id(garantie:str):
    garantie_digit = extract_digits(garantie)[0]
    for c in electroplanet_garanties:
        if int(c['value']) == garantie_digit:
            return c['id']
    return None

def get_item_ram_id(ram:str):
    ram_digit = extract_digits(ram)[0]
    for c in electroplanet_ram:
        if int(c['value']) == ram_digit:
            return c['id']
    return None

def get_item_stockage_id(stockage:str):
    stockage_digit = extract_digits(stockage)[0]
    for c in electroplanet_storage:
        if int(c['value']) == stockage_digit:
            return c['id']
    return None

def get_item_connexion_adapter_id(connexion_adapter:str):
    for ca in electroplanet_connector_adapter:
        if str(ca['value']) == str(connexion_adapter):
            return ca['id']
    return None

def get_item_screen_size_id(screen_size:str):
    screen_size_digit = extract_digits_float(screen_size)

    for c in electroplanet_taille_ecrant:
        if float(c['value']) == screen_size_digit:
            return c['id']
    return None


def get_item_length_id(lenght:str):
    try:
        stockage_type_digit1 = extract_digits(lenght)[0]
        stockage_type_digit = stockage_type_digit1/100
        tmp_list = [c for c in electroplanet_lenght if c['unit'] == 'm']
        for c in tmp_list:
            if int(stockage_type_digit) ==  int(c['value']):
                return c['id']
        tmp_list = [c for c in electroplanet_lenght if c['unit'] == 'm']
        for c in tmp_list:
            if int(stockage_type_digit1) ==  int(c['value']):
                return c['id']
        return None
    except:
        return None

def get_item_power_id(power:str):
    try:
        power_digit = extract_digits_float(power)
        for c in electroplanet_power:
            if float(power_digit) == float(c['value']):
                return c['id']
        power_digit = extract_digits(power)
        for c in electroplanet_power:
            if float(power_digit) == float(c['value']):
                return c['id']
        return None
    except:
        return None


def dictfetchall(cursor):
    """Returns all rows from a cursor as a list of dicts"""
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()]

def get_brand_id(brands:List , item_brand : str) -> str:
    for x in brands:
        if x['name'] == item_brand.title():
            return str(x['id'])
    print(f'new brands has been detected {item_brand}')
    for x in brands:
        if x['name'] == 'UNKNOW':
            return  str(x['id'])

def get_category_id(cat_str : str) -> str:
    cats = []
    with open('../electroplanet/electro_mapped_cats.json', 'r' , encoding='utf8') as j:
        cats =json.load(j)
    for dic_c in cats:
        if dic_c['electro_cat'] == cat_str:
            return dic_c['supero_cat']
    for dic_c in cats:
        if dic_c['electro_cat'] == 'UNKNOWN':
            return dic_c['supero_cat']