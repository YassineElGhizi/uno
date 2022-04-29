from typing import List
import json

from mappers.Helpers.electroplanet_helprs.generale_purposed_functions import get_tv
from mappers.Helpers.electroplanet import get_item_color_id, get_item_screen_size_id
from mappers.Helpers.electroplanet_helprs.generale_purposed_functions import get_category_id
from mappers.Helpers.electroplanet import extract_specification_json, get_brand_id, get_product_name_id



def tv(brands : List , list_of_mapped_product_names) -> List:
    #Getting Electroplanet Products
    results = get_tv()

    res_to_post_fastapi = []

    for r in results:
        tmp_d = {}
        item_options = []

        tmp_d["current_price"] = r["current_price"]
        tmp_d["category_in_store"] = r["category_in_store"]
        tmp_d["category_in_store_to_id"] = get_category_id(r["category_in_store"])
        tmp_d["link"] = r["link"]
        tmp_d["image_url"] = r["image_url"]
        tmp_d["current_price"] = r["current_price"]
        tmp_d["name_in_store"] = r["name_in_store"]
        tmp_d["details"] = r["details"]

        id_brand = None
        id_color = None
        id_screen_size = None

        tmp_specification_json = json.loads(r["specification"])
        try:
            tmp_json = extract_specification_json(tmp_specification_json['specification_table'])
        except Exception as e:
            continue

        if int(tmp_d["category_in_store_to_id"]) != 141 :
            if 'reference_fournisseur' in tmp_json:
                tmp_d["prod_name"] = get_product_name_id(tmp_json["reference_fournisseur"] , list_of_mapped_product_names)
        else:
            tmp_d["prod_name"] = r["name_in_store"]


        if 'marque' in tmp_json:
            id_brand = get_brand_id(brands, tmp_json['marque'])
        if 'couleur' in tmp_json:
            id_color = get_item_color_id(tmp_json["couleur"])
        if 'coloris' in tmp_json:
            id_color = get_item_color_id(tmp_json["coloris"])

        if "taille_d'écran" in tmp_json.keys():
            id_screen_size = get_item_screen_size_id(tmp_json["taille_d'écran"])

        if id_color != None:
            tmp_d['id_color'] = id_color
            item_options.append(id_color)
        if id_screen_size != None:
            tmp_d['id_screen_size'] = id_screen_size
            item_options.append(id_screen_size)
        if id_brand != None:
            tmp_d['brand_id'] = id_brand

        tmp_d['options'] = item_options
        res_to_post_fastapi.append(tmp_d)

    # [print(i , '\n') for i in res_to_post_fastapi]
    print(f"len (res_to_post_fastapi) = {len(res_to_post_fastapi)}")
    return res_to_post_fastapi

