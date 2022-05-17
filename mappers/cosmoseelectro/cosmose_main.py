from typing import List
import json
import requests

from mappers.Helpers.electroplanet import get_options_from_api
from mappers.Helpers.fetch_from_local import get_mapped_procuts
from mappers.Helpers.generale_purposed_functions import get_jwt_token_or_fail
from mappers.cosmoseelectro.helpers import get_cosmoseelectro_products, get_item_color_id, get_cosmose_category_id, get_item_ram_id

from mappers.electroplanet.fetch_api import fetch_brands
from mappers.cosmoseelectro.helpers import get_brand_id, get_product_name_id, get_item_screen_size_id

#To Fetch From API
from mappers.electroplanet.main import login_url, headers, payload

from mappers.cosmoseelectro.helpers import post_list_of_product


def main( brands : List , list_of_mapped_product_names) -> List:

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
        # tmp_d["name_in_store"] = r["name_in_store"]
        tmp_d["name_in_store"] = r["prod_name"]
        tmp_d["details"] = r["details"]

        id_brand = None
        id_color = None
        id_ram = None
        id_stockage = None
        id_screen_size = None
        id_stockage_type = None

        tmp_specification_json = json.loads(r["specification"])
        tmp_d["prod_name"] = get_product_name_id(r["prod_name"], list_of_mapped_product_names)

        id_brand = get_brand_id(brands, tmp_specification_json['specification_table'])
        id_color = get_item_color_id(r["prod_name"])

        # CHECK LATER BECAUSE THERE IS NO GENERAL FORMAT
        # if r['category_in_store'] in ['Ordinateur portable' , 'Tablettes'] or r['category_in_store'] == 'Smartphone':
        #     id_ram = get_item_ram_id(r["prod_name"])
        #CHECK LATER BECAUSE DIS DURES & USB ARE IN SAME CATEGORY
        # if r['category_in_store'] == 'Stockage informatique':
        #     id_stockage = get_item_stockage_id(r["prod_name"])

        if r['category_in_store'] == 'Téléviseur':
            if ' 4k ' in r['prod_name'] or ' 4K ' in r['prod_name']:
                tmp_d["category_in_store_to_id"] = '271'


        if id_color != None:
            tmp_d['id_color'] = id_color
            item_options.append(id_color)
        # if id_ram != None:
        #     tmp_d['id_ram'] = id_ram
        #     item_options.append(id_ram)
        # if id_stockage != None:
        #     tmp_d['id_stockage'] = id_stockage
        #     item_options.append(id_stockage)
        #     item_options.append(id_stockage)
        # if id_screen_size != None:
        #     tmp_d['id_screen_size'] = id_screen_size
        #     item_options.append(id_screen_size)
        # if id_stockage_type != None:
        #     tmp_d['id_stockage_type'] = id_stockage_type
        #     item_options.append(id_stockage_type)
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

    list_of_mapped_product_names = get_mapped_procuts()

    list_of_products = main(fetch_brands(token, 'electroplanet_smartphones_tablette' , s), list_of_mapped_product_names)
    post_list_of_product(list_of_products, token)