import json
import pymysql

from mappers.Helpers.electroplanet import electroplanet_colors,electroplanet_storage,electroplanet_ram,electroplanet_taille_ecrant,electroplanet_type_hd,electroplanet_connector_adapter,electroplanet_type_stockage,electroplanet_power,electroplanet_lenght


def get_product_name_from_product_title(prod_title, list_of_prod_names) -> str:
    for i in list_of_prod_names:
        if i.lower() in prod_title[0].lower():
            return i
    else:
        return prod_title[1]

def organise_options_from_json(json):
    for j in json:
        if j["id_parent"] == 1:
            electroplanet_colors.append(j)
        if j["id_parent"] == 2:
            electroplanet_storage.append(j)
        if j["id_parent"] == 3:
            electroplanet_ram.append(j)
        if j["id_parent"] == 5:
            electroplanet_taille_ecrant.append(j)
        if j["id_parent"] == 6:
            electroplanet_type_hd.append(j)
        if j["id_parent"] == 152:
            electroplanet_connector_adapter.append(j)
        if j["id_parent"] == 187:
            electroplanet_type_stockage.append(j)
        if j["id_parent"] == 156:
            electroplanet_power.append(j)
        if j["id_parent"] == 4:
            electroplanet_lenght.append(j)

def get_jwt_token_or_fail(session, login_url, headers,payload):
    response = session.post(login_url, headers=headers, data=payload)
    if response.status_code == 401:
        print("[-] err 401 : Invalid username and/or password")
        quit()
    print("[+] token recieved with success")
    return json.loads(response.text)['token']

def dictfetchall(cursor):
    """Returns all rows from a cursor as a list of dicts"""
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()]

def get_electroplanet_products():
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
    return results


def get_category_id(cat_in_store):
    # NB PATH IS RELATIVE TO MAIN
    f = open('../Helpers/electroplanet_helprs/electro_mapped_cats.json')
    data = json.load(f)
    f.close()

    prod_cat={}
    for c in data:
        if cat_in_store in c.keys():
            prod_cat = c[str(cat_in_store)]
            break
    else:
        prod_cat= '311'

    return prod_cat
