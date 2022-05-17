import json
import requests
from mappers.Helpers.electroplanet_helprs.generale_purposed_functions import mydb
from mappers.config.urls import options_url

mapper_credetials = {"username": "electroplanet_mapper", "password": "electroplanetMapperSupero2022"}
login_url = "http://localhost:9999/login"
url_post = "http://127.0.0.1:9999/products?website=ikea"
payload = json.dumps(mapper_credetials)
headers = {'Content-Type': 'application/json'}
electroplanet_colors =[]

def dictfetchall(cursor):
    """Returns all rows from a cursor as a list of dicts"""
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()]

def get_ikea_products():
    mycursor = mydb.cursor()
    sql = """
        SELECT * FROM ITEMS WHERE id_store = 7
    and (category_in_store like "Barbecues"
    or category_in_store like "Cuisine extérieure"
    or category_in_store like "Luminaires"
    or category_in_store like "Parasols"
    or category_in_store like "Caillebotis"
    or category_in_store like "Tapis d'extérieur"
    or category_in_store like "Accessoires d'extérieur"
    or category_in_store like "Pique-nique et loisirs de plein air"
    or category_in_store like "Rangements d'extérieur"
    or category_in_store like "Pots et plantes"
    or category_in_store like "Robinets mitigeurs"
    or category_in_store like "Douchess"
    or category_in_store like "Vasques & lavabos"
    or category_in_store like "Tabourets et bancs salle de bain"
    or category_in_store like "Ensemble meuble salle de bain"
    or category_in_store like "Luminaires salle de bain"
    or category_in_store like "Accessoires buanderie"
    or category_in_store like "Accessoires salle de bain"
    or category_in_store like "Miroirs salle de bain"
    or category_in_store like "Rangements salle de bain"
    or category_in_store like "Meubles vasques/lavabos"
    or category_in_store like "Parfums d'ambiance"
    or category_in_store like "Horloges"
    or category_in_store like "Décorations de Noël"
    or category_in_store like "Papeterie et fournitures de bureau"
    or category_in_store like "Accessoires décoratifs"
    or category_in_store like "Tableaux d'affichage"
    or category_in_store like "Vases et coupes"
    or category_in_store like "Bougies, photophores et bougeoirs"
    or category_in_store like "Miroirs"
    or category_in_store like "Pots, cache-pots et jardinières"
    or category_in_store like "Boîtes de rangement et paniers"
    or category_in_store like "Plantes et fleurs"
    or category_in_store like "Cadres et affiches"
    or category_in_store like "Tapis"
    or category_in_store like "Carreaux de chaise"
    or category_in_store like "Textile bébé"
    or category_in_store like "Textiles de cuisine"
    or category_in_store like "Linge de bain"
    or category_in_store like "Nappes, sets de table et carreaux de chaise"
    or category_in_store like "Coussins d'extérieur"
    or category_in_store like "Textile enfant"
    or category_in_store like "Coussins et housses de coussins"
    or category_in_store like "Rideaux, tringles et stores"
    or category_in_store like "Rangement pour documents et accessoires media"
    or category_in_store like "Chargeurs, piles et câbles"
    or category_in_store like "Lampes de bureau"
    or category_in_store like "Meubles de rangement bureau"
    or category_in_store like "Caissons à tiroirs"
    or category_in_store like "Ensembles bureau et chaise"
    or category_in_store like "Bureaux et support PC/tablettes"
    or category_in_store like "Chaises de bureau"
    or category_in_store like "Panneaux pour porte coulissante"
    or category_in_store like "Etagères murales"
    or category_in_store like "Matériel de déménagement"
    or category_in_store like "Rangements chaussures et portemanteaux"
    or category_in_store like "Crochets et rangements muraux"
    or category_in_store like "Accessoires de rangement"
    or category_in_store like "Solutions de rangement"
    or category_in_store like "Ensemble meuble chambre"
    or category_in_store like "Rangements de lit"
    or category_in_store like "Tables de chevet"
    or category_in_store like "Matelas"
    or category_in_store like "Linge de lit"
    or category_in_store like "Crédences et revêtements muraux"
    or category_in_store like "Mitigeurs et éviers"
    or category_in_store like "Éclairage intégré cuisine"
    or category_in_store like "Boutons et poignées"
    or category_in_store like "Plans de travail"
    or category_in_store like "Rangements muraux"
    or category_in_store like "Etagères et crémaillères"
    or category_in_store like "Aménagements intérieurs et tri des déchets"
    or category_in_store like "Solutions cuisine"
    or category_in_store like "Meubles de cuisine"
    or category_in_store like "Portes et façades de tiroirs"
    or category_in_store like "Meubles bébé"
    or category_in_store like "Mobilier de café et restaurant"
    or category_in_store like "Fauteuils et méridiennes"
    or category_in_store like "Tables et chaises de bar"
    or category_in_store like "Dessertes et îlots"
    or category_in_store like "Séparateurs de pièce"
    or category_in_store like "Meubles enfant"
    or category_in_store like "Buffets et consoles"
    or category_in_store like "Mobilier de jardin"
    or category_in_store like "Chaises"
    or category_in_store like "Armoires, penderies et dressings"
    or category_in_store like "Commodes et caissons à tiroirs"
    or category_in_store like "Meubles TV"
    or category_in_store like "Rangements bureau et salon"
    or category_in_store like "Bibliothèques et étagères"
    or category_in_store like "Canapés"
    or category_in_store like "Lits"
    or category_in_store like "Meubles de gaming"
    );
    """
    mycursor.execute(sql, )
    results = dictfetchall(mycursor)
    return results



def get_category_id_ikea(cat_in_store):
    f = open('../mappeed_categories/ikea/mapped_prods.json')
    data = json.load(f)
    f.close()

    for c in data:
        tmp =cat_in_store.replace('è' , 'e')
        tmp =tmp.replace('é' , 'e')
        tmp = tmp.replace('à' , 'a')
        tmp = tmp.replace('â' , 'a')
        tmp = tmp.replace('É' , 'E')
        tmp = tmp.replace('ê' , 'e')
        tmp = tmp.replace('ë' , 'e')
        tmp = tmp.replace('ç' , 'c')
        tmp = tmp.replace('î' , 'i')
        tmp = tmp.replace('ï' , 'i')
        if tmp in c.keys():
            prod_cat = c[str(tmp)]
            break
    else:
        if cat_in_store == 'Protection Solaire':
            return '389'
        prod_cat= '311'
        print(f'311 FOR: {cat_in_store}')
    return prod_cat


def get_item_color_id(color:str):
    for c in electroplanet_colors:
        if  c["value"].lower() in color:
            return c['id']
    print(f'NEW COLOR {color}')
    return None


def get_options_from_api(token):
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
    r = requests.get(options_url, headers=headers)
    all_options = json.loads(r.text)

    for o in all_options:
        if o["id_parent"] == 1:
            electroplanet_colors.append(o)


def post_list_of_product(res_to_post_fastapi, token):
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
    payload = json.dumps(res_to_post_fastapi)
    response = requests.request("POST", url_post, headers=headers, data=payload)
    print(response.text)
    print(f"response.elapsed.total_seconds() = {response.elapsed.total_seconds()}")
