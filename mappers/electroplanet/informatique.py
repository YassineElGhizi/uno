from typing import List
import json

from mappers.Helpers.electroplanet import get_item_color_id, get_item_ram_id, get_item_stockage_id,get_item_screen_size_id
from mappers.Helpers.electroplanet_helprs.generale_purposed_functions import get_informatique_category_id, get_electro_informartique_products
from mappers.Helpers.electroplanet import extract_specification_json, get_brand_id, get_product_name_id



def informartique( brands : List) -> List:
    results = get_electro_informartique_products()
    res_to_post_fastapi = []

    for r in results:
        tmp_d = {}
        item_options = []

        tmp_d["current_price"] = r["current_price"]
        tmp_d["category_in_store"] = r["category_in_store"]
        tmp_d["category_in_store_to_id"] = get_informatique_category_id(r["category_in_store"])
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
        try:
            tmp_json = extract_specification_json(tmp_specification_json['specification_table'])
        except Exception as e:
            continue


        if 'marque' in tmp_json:
            id_brand = get_brand_id(brands, tmp_json['marque'])
            if tmp_json['marque'].title() not in r["name_in_store"].title():
                tmp_d["prod_title"] = tmp_json['marque'].title() + ' ' + r["name_in_store"] + " - " + tmp_d["unique_id"]
            else:
                tmp_d["prod_title"] = r["name_in_store"] + " - " + tmp_d["unique_id"]
        else:
            tmp_d["prod_title"] = r["name_in_store"] + " - " + tmp_d["unique_id"]

        if 'couleur' in tmp_json:
            id_color = get_item_color_id(tmp_json["couleur"])
        if 'coloris' in tmp_json:
            id_color = get_item_color_id(tmp_json["coloris"])
        if 'mémoire_ram' in tmp_json:
            id_ram = get_item_ram_id(tmp_json["mémoire_ram"])
        if 'mémoire_vive_(ram)' in tmp_json:
            id_ram = get_item_ram_id(tmp_json["mémoire_vive_(ram)"])
        if 'mémoire_de_stockage' in tmp_json:
            id_stockage = get_item_stockage_id(tmp_json["mémoire_de_stockage"])
        if 'capacite_disque_dur_ssd' in tmp_json:
            id_stockage = get_item_stockage_id(tmp_json["capacite_disque_dur_ssd"])
        if 'taille_d\'ecran' in tmp_json:
            id_screen_size = get_item_screen_size_id(tmp_json['taille_d\'ecran'])




        if id_color != None:
            tmp_d['id_color'] = id_color
            item_options.append(id_color)
        if id_ram != None:
            tmp_d['id_ram'] = id_ram
            item_options.append(id_ram)
        if id_stockage != None:
            tmp_d['id_stockage'] = id_stockage
            item_options.append(id_stockage)
        if id_screen_size != None:
            tmp_d['id_screen_size'] = id_screen_size
            item_options.append(id_screen_size)
        if id_stockage_type != None:
            tmp_d['id_stockage_type'] = id_stockage_type
            item_options.append(id_stockage_type)
        if id_brand != None:
            tmp_d['brand_id'] = id_brand

        tmp_d['options'] = item_options
        res_to_post_fastapi.append(tmp_d)


    # [print(i , '\n') for i in res_to_post_fastapi]
    # quit()
    print(f"len (res_to_post_fastapi) = {len(res_to_post_fastapi)}")
    return res_to_post_fastapi

