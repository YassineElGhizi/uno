import json
import pymysql

from mappers.Helpers.electroplanet import electroplanet_colors,electroplanet_storage,electroplanet_ram,electroplanet_taille_ecrant,electroplanet_type_hd,electroplanet_connector_adapter,electroplanet_type_stockage,electroplanet_power,electroplanet_lenght


mydb = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="supero_datalake2",)

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

def get_electroplanet_beaute_sante():
    mycursor = mydb.cursor()
    sql = """
        SELECT * FROM ITEMS WHERE id_store = 3
    and (category_in_store like 'Pack Beaute'
    or category_in_store like 'Brosse soufflante'
    or category_in_store like 'Fer à coiffer'
    or category_in_store like 'Lisseur'
    or category_in_store like 'Seche cheveux'
    or category_in_store like 'Rasoir'
    or category_in_store like 'Tondeuse'
    or category_in_store like 'Appareil anti cellulite'
    or category_in_store like 'Brosse nettoyante visage'
    or category_in_store like 'Epilateur'
    or category_in_store like 'Lumiere pulsee'
    );
    """
    mycursor.execute(sql,)
    results = dictfetchall(mycursor)
    return results


def get_electroplanet_small_electromenager():
    mycursor = mydb.cursor()
    sql = """
        SELECT distinct * FROM ITEMS WHERE id_store = 3
    and (
    category_in_store like 'Batteur'
    or category_in_store like 'Blender'
    or category_in_store like 'Hache viande'
    or category_in_store like 'Hachoir'
    or category_in_store like 'Kitchen machine'
    or category_in_store like 'Mixeur plongeant'
    or category_in_store like 'Moulinette'
    or category_in_store like 'Robot de cuisine'
    or category_in_store like 'Sorbetière'
    or category_in_store like 'Bouilloire'
    or category_in_store like 'Centrifugeuse'
    or category_in_store like 'Extracteur de jus'
    or category_in_store like 'Grill pain - toaster'
    or category_in_store like 'Presse-agrumes'
    or category_in_store like 'Grill pain - Presse-agrumes'
    or category_in_store like 'Set petit déjeuner'
    or category_in_store like 'Cafetiere classique'
    or category_in_store like 'Expresso a capsule'
    or category_in_store like 'Expresso avec broyeur a cafe'
    or category_in_store like 'Machine a cafe pression'
    or category_in_store like 'Moulin a cafe'
    or category_in_store like 'Appareil à croque monsieur'
    or category_in_store like 'Gaufrier'
    or category_in_store like 'Grill à panini'
    or category_in_store like 'Grill pain - toaster'
    or category_in_store like 'Grill pain - Presse-agrumes'
    or category_in_store like 'Grill à viande'
    or category_in_store like 'Machine a pop corn'
    or category_in_store like 'Friteuse classique'
    or category_in_store like 'Friteuse sans huile'
    or category_in_store like 'Pack preparation culinaire'
    or category_in_store like 'Four posable'
    or category_in_store like 'Micro-ondes'
    or category_in_store like 'Aspirateur'
    or category_in_store like 'Aspirette'
    or category_in_store like 'Nettoyeur a vapeur'
    or category_in_store like 'Housse table a repasser'
    or category_in_store like 'Planches a repasser'
    or category_in_store like 'Centrale vapeur'
    or category_in_store like 'Fer a repasser'
    );
    """
    mycursor.execute(sql,)
    results = dictfetchall(mycursor)
    return results


def get_category_id(cat_in_store):
    f = open('../mappeed_categories/tv.json')
    data = json.load(f)
    f.close()

    for c in data:
        if cat_in_store in c.keys():
            prod_cat = c[str(cat_in_store)]
            break
    else:
        prod_cat= '311'
    return prod_cat

def get_smartphone_category_id(cat_in_store):
    f = open('../mappeed_categories/electro_mapped_cats.json')
    data = json.load(f)
    f.close()

    for c in data:
        if cat_in_store in c.keys():
            prod_cat = c[str(cat_in_store)]
            break
    else:
        prod_cat= '311'
    return prod_cat

