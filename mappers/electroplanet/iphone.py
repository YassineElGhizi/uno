import time
import pymysql
import requests
import json
from mappers.Helpers.electroplanet import *
import logging
import math

logging.basicConfig(
    filename='../electroplanet.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)


# #GETTING THE JWT TOKEN
print("[+] preparing to get token")
mapper_credetials = {
  "username": "electroplanet_mapper",
  "password": "electroplanetMapperSupero2022"
}
login_url = "http://localhost:9999/login"
token : str
payload = json.dumps(mapper_credetials)
headers = {
  'Content-Type': 'application/json'
}

s = requests.session()
response = s.post(login_url, headers=headers, data=payload)
if response.status_code == 401:
    print("[-] err 401 : Invalid username and/or password")
    quit()
print("[+] token recieved with success")
token = json.loads(response.text)['token']


# Global Conf
url = "http://127.0.0.1:9999/options?website=electroplanet-iphone"
# url_post = "http://127.0.0.1:9999/products?website=uno"

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
}

response = s.get(url , headers=headers)
# response = requests.request("GET", url , headers=headers)
tmp = json.loads(response.text)
obe_by_req = 100
apple_id = 33

mydb = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="",
    database="supero_datalake2",
)

mycursor = mydb.cursor()
sql = "SELECT * FROM ITEMS WHERE id_store = 3 and category_in_store like \'iphone\' or category_in_store like \'telephone-android\'"
mycursor.execute(sql,)
results = dictfetchall(mycursor)


# for r in results:
#     x = json.loads(r["specification"])
#     keys = x.keys()
#     [ all_keys.append(k) for k in keys if k not in all_keys ]
# secondary_keys = []
# for r in results:
#     x = json.loads(r["specification"])
#     try:
#         all_brands.append(x["brand"])
#         item_ref.append(x["item_ref"])
#         specification_table.append(x["specification_table"])
#         for r in extract_specification(x["specification_table"]):
#             keys = r.keys()
#             [secondary_keys.append(k) for k in keys if k not in secondary_keys]
#     except Exception as e:
#         pass
# all_keys = secondary_keys



for t in tmp:
    if t['id_parent'] == 1:
        electroplanet_colors.append(t)
        continue
    if t['id_parent'] == 2:
        electroplanet_storage.append(t)
        continue
    if t['id_parent'] == 3:
        electroplanet_ram.append(t)
        continue
    if t['id_parent'] == 5:
        electroplanet_taille_ecrant.append(t)
        continue
    if t['id_parent'] == 6:
        electroplanet_type_hd.append(t)
        continue
    if t['id_parent'] == 143:
        electroplanet_garanties.append(t)
        continue
    if t['id_parent'] == 152:
        electroplanet_connector_adapter.append(t)
        continue
    if t['id_parent'] == 187:
        electroplanet_type_stockage.append(t)
        continue
    if t['id_parent'] == 4:
        electroplanet_lenght.append(t)
        continue
    if t['id_parent'] == 156:
        electroplanet_power.append(t)
        continue


for r in results:
    tmp_d = {}
    item_options = []

    tmp_d["current_price"] = r["current_price"]
    tmp_d["category_in_store"] = r["category_in_store"]
    tmp_d["brand_id"] = apple_id
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

    tmp_specification_json = json.loads(r["specification"])
    tmp_json = extract_specification_json(tmp_specification_json['specification_table'])

    if 'couleur' in tmp_json:
        id_color = get_item_color_id(tmp_json["couleur"])
    if 'garantie' in tmp_json:
        id_gatantie = get_item_garantie_id(tmp_json["garantie"])
    if 'mémoire_ram' in tmp_json:
        id_ram = get_item_ram_id(tmp_json["mémoire_ram"])
    if 'mémoire_de_stockage' in tmp_json:
        id_stockage = get_item_stockage_id(tmp_json["mémoire_de_stockage"])
    if 'reseau' in tmp_json:
        id_connexion_adapter = get_item_connexion_adapter_id(tmp_json['reseau'])
    if 'taille_d\'ecran' in tmp_json:
        id_screen_size = get_item_screen_size_id(tmp_json['taille_d\'ecran'])
    if 'stockage_type' in tmp_json:
        id_stockage_type = get_item_stockage_type_id(tmp_json['stockage_type'])
    if 'length' in tmp_json:
        id_length = get_item_length_id(tmp_json['length'])
    if 'power' in tmp_json:
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
print(f"len (res_to_post_fastapi) = {len(res_to_post_fastapi)}")
#
#
# nb_req = math.ceil(len(res_to_post_fastapi) / obe_by_req)
# reqs = []
# tmp = []
# for num , k in enumerate(res_to_post_fastapi):
#     tmp.append(k)
#     if (num+1) == len(res_to_post_fastapi):
#         reqs.append(tmp)
#     if (num+1) % obe_by_req == 0:
#         reqs.append(tmp)
#         tmp = []
#         continue
#
#
# for n ,r in enumerate(reqs):
#     print(f'preparing req NO {n}')
#     payload = json.dumps(r)
#     response = requests.request("POST", url_post, headers=headers, data=payload)
#     print(response.text)
#     print(f"response.elapsed.total_seconds() = {response.elapsed.total_seconds()}")
#     time.sleep(5)
