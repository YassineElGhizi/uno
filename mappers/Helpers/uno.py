import json
from itertools import groupby
import re
from typing import List

##Vars that get populated from FASTAPI
import pymysql
import requests

uno_colors =[]
uno_storage =[]
uno_ram =[]
uno_taille_ecrant=[]
uno_type_hd = []
uno_connector_adapter = []
uno_type_stockage = []
uno_power = []
uno_lenght = []

#Vars to be used localy
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
def extract_digits(sentance:str):
    try:
        return [int(''.join(i)) for is_digit, i in groupby(sentance, str.isdigit) if is_digit]
    except:
        return None

def extract_digits_float(sentance : str):
    try:
        res = re.findall("\d+\.\d+", sentance)
        if len(res) == 0:
            res = extract_digits(sentance)
        if float(res[0]) < 8.0:
            try:
                return float(sentance.split("\"")[0])
            except:
                # print(f"the follwoing has None : {sentance}")
                return None
    except:
        res = extract_digits(sentance)
    return res[0]


def get_item_color_id(color:str):
    for c in uno_colors:
        if color.title() == c["value"]:
            return c['id']
    return None

def get_item_ram_id(ram:str):
    ram_digit = extract_digits(ram)[0]
    for c in uno_ram:
        if int(c['value']) == ram_digit:
            return c['id']
    return None

def get_item_stockage_id(stockage:str):
    stockage_digit = extract_digits(stockage)[0]
    for c in uno_storage:
        if int(c['value']) == stockage_digit:
            return c['id']
    return None

def get_item_connexion_adapter_id(connexion_adapter:str):
    for ca in uno_connector_adapter:
        if str(ca) == str(connexion_adapter):
            return ca['value']
    return None

def get_item_screen_size_id(screen_size:str):
    screen_size_digit = extract_digits_float(screen_size)
    for c in uno_taille_ecrant:
        if float(c['value']) == screen_size_digit:
            return c['id']
    return None

def get_item_stockage_type_id(stockage_type:str):
    for c in uno_type_stockage:
        if stockage_type.lower() == c['value']:
            return c['id']
    return None

def get_item_length_id(lenght:str):
    stockage_type_digit = extract_digits(lenght)[0]
    tmp_list = [c for c in uno_lenght if c['unit'] == 'm']
    for c in tmp_list:
        if int(stockage_type_digit) ==  int(c['value']):
            return c['id']
    return None

def get_item_power_id(power:str):
    power_digit = extract_digits(power)[0]
    for c in uno_power:
        if int(power_digit) == int(c['value']):
            return c['id']
    return None


def dictfetchall(cursor):
    """Returns all rows from a cursor as a list of dicts"""
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()]

def get_item_brand_id(brands:List, item_brand : str) -> str:
    try:
        for i in brands:
            if i['name'].title().strip() == item_brand.title().strip():
                return str(i['id'])
    except:
        return '507'


def get_uno_products():
    mydb = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="", database="supero_datalake2", )
    mycursor = mydb.cursor()
    sql = "SELECT * FROM ITEMS WHERE id_store = 1"
    mycursor.execute(sql, )
    return dictfetchall(mycursor)

def getting_jwt_token(s, login_url, payload):
    headers = {'Content-Type': 'application/json'}
    response = s.post(login_url, headers=headers, data=payload)
    if response.status_code == 401:
        print("[-] err 401 : Invalid username and/or password")
        quit()
    print("[+] token recieved with success")
    return json.loads(response.text)['token']

def parsing_specification_json_field(results):
    for r in results:
        x = json.loads(r["specification"])
        try:
            colors.append(x["color"])
            all_garantie.append(x["garantie"])
            all_ram.append(x["ram"])
            all_stockage.append(x["stockage"])
            connexion_adapter.append(x["connexion_adapter"])
            screen_size.append(x["screen_size"])
            stockage_type.append(x["stockage_type"])
            length.append(x["length"])
            power.append(x["power"])
        except Exception as e:
            pass