def get_informatique_category_id(cat_in_store):
    f = open('../mappeed_categories/informatique.json')
    data = json.load(f)
    f.close()

    for c in data:
        if cat_in_store in c.keys():
            prod_cat = c[str(cat_in_store)]
            break
    else:
        prod_cat= '311'
    return prod_cat



def get_category_id_beaute_sante(cat_in_store):
    f = open('../mappeed_categories/Beaute_sante.json')
    data = json.load(f)
    f.close()

    for c in data:
        if cat_in_store in c.keys():
            prod_cat = c[str(cat_in_store)]
            break
    else:
        prod_cat= '311'

    return prod_cat


def get_category_id_small_electromenager(cat_in_store):
    # NB PATH IS RELATIVE TO MAIN
    f = open('../mappeed_categories/small_electromenager.json')
    data = json.load(f)
    f.close()

    for c in data:
        if cat_in_store in c.keys():
            prod_cat = c[str(cat_in_store)]
            break
    else:
        prod_cat= '311'

    return prod_cat

def get_category_id_maison_et_cuisine(cat_in_store):
    # NB PATH IS RELATIVE TO MAIN
    f = open('../mappeed_categories/maison_et_cuisine.json')
    data = json.load(f)
    f.close()

    for c in data:
        if cat_in_store in c.keys():
            prod_cat = c[str(cat_in_store)]
            break
    else:
        prod_cat= '311'

    return prod_cat

def get_category_id_big_electromenager(cat_in_store):
    # NB PATH IS RELATIVE TO MAIN
    f = open('../mappeed_categories/big_electromenager.json')
    data = json.load(f)
    f.close()

    for c in data:
        if cat_in_store in c.keys():
            prod_cat = c[str(cat_in_store)]
            break
    else:
        prod_cat= '311'

    return prod_cat



def get_electroplanet_big_electromenager():
    mycursor = mydb.cursor()
    sql = """
        SELECT distinct * FROM ITEMS WHERE id_store = 3
    and (
    category_in_store like 'Batteur"Mini bar'
    or category_in_store like 'Petit Refrigerateur'
    or category_in_store like 'Refrigerateur americain duo jumelable'
    or category_in_store like 'Refrigerateur americain side by side'
    or category_in_store like 'Refrigerateur avec congelateur en bas'
    or category_in_store like 'Refrigerateur avec congelateur en haut'
    or category_in_store like 'Cuisiniere 4 feux'
    or category_in_store like 'Cuisiniere 5 feux'
    or category_in_store like 'Cuisiniere 5 feux cache bouteille'
    or category_in_store like 'Lave-vaisselle encastrable'
    or category_in_store like 'Machine à laver encastrable'
    or category_in_store like 'Plaque de cuisson a gaz'
    or category_in_store like 'Plaque de cuisson electrique'
    or category_in_store like 'Machine a laver a hublot'
    or category_in_store like 'Machine a laver ouverture en haut'
    or category_in_store like 'machine a laver sechante'
    or category_in_store like 'Machine a laver semi automatique avec essorage'
    or category_in_store like 'Machine a laver semi automatique sans essorage'
    or category_in_store like 'Lave vaisselle pose libre'
    or category_in_store like 'Climatiseur'
    );
    """
    mycursor.execute(sql,)
    results = dictfetchall(mycursor)
    return results


def get_tv():
    mycursor = mydb.cursor()
    sql = """
           SELECT distinct * FROM ITEMS WHERE id_store = 3
       and (
       category_in_store like 'Televiseur'
       or category_in_store like 'Smart tv'
       or category_in_store like 'Televiseurs 4k uhd'
       or category_in_store like 'Televiseurs premium 4k uhd'
       or category_in_store like 'Oled'
       or category_in_store like 'Oanocell'
       or category_in_store like 'Support TV'
       or category_in_store like 'Demodulateurs et recepteurs tnt'
       );
       """
    mycursor.execute(sql, )
    results = dictfetchall(mycursor)
    return results


