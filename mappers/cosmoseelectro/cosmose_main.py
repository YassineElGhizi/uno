from typing import List
import json
import requests

from mappers.Helpers.electroplanet import get_options_from_api
from mappers.Helpers.generale_purposed_functions import get_jwt_token_or_fail
from mappers.cosmoseelectro.helpers import get_cosmoseelectro_products, get_item_color_id, get_cosmose_category_id
from mappers.electroplanet.fetch_api import fetch_brands
from mappers.cosmoseelectro.helpers import get_brand_id
from mappers.cosmoseelectro.helpers import post_list_of_product

#To Fetch From API
from mappers.electroplanet.main import login_url, headers, payload

def main(brands : List) -> List:
    results = get_cosmoseelectro_products()
    res_to_post_fastapi = []
    for r in results:
        tmp_d = {}
        item_options = []

        tmp_d["current_price"] = r["current_price"]
        tmp_d["category_in_store"] = r["category_in_store"]
        tmp_d["category_in_store_to_id"] = get_cosmose_category_id(r["category_in_store"])
        tmp_d["link"] = r["link"]
        tmp_d["image_url"] = r["image_url"]
        tmp_d["current_price"] = r["current_price"]
        tmp_d["name_in_store"] = r["name_in_store"]
        tmp_d["details"] = r["details"]
        tmp_d["unique_id"] = r["unique_id"]

        id_brand = 596
        id_color = None
        id_ram = None
        id_stockage = None
        id_screen_size = None
        id_stockage_type = None

        tmp_specification_json = json.loads(r["specification"])

        id_brand , brand_name = get_brand_id(brands, tmp_specification_json['specification_table'])
        if brand_name:
            if brand_name.title() not in r["name_in_store"].title():
                tmp_d["prod_title"] = brand_name.title() + ' ' + r["name_in_store"] + " - " + tmp_d["unique_id"]
            else:
                tmp_d["prod_title"] = r["name_in_store"] + " - " + tmp_d["unique_id"]
        else:
            tmp_d["prod_title"] = r["name_in_store"] + " - " + tmp_d["unique_id"]

        id_color = get_item_color_id(r["prod_name"])

        if r['category_in_store'] == 'Téléviseur':
            if ' 4k ' in r['prod_name'] or ' 4K ' in r['prod_name']:
                tmp_d["category_in_store_to_id"] = '271'

        if id_color != None:
            tmp_d['id_color'] = id_color
            item_options.append(id_color)

        if id_brand != None:
            tmp_d['brand_id'] = id_brand

        tmp_d['options'] = item_options
        res_to_post_fastapi.append(tmp_d)

    # [print(i) for i in res_to_post_fastapi]
    # quit()
    print(f"len (res_to_post_fastapi) = {len(res_to_post_fastapi)}")
    return res_to_post_fastapi

if __name__ == '__main__':
    print("[+] preparing to get token")
    s = requests.session()
    token = get_jwt_token_or_fail(s, login_url, headers, payload)

    print("[+] getting options from API")
    get_options_from_api(token)

    list_of_products = main(fetch_brands(token, 'electroplanet_smartphones_tablette' , s),)
    post_list_of_product(list_of_products, token)