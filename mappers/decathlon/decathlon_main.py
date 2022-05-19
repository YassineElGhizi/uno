from typing import List
import json
import requests
import webcolors


from mappers.Helpers.electroplanet import get_brand_id, get_options_from_api
from mappers.decathlon.helpers import get_decathlon_products, get_category_id_decathlon, login_url, headers, payload, post_list_of_product
from mappers.electroplanet.fetch_api import fetch_brands
from mappers.Helpers.generale_purposed_functions import get_jwt_token_or_fail
from mappers.Helpers.electroplanet import get_item_color_id


def main(brands: List) -> List:
    #Getting Electroplanet Products
    results = get_decathlon_products()
    res_to_post_fastapi = []

    for r in results:
        tmp_d = {}
        item_options = []

        tmp_d["current_price"] = r["current_price"]
        tmp_d["category_in_store"] = r["category_in_store"]
        tmp_d["category_in_store_to_id"] = get_category_id_decathlon(r["category_in_store"])
        tmp_d["link"] = r["link"]
        tmp_d["image_url"] = r["image_url"]
        tmp_d["current_price"] = r["current_price"]
        tmp_d["name_in_store"] = r["name_in_store"]
        tmp_d["details"] = r["details"]
        tmp_d["unique_id"] = r["unique_id"]

        try:
            tmp_json = json.loads(r["specification"])
            geniric_color = tmp_json['specification_table']['generic_color']['value']
            try:
                id_color = get_item_color_id(webcolors.hex_to_name(geniric_color))
                if id_color != None:
                    item_options.append(id_color)
            except:
                pass
        except:
            pass

        id_brand = 596
        if 'item_brand' in tmp_json:
            id_brand = get_brand_id(brands, tmp_json['item_brand'])
            if tmp_json['item_brand'].title() not in r["name_in_store"].title():
                tmp_d["prod_title"] = tmp_json['item_brand'].title() + ' ' + r["name_in_store"] + " - " + tmp_d["unique_id"]
            else:
                tmp_d["prod_title"] = r["name_in_store"] + " - " + tmp_d["unique_id"]
        else:
            tmp_d["prod_title"] = r["name_in_store"] + " - " + tmp_d["unique_id"]
        if id_brand != None:
            tmp_d['brand_id'] = id_brand
        tmp_d['options'] = item_options
        res_to_post_fastapi.append(tmp_d)

    # [print(i , '\n') for i in res_to_post_fastapi]
    print(f"len (res_to_post_fastapi) = {len(res_to_post_fastapi)}")
    # quit()
    return res_to_post_fastapi

if __name__ == "__main__":
    print("[+] preparing to get token")
    s = requests.session()
    token = get_jwt_token_or_fail(s, login_url, headers, payload)

    print("[+] getting options from API")
    get_options_from_api(token)

    listof_products = main(fetch_brands(token, 'electroplanet_smartphones_tablette' , s))
    post_list_of_product(listof_products, token)
    
