from typing import List
import json
from bs4 import BeautifulSoup as BS
import requests

from mappers.Helpers.electroplanet_helprs.generale_purposed_functions import mydb
from mappers.Helpers.electroplanet import get_brand_id, get_options_from_api
from mappers.electroplanet.fetch_api import fetch_brands
from mappers.Helpers.generale_purposed_functions import get_jwt_token_or_fail
from mappers.Helpers.electroplanet import get_item_color_id


mapper_credetials = {"username": "electroplanet_mapper", "password": "electroplanetMapperSupero2022"}
login_url = "http://localhost:9999/login"
url_post = "http://127.0.0.1:9999/products?website=kitea"
payload = json.dumps(mapper_credetials)
headers = {'Content-Type': 'application/json'}

def post_list_of_product(res_to_post_fastapi, token):
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
    payload = json.dumps(res_to_post_fastapi)
    response = requests.request("POST", url_post, headers=headers, data=payload)
    print(response.text)
    print(f"response.elapsed.total_seconds() = {response.elapsed.total_seconds()}")


def dictfetchall(cursor):
    """Returns all rows from a cursor as a list of dicts"""
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()]

def get_kitea_products():
    mycursor = mydb.cursor()
    sql = """SELECT * FROM ITEMS WHERE id_store = 4;"""
    mycursor.execute(sql, )
    results = dictfetchall(mycursor)
    return results

def get_category_id_kitea(cat_in_store):
    f = open('../mappeed_categories/kitea/mapped_prods.json')
    data = json.load(f)
    f.close()

    for c in data:
        tmp =cat_in_store.replace('è' , 'e')
        tmp =tmp.replace('é' , 'e')
        tmp = tmp.replace('à' , 'a')
        if tmp in c.keys():
            prod_cat = c[str(tmp)]
            break
    else:
        prod_cat= '311'
    return prod_cat


def extract_specification_json_kitea(html_table : str) -> dict:
    soup = BS(html_table , features="html.parser")
    d = {}
    for tag in soup.find_all('li'):
        try:
            d[tag.find('p').get_text()] = tag.find('span').get_text()
        except:
            pass
    return d

def main(brands : List) -> List:
    #Getting Electroplanet Products
    results = get_kitea_products()
    res_to_post_fastapi = []

    for r in results:
        tmp_d = {}
        item_options = []

        tmp_d["current_price"] = r["current_price"]
        tmp_d["category_in_store"] = r["category_in_store"]
        tmp_d["category_in_store_to_id"] = get_category_id_kitea(r["category_in_store"])
        tmp_d["link"] = r["link"]
        tmp_d["image_url"] = r["image_url"]
        tmp_d["current_price"] = r["current_price"]
        tmp_d["name_in_store"] = r["name_in_store"]
        tmp_d["prod_name"] = r ["prod_name"]
        tmp_d["details"] = r["details"]

        tmp_specification_json = json.loads(r["specification"])

        try:
            tmp_json = extract_specification_json_kitea(tmp_specification_json['specification_table'])
        except Exception as e:
            continue

        id_brand = None
        if 'marque' in tmp_json:
            id_brand = get_brand_id(brands, tmp_json['marque'])
        if id_brand != None:
            tmp_d['brand_id'] = id_brand
        if 'Coloris' in tmp_json:
            id_color = get_item_color_id(tmp_json["Coloris"])
        if 'Famille de couleurs' in tmp_json:
            id_color = get_item_color_id(tmp_json["Famille de couleurs"])

        if id_color != None:
            tmp_d['id_color'] = id_color
            item_options.append(id_color)
        # if id_brand != None:
        #     tmp_d['brand_id'] = id_brand
        # else:
        #     tmp_d['brand_id'] = None

        tmp_d['brand_id'] = None
        tmp_d['options'] = item_options
        res_to_post_fastapi.append(tmp_d)


    # [print(i , '\n') for i in res_to_post_fastapi]
    # quit()
    print(f"len (res_to_post_fastapi) = {len(res_to_post_fastapi)}")
    return res_to_post_fastapi



if __name__ == "__main__":
    print("[+] preparing to get token")
    s = requests.session()
    token = get_jwt_token_or_fail(s, login_url, headers, payload)

    print("[+] getting options from API")
    get_options_from_api(token)

    listof_products = main(fetch_brands(token, 'electroplanet_smartphones_tablette' , s))
    post_list_of_product(listof_products, token)