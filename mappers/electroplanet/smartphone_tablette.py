import pymysql
from requests import Session
from mappers.Helpers.electroplanet import *


def get_mapped_prod_names(mycursor) -> List:
    l = []
    sql = "select frome_to from mapped_prod_names"
    mycursor.execute(sql,)
    [l.append(i[0]) for i in mycursor.fetchall()]
    return l

def prod_names_reducer(mycursor):
    l = []
    list_reducers = []
    sql = """
        SELECT distinct name_in_store FROM ITEMS WHERE id_store = 3
        and (category_in_store like 'iphone'
        or category_in_store like 'telephone-android'
        or category_in_store like 'ipad'
        or category_in_store like 'tablettes-android'
        or category_in_store like 'Domestique'
        or category_in_store like 'Mobile'
        or category_in_store like 'Cover de protection'
        or category_in_store like 'Oreillettes bluetooth'
        or category_in_store like 'Perche selfie filaire'
        or category_in_store like 'Selfie sans fil'
        or category_in_store like 'Macbook'
        or category_in_store like 'Chargeur'
        or category_in_store like 'Tablettes cover de protection'
        or category_in_store like 'Tablettes support voiture'
        or category_in_store like 'Adaptateurs telephone tablette'
        or category_in_store like 'Cablage'
        );
        """
    mycursor.execute(sql,)
    [l.append(i[0]) for i in mycursor.fetchall()]
    list_mapped_prod_names = get_mapped_prod_names(mycursor)
    l.sort(key=len)

    for i in list_mapped_prod_names:
        for j in l:
            if i.lower() in j.lower().replace(',' , '.'):
                if not key_exists_in_list_of_dicts(list_reducers, j):
                    reducer = {}
                    reducer[f'{j}'] = i
                    list_reducers.append(reducer)
                    continue
            if 'CHARGEUR' in j or 'CABLE' in j:
                reducer = {}
                reducer[f'{j}'] = 'Cable Chargeur'
                list_reducers.append(reducer)
                continue

    no_names_products = []
    for j in l:
        if not key_exists_in_list_of_dicts(list_reducers, j):
            no_names_products.append(j)
    [print(x) for x in no_names_products]
    print(f'len = {len(no_names_products)}')
    return list_reducers

def key_exists_in_list_of_dicts(l : List , k : str) -> bool:
    for d in l:
        if k in d:
            return True
    return False


def smartphones_tablette(token:str , s:Session , brands : List) -> List:
    url = "http://127.0.0.1:9999/options?website=electroplanet-iphone"
    headers = {'Content-Type': 'application/json','Authorization': f'Bearer {token}'}
    response = s.get(url , headers=headers)
    tmp = json.loads(response.text)

    mydb = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="supero_datalake2",)
    mycursor = mydb.cursor()
    sql = """
    SELECT * FROM ITEMS WHERE id_store = 3
    and (category_in_store like 'iphone'
    or category_in_store like 'telephone-android'
    or category_in_store like 'ipad'
    or category_in_store like 'tablettes-android'
    or category_in_store like 'Domestique'
    or category_in_store like 'Mobile'
    or category_in_store like 'Cover de protection'
    or category_in_store like 'Oreillettes bluetooth'
    or category_in_store like 'Perche selfie filaire'
    or category_in_store like 'Selfie sans fil'
    or category_in_store like 'Macbook'
    or category_in_store like 'Chargeur'
    or category_in_store like 'Tablettes cover de protection'
    or category_in_store like 'Tablettes support voiture'
    or category_in_store like 'Adaptateurs telephone tablette'
    or category_in_store like 'Cablage'
    );
    """

    mycursor.execute(sql,)
    results = dictfetchall(mycursor)

    x = prod_names_reducer(mycursor)
    print('\n\n')
    [ print(xx) for xx in x ]
    quit()

    for t in tmp:
        if t['id_parent'] == 1:
            electroplanet_colors.append(t)
            continue
        if t['id_parent'] == 2:
            electroplanet_storage.append(t)
            continue
        if t['id_parent'] == 3:
            electroplanet_ram.append(t)
            continue
        if t['id_parent'] == 5:
            electroplanet_taille_ecrant.append(t)
            continue
        if t['id_parent'] == 6:
            electroplanet_type_hd.append(t)
            continue
        if t['id_parent'] == 143:
            electroplanet_garanties.append(t)
            continue
        if t['id_parent'] == 152:
            electroplanet_connector_adapter.append(t)
            continue
        if t['id_parent'] == 187:
            electroplanet_type_stockage.append(t)
            continue
        if t['id_parent'] == 4:
            electroplanet_lenght.append(t)
            continue
        if t['id_parent'] == 156:
            electroplanet_power.append(t)
            continue

    for r in results:
        tmp_d = {}
        item_options = []
        tmp_d["current_price"] = r["current_price"]
        tmp_d["category_in_store"] = r["category_in_store"]
        tmp_d["category_id"] =get_category_id(r["category_in_store"])
        tmp_d["link"] = r["link"]
        tmp_d["prod_name"] = r["prod_name"]
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
        id_length = None
        id_power = None

        tmp_specification_json = json.loads(r["specification"])
        try:
            tmp_json = extract_specification_json(tmp_specification_json['specification_table'])
        except Exception as e:
            continue

        if 'marque' in  tmp_json:
            id_brand = get_brand_id(brands, tmp_json['marque'])
        if 'couleur' in tmp_json:
            id_color = get_item_color_id(tmp_json["couleur"])
        if 'coloris' in tmp_json:
            id_color = get_item_color_id(tmp_json["coloris"])
        if 'garantie' in tmp_json:
            id_gatantie = get_item_garantie_id(tmp_json["garantie"])
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
            tmp_d['id_brand'] = id_brand

        tmp_d['options'] = item_options
        res_to_post_fastapi.append(tmp_d)


    [print(i) for i in res_to_post_fastapi]
    print(f"len (res_to_post_fastapi) = {len(res_to_post_fastapi)}")
    return res_to_post_fastapi
