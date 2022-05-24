from typing import List
import json
import requests

from mappers.Helpers.electroplanet import get_brand_id, get_options_from_api
from mappers.electroplanet.fetch_api import fetch_brands
from mappers.Helpers.generale_purposed_functions import get_jwt_token_or_fail
from mappers.Helpers.electroplanet import get_item_color_id

#Helpers
from bestmark_helpers import extract_specification_json_brestmark, get_category_id_bricoma, get_bestmark_products, get_item_stockage_id

mapper_credetials = {"username": "electroplanet_mapper", "password": "electroplanetMapperSupero2022"}
login_url = "http://localhost:9999/login"
url_post = "http://127.0.0.1:9999/products?website=bestmark"
payload = json.dumps(mapper_credetials)
headers = {'Content-Type': 'application/json'}

def post_list_of_product(res_to_post_fastapi, token):
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
    payload = json.dumps(res_to_post_fastapi)
    response = requests.request("POST", url_post, headers=headers, data=payload)
    print(response.text)
    print(f"response.elapsed.total_seconds() = {response.elapsed.total_seconds()}")


def main(brands : List) -> List:
    results = get_bestmark_products()
    res_to_post_fastapi = []

    for r in results:
        tmp_d = {}
        item_options = []

        tmp_d["current_price"] = r["current_price"]
        tmp_d["category_in_store"] = r["category_in_store"]
        tmp_d["category_in_store_to_id"] = get_category_id_bricoma(r["category_in_store"])
        tmp_d["link"] = r["link"]
        tmp_d["image_url"] = r["image_url"]
        tmp_d["current_price"] = r["current_price"]
        tmp_d["unique_id"] = r["unique_id"].strip()
        tmp_d["details"] = r["details"]
        tmp_d["name_in_store"] = r["name_in_store"]
        tmp_specification_json = json.loads(r["specification"])

        try:
            tmp_json = extract_specification_json_brestmark(tmp_specification_json['specification_table'])
        except Exception as e:
            continue

        id_brand = None
        id_color = None
        id_stockage = None
        if 'Marque' in tmp_json:
            id_brand = get_brand_id(brands, tmp_json['Marque'])

        if id_brand != None and tmp_json['Marque'] != 'SANS MARQUE' and tmp_json['Marque'].title() not in r["name_in_store"].title():
            tmp_d['brand_id'] = id_brand
            tmp_d["prod_title"] = tmp_json['Marque'].title() + ' ' + r["name_in_store"] + " - " + tmp_d["unique_id"]
        else:
            tmp_d["prod_title"] = r["name_in_store"] + " - " + tmp_d["unique_id"]
            tmp_d['brand_id'] = 507

        if 'Couleur' in tmp_json:
            id_color = get_item_color_id(tmp_json["Couleur"])

        if id_color != None:
            tmp_d['id_color'] = id_color
            item_options.append(id_color)

        if 'Stockage' in tmp_json:
            id_stockage = get_item_stockage_id(tmp_json["Stockage"])

        if id_stockage != None:
            tmp_d['id_stockage'] = id_stockage
            item_options.append(id_stockage)


        tmp_d['options'] = item_options
        res_to_post_fastapi.append(tmp_d)


    # [print(i , '\n') for i in res_to_post_fastapi]
    # quit()
    print(f"len (res_to_post_fastapi) = {len(res_to_post_fastapi)}")
    return res_to_post_fastapi

if __name__ == "__main__":
    print("[+] preparing to get token")
    s = requests.session()
    token = get_jwt_token_or_fail(s, login_url, headers, payload)

    print("[+] getting options from API")
    get_options_from_api(token)

    listof_products = main(fetch_brands(token, 'electroplanet_smartphones_tablette' , s))
    post_list_of_product(listof_products, token)