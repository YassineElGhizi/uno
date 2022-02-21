import pymysql
import time
import requests
import json
from Helpers.uno import *
import logging
import math


logging.basicConfig(
    filename='uno_mapper.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)

#Global Conf
url = "http://127.0.0.1:9999/options?website=uno"
url_post = "http://127.0.0.1:9999/products?website=uno"

headers = {'Content-Type': 'application/json'}
response = requests.request("GET", url)
tmp = json.loads(response.text)
obe_by_req = 100

mydb = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="",
    database="supero_datalake2",
)

mycursor = mydb.cursor()
sql = "SELECT * FROM ITEMS WHERE id_store = 1"
mycursor.execute(sql,)
results = dictfetchall(mycursor)

for r in results:
    x = json.loads(r["specification"])
    keys = x.keys()
    [ all_keys.append(k) for k in keys if k not in all_keys ]

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

for t in tmp:
    if t['id_parent'] == 1:
        uno_colors.append(t)
        continue
    if t['id_parent'] == 2:
        uno_storage.append(t)
        continue
    if t['id_parent'] == 3:
        uno_ram.append(t)
        continue
    if t['id_parent'] == 5:
        uno_taille_ecrant.append(t)
        continue
    if t['id_parent'] == 6:
        uno_type_hd.append(t)
        continue
    if t['id_parent'] == 143:
        uno_garanties.append(t)
        continue
    if t['id_parent'] == 157:
        uno_connector_adapter.append(t)
        continue
    if t['id_parent'] == 172:
        uno_type_stockage.append(t)
        continue
    if t['id_parent'] == 4:
        uno_lenght.append(t)
        continue
    if t['id_parent'] == 185:
        uno_power.append(t)
        continue

for r in results:
    tmp_d = {}
    tmp_d["current_price"] = r["current_price"]
    tmp_d["category_in_store"] = r["category_in_store"]
    tmp_d["link"] = r["link"]
    tmp_d["prod_name"] = r["prod_name"]
    tmp_d["image_url"] = r["image_url"]
    tmp_d["current_price"] = r["current_price"]
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
    if id_color != None:
        tmp_d['id_color'] = id_color
    if id_ram != None:
        tmp_d['id_ram'] = id_ram
    if id_stockage != None:
        tmp_d['id_stockage'] = id_stockage
    if id_connexion_adapter != None:
        tmp_d['id_connexion_adapter'] = id_connexion_adapter
    if id_screen_size != None:
        tmp_d['id_screen_size'] = id_screen_size
    if id_stockage_type != None:
        tmp_d['id_stockage_type'] = id_stockage_type
    if id_power != None:
        tmp_d['id_power'] = id_power

    res_to_post_fastapi.append(tmp_d)

logging.info(f"MAPPED {len(res_to_post_fastapi)} ITEMS")

# [print(x) for x in res_to_post_fastapi]
print(f"len (res_to_post_fastapi) = {len(res_to_post_fastapi)}")


nb_req = math.ceil(len(res_to_post_fastapi) / obe_by_req)
reqs = []
tmp = []
for num , k in enumerate(res_to_post_fastapi):
    tmp.append(k)
    if (num+1) == len(res_to_post_fastapi):
        reqs.append(tmp)
    if (num+1) % obe_by_req == 0:
        reqs.append(tmp)
        tmp = []
        continue




for r in reqs:
    payload = json.dumps(r)
    response = requests.request("POST", url_post, headers=headers, data=payload)
    print(f"response.text = {response.text}")
    quit()
    # time.sleep(100)
    pass