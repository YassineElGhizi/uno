import time
import pymysql
import requests
import json
from mappers.Helpers.uno import *
import logging
import math
from fetch_api import fetch_brands

#VARS
logging.basicConfig(filename='../uno_mapper.log',encoding='utf-8',level=logging.DEBUG,format='%(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
url = "http://127.0.0.1:9999/options?website=uno"
url_post = "http://127.0.0.1:9999/products?website=uno"
login_url = "http://localhost:9999/login"
mapper_credetials = {"username": "uno_mapper","password": "unoMapperSupero2022"}
payload = json.dumps(mapper_credetials)
obe_by_req = 100

#GETTING THE JWT TOKEN
print("[+] preparing to get token")
headers = {'Content-Type': 'application/json'}
s = requests.session()
response = s.post(login_url, headers=headers, data=payload)
if response.status_code == 401:
    print("[-] err 401 : Invalid username and/or password")
    quit()
print("[+] token recieved with success")
token = json.loads(response.text)['token']
#GETTING OPTIONS
headers = {'Content-Type': 'application/json','Authorization': f'Bearer {token}'}
response = requests.request("GET", url , headers=headers)
tmp = json.loads(response.text)

#Fetching brands
supero_brand = fetch_brands(token,s)

#Fetching from LOCAL DB
mydb = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="supero_datalake2",)
mycursor = mydb.cursor()
sql = "SELECT * FROM ITEMS WHERE id_store = 1"
mycursor.execute(sql,)
results = dictfetchall(mycursor)

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


for r in results:
    tmp_d = {}
    item_options = []

    tmp_d["current_price"] = r["current_price"]
    tmp_d["brand_id"] = get_item_brand_id(supero_brand, 'apple')
    if r["category_in_store"] == 'iphone':
        tmp_d["category_in_store_to_id"] = 137
    if r["category_in_store"] == 'ipad':
        tmp_d["category_in_store_to_id"] = 152
    if r["category_in_store"] == 'mac':
        tmp_d["category_in_store_to_id"] = 307
    if r["category_in_store"] == 'apple watch':
        tmp_d["category_in_store_to_id"] = 139
    if r["category_in_store"] == 'apple tv':
        continue
    if r["category_in_store"] == 'chargeur':
        tmp_d["category_in_store_to_id"] = 144
    if r["category_in_store"] == 'accessoires iphone':
        tmp_d["category_in_store_to_id"] = 308
    if r["category_in_store"] == 'accessoires mac':
        tmp_d["category_in_store_to_id"] = 309
    if r["category_in_store"] == 'powerbank':
        tmp_d["category_in_store_to_id"] = 310
    if r["category_in_store"] == 'coques iphone':
        tmp_d["category_in_store_to_id"] = 141
    if r["category_in_store"] == 'disque dur externe':
        tmp_d["category_in_store_to_id"] = 191
    if r["category_in_store"] == 'tablette graphique':
        continue
    if r["category_in_store"] == 'airpods':
        tmp_d["category_in_store_to_id"] = 143

    tmp_d["category_in_store"] = r["category_in_store"]
    tmp_d["link"] = r["link"]
    tmp_d["prod_name"] = r["prod_name"]
    tmp_d["image_url"] = r["image_url"]
    tmp_d["current_price"] = r["current_price"]
    tmp_d["name_in_store"] = r["name_in_store"]
    tmp_d["details"] = r["details"]
    id_gatantie = None
    id_color = None
    id_ram = None
    id_stockage = None
    id_connexion_adapter = None
    id_screen_size = None
    id_stockage_type = None
    id_length = None
    id_power = None

    tmp_json = json.loads(r["specification"])
    tmp_all_keys = []
    keys = tmp_json.keys()
    [tmp_all_keys.append(k) for k in keys if k not in tmp_all_keys]
    if 'color' in keys:
        id_color = get_item_color_id(tmp_json["color"])
    if 'garantie' in keys:
        id_gatantie = get_item_garantie_id(tmp_json["garantie"])
    if 'ram' in keys:
        id_ram = get_item_ram_id(tmp_json["ram"])
    if 'stockage' in keys:
        id_stockage = get_item_stockage_id(tmp_json["stockage"])
    if 'connexion_adapter' in keys:
        id_connexion_adapter = get_item_connexion_adapter_id(tmp_json['connexion_adapter'])
    if 'screen_size' in keys:
        id_screen_size = get_item_screen_size_id(tmp_json['screen_size'])
    if 'stockage_type' in keys:
        id_stockage_type = get_item_stockage_type_id(tmp_json['stockage_type'])
    if 'length' in keys:
        id_length = get_item_length_id(tmp_json['length'])
    if 'power' in keys:
        id_power = get_item_power_id(tmp_json['power'])

    if id_gatantie != None:
        tmp_d['id_gatantie'] = id_gatantie
        item_options.append(id_gatantie)
    if id_color != None:
        tmp_d['id_color'] = id_color
        item_options.append(id_color)
    if id_ram != None:
        tmp_d['id_ram'] = id_ram
        item_options.append(id_ram)
    if id_stockage != None:
        tmp_d['id_stockage'] = id_stockage
        item_options.append(id_stockage)
    if id_connexion_adapter != None:
        tmp_d['id_connexion_adapter'] = id_connexion_adapter
        item_options.append(id_connexion_adapter)
    if id_screen_size != None:
        tmp_d['id_screen_size'] = id_screen_size
        item_options.append(id_screen_size)
    if id_stockage_type != None:
        tmp_d['id_stockage_type'] = id_stockage_type
        item_options.append(id_stockage_type)
    if id_power != None:
        tmp_d['id_power'] = id_power
        item_options.append(id_power)

    tmp_d['options'] = item_options
    res_to_post_fastapi.append(tmp_d)

logging.info(f"MAPPED {len(res_to_post_fastapi)} ITEMS")

# [print(x) for x in res_to_post_fastapi]
print(f"len (res_to_post_fastapi) = {len(res_to_post_fastapi)}")

payload = json.dumps(res_to_post_fastapi)
response = requests.request("POST", url_post, headers=headers, data=payload)
print(response.text)
print(f"response.elapsed.total_seconds() = {response.elapsed.total_seconds()}")