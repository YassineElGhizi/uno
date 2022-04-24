from mappers.Helpers.uno import *
from mappers.Helpers.fetch_from_local import get_mapped_procuts
from mappers.Helpers.generale_purposed_functions import get_product_name_from_product_title, organise_options_from_json
from fetch_api import fetch_brands

#VARS
list_outlayers = ["anker","Silicon","power","Sandisk","LaCie","Beats",]
options_url = "http://127.0.0.1:9999/options?website=uno"
url_post = "http://127.0.0.1:9999/products?website=uno"
login_url = "http://localhost:9999/login"
mapper_credetials = {"username": "uno_mapper","password": "unoMapperSupero2022"}
payload = json.dumps(mapper_credetials)

#GETTING THE JWT TOKEN
print("[+] preparing to get token")
s = requests.session()
token = getting_jwt_token(s, login_url, payload)

#GETTING OPTIONS
headers = {'Content-Type': 'application/json','Authorization': f'Bearer {token}'}
response = requests.request("GET", options_url , headers=headers)
tmp = json.loads(response.text)
organise_options_from_json(tmp)

#Fetching brands
supero_brand = fetch_brands(token,s)

#Fetching Products
list_of_mapped_product_names = get_mapped_procuts()

#Fetching Items
results = get_uno_products()

#Parsing specification json field
parsing_specification_json_field(results)

for r in results:
    tmp_d = {}
    item_options = []
    tmp_d["current_price"] = r["current_price"]

    #Product Name
    tmp_d["prod_name"] = get_product_name_from_product_title((r["name_in_store"] , r["prod_name"]), list_of_mapped_product_names)
    if tmp_d["prod_name"] not in list_outlayers:
        tmp_d["brand_id"] = get_item_brand_id(supero_brand, 'apple')
    else:
        tmp_d["brand_id"] = get_item_brand_id(supero_brand, tmp_d["prod_name"])

    #Categories
    if r["category_in_store"] == 'iphone':
        tmp_d["category_in_store_to_id"] = 137
    if r["category_in_store"] == 'ipad':
        tmp_d["category_in_store_to_id"] = 152
    if r["category_in_store"] == 'mac':
        tmp_d["category_in_store_to_id"] = 307
    if r["category_in_store"] == 'apple watch':
        tmp_d["category_in_store_to_id"] = 148
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

    if 'Cable USB' in tmp_d["prod_name"] or 'Cable Apple USB' in tmp_d["prod_name"]:
        tmp_d["category_in_store_to_id"] = 145

    tmp_d["category_in_store"] = r["category_in_store"]



    tmp_d["link"] = r["link"]
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

print(f"len (res_to_post_fastapi) = {len(res_to_post_fastapi)}")

payload = json.dumps(res_to_post_fastapi)
response = requests.request("POST", url_post, headers=headers, data=payload)
print(response.text)
print(f"response.elapsed.total_seconds() = {response.elapsed.total_seconds()}")
