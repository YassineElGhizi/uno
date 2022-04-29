from typing import List
import json

from mappers.Helpers.electroplanet_helprs.generale_purposed_functions import get_electroplanet_audio ,get_category_id_audio
from mappers.Helpers.electroplanet import extract_specification_json, get_brand_id


def audio(brands: List) -> List:
    results = get_electroplanet_audio();
    res_to_post_fastapi = []

    for r in results:
        tmp_d = {}
        item_options = []

        tmp_d["current_price"] = r["current_price"]
        tmp_d["category_in_store"] = r["category_in_store"]
        tmp_d["category_in_store_to_id"] = get_category_id_audio(r["category_in_store"])
        tmp_d["link"] = r["link"]
        tmp_d["image_url"] = r["image_url"]
        tmp_d["current_price"] = r["current_price"]
        tmp_d["name_in_store"] = r["name_in_store"]
        tmp_d["prod_name"] = r["prod_name"]
        tmp_d["details"] = r["details"]

        tmp_specification_json = json.loads(r["specification"])
        try:
            tmp_json = extract_specification_json(tmp_specification_json['specification_table'])
        except Exception as e:
            continue

        id_brand = None
        if 'marque' in tmp_json:
            id_brand = get_brand_id(brands, tmp_json['marque'])
        if id_brand != None:
            tmp_d['brand_id'] = id_brand

        tmp_d['options'] = item_options
        res_to_post_fastapi.append(tmp_d)

    # [print(i , '\n') for i in res_to_post_fastapi]
    # quit()
    print(f"len (res_to_post_fastapi) = {len(res_to_post_fastapi)}")
    return res_to_post_fastapi

