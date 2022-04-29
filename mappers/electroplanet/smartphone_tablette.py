from requests import Session
from typing import List
import json
from mappers.Helpers.electroplanet_helprs.generale_purposed_functions import organise_options_from_json, \
    get_smartphone_category_id
from mappers.Helpers.electroplanet import get_item_color_id, get_item_ram_id, get_item_stockage_id, get_item_connexion_adapter_id,get_item_screen_size_id,get_item_length_id,get_item_power_id


from mappers.Helpers.electroplanet_helprs.generale_purposed_functions import get_electroplanet_products, get_category_id
from mappers.Helpers.electroplanet import extract_specification_json, get_brand_id, get_product_name_id



def smartphones_tablette(token:str , s:Session , brands : List , list_of_mapped_product_names) -> List:
    #Getting Options
    url = "http://127.0.0.1:9999/options?website=electroplanet-iphone"
    headers = {'Content-Type': 'application/json','Authorization': f'Bearer {token}'}
    response = s.get(url , headers=headers)
    organise_options_from_json(json.loads(response.text))

    #Getting Electroplanet Products
    results = get_electroplanet_products()

    res_to_post_fastapi = []

    for r in results:
        tmp_d = {}
        item_options = []

        tmp_d["current_price"] = r["current_price"]
        tmp_d["category_in_store"] = r["category_in_store"]
        tmp_d["category_in_store_to_id"] = get_smartphone_category_id(r["category_in_store"])
        tmp_d["link"] = r["link"]
        tmp_d["image_url"] = r["image_url"]
        tmp_d["current_price"] = r["current_price"]
        tmp_d["name_in_store"] = r["name_in_store"]
        tmp_d["details"] = r["details"]

        id_brand = None
        id_gatantie = None
        id_color = None
        id_ram = None
        id_stockage = None
        id_connexion_adapter = None
        id_screen_size = None
        id_stockage_type = None
        id_power = None

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
        if 'mémoire_ram' in tmp_json:
            id_ram = get_item_ram_id(tmp_json["mémoire_ram"])
        if 'mémoire_vive_(ram)' in tmp_json:
            id_ram = get_item_ram_id(tmp_json["mémoire_vive_(ram)"])
        if 'mémoire_de_stockage' in tmp_json:
            id_stockage = get_item_stockage_id(tmp_json["mémoire_de_stockage"])
        if 'capacite_disque_dur_ssd' in tmp_json:
            id_stockage = get_item_stockage_id(tmp_json["capacite_disque_dur_ssd"])
        if 'reseau' in tmp_json:
            id_connexion_adapter = get_item_connexion_adapter_id(tmp_json['reseau'])
        if 'taille_d\'ecran' in tmp_json:
            id_screen_size = get_item_screen_size_id(tmp_json['taille_d\'ecran'])
        if 'longueur' in tmp_json:
            id_length = get_item_length_id(tmp_json['longueur'])
        if 'puissance' in tmp_json:
            if not 'FAST' == tmp_json['puissance']:
                id_power = get_item_power_id(tmp_json['puissance'])


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
        if id_brand != None:
            tmp_d['brand_id'] = id_brand

        tmp_d['options'] = item_options
        res_to_post_fastapi.append(tmp_d)


    # [print(i , '\n') for i in res_to_post_fastapi]
    # quit()
    print(f"len (res_to_post_fastapi) = {len(res_to_post_fastapi)}")
    return res_to_post_fastapi