def get_assecoire_tv():
    mycursor = mydb.cursor()
    sql = """
           SELECT distinct * FROM ITEMS WHERE id_store = 3
       and (
       category_in_store like 'Televiseur'
       or category_in_store like 'Smart tv'
       or category_in_store like 'Televiseurs 4k uhd'
       or category_in_store like 'Televiseurs premium 4k uhd'
       or category_in_store like 'Oled'
       or category_in_store like 'Oanocell'
       );
       """
    mycursor.execute(sql, )
    results = dictfetchall(mycursor)
    return results


def get_electroplanet_appareil_photo():
    mycursor = mydb.cursor()
    sql = """
               SELECT distinct * FROM ITEMS WHERE id_store = 3
           and (
           category_in_store like 'Appareil photo bridge'
           or category_in_store like 'Appareil photo compact'
           or category_in_store like 'Appareil photo instantane'
           or category_in_store like 'Appareil photo reflex'
           );
           """
    mycursor.execute(sql, )
    results = dictfetchall(mycursor)
    return results


def get_category_id_appareil_photo(cat_in_store):
    f = open('../mappeed_categories/appareil_photo.json')
    data = json.load(f)
    f.close()

    for c in data:
        if cat_in_store in c.keys():
            prod_cat = c[str(cat_in_store)]
            break
    else:
        prod_cat = '311'

    return prod_cat


def get_electroplanet_audio():
    mycursor = mydb.cursor()
    sql = """
               SELECT distinct * FROM ITEMS WHERE id_store = 3
           and (
           category_in_store like 'Haut parleurs et enceintes'
           or category_in_store like 'casque audio avec micro'
           or category_in_store like 'casque audio avec micro sans fil'
           or category_in_store like 'Ecouteurs avec micro'
           or category_in_store like 'Ecouteurs avec micro sans fil'
           or category_in_store like 'Ecouteurs sportifs avec micro sans fil'
           or category_in_store like 'Ecouteurs sportifs avec micro'
           or category_in_store like 'Casques gamers'
           );
           """
    mycursor.execute(sql, )
    results = dictfetchall(mycursor)
    return results

def get_category_id_audio(cat_in_store):
    f = open('../mappeed_categories/audio.json')
    data = json.load(f)
    f.close()

    for c in data:
        if cat_in_store in c.keys():
            prod_cat = c[str(cat_in_store)]
            break
    else:
        prod_cat = '311'

    return prod_cat


def get_electro_informartique_products():
    mycursor = mydb.cursor()
    sql = """
           SELECT distinct * FROM ITEMS WHERE id_store = 3
           and (
           category_in_store like 'netbook'
           or category_in_store like 'Notebook'
           or category_in_store like 'Pc gamer'
           or category_in_store like 'Ultrabook'
           or category_in_store like 'Desktop Gamer'
           or category_in_store like 'Pc gamer'
           or category_in_store like 'Ecran pour pc'
           or category_in_store like 'Imac'
           or category_in_store like 'All in one'
           or category_in_store like 'Imprimante jet d encre'
           or category_in_store like 'Imprimante laser'
           or category_in_store like 'Claviers'
           or category_in_store like 'Souris gamers'
           or category_in_store like 'Souris'
           or category_in_store like 'Support ventilateur pc'
           or category_in_store like 'Webcam'
           );
               """
    mycursor.execute(sql, )
    results = dictfetchall(mycursor)
    return results

def get_electroplanet_maison_et_cuisine():
    mycursor = mydb.cursor()
    sql = """
           SELECT distinct * FROM ITEMS WHERE id_store = 3
           and (
           category_in_store like 'Ustensiles de cuisine'
           or category_in_store like 'Cafetieres'
           );
               """
    mycursor.execute(sql, )
    results = dictfetchall(mycursor)
    return results