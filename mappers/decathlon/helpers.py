import json
import requests
from mappers.Helpers.electroplanet_helprs.generale_purposed_functions import mydb


mapper_credetials = {"username": "electroplanet_mapper", "password": "electroplanetMapperSupero2022"}
login_url = "http://localhost:9999/login"
url_post = "http://127.0.0.1:9999/products?website=decathlon"
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

def get_decathlon_products():
    mycursor = mydb.cursor()
    sql = """SELECT * FROM ITEMS WHERE id_store = 6;"""
    mycursor.execute(sql, )
    results = dictfetchall(mycursor)
    return results

def get_category_id_decathlon(cat_in_store):
    f = open('../mappeed_categories/decathlon/mapped_procuts.json')
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

