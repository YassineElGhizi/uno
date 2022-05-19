from typing import List
import json

from mappers.Helpers.electroplanet_helprs.generale_purposed_functions import get_electroplanet_beaute_sante, get_category_id_beaute_sante
from mappers.Helpers.electroplanet import extract_specification_json, get_brand_id

def beaute_sante(brands : List) -> List:
    #Getting Electroplanet Products
    results = get_electroplanet_beaute_sante()
    res_to_post_fastapi = []

    for r in results:
        tmp_d = {}
        item_options = []

        tmp_d["current_price"] = r["current_price"]
        tmp_d["category_in_store"] = r["category_in_store"]
        tmp_d["category_in_store_to_id"] = get_category_id_beaute_sante(r["category_in_store"])
        tmp_d["link"] = r["link"]
        tmp_d["image_url"] = r["image_url"]
        tmp_d["current_price"] = r["current_price"]
        tmp_d["name_in_store"] = r["name_in_store"]
        tmp_d["details"] = r["details"]
        tmp_d["unique_id"] = r["unique_id"]

        tmp_specification_json = json.loads(r["specification"])
        try:
            tmp_json = extract_specification_json(tmp_specification_json['specification_table'])
        except:
            continue

        id_brand = 596
        if 'marque' in tmp_json:
            id_brand = get_brand_id(brands, tmp_json['marque'])
            if tmp_json['marque'].title() not in r["name_in_store"].title():
                tmp_d["prod_title"] = tmp_json['marque'].title() + ' ' + r["name_in_store"] + " - " + tmp_d["unique_id"]
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

