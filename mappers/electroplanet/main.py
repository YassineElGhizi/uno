import requests
import json

from mappers.electroplanet.smartphone_tablette import smartphones_tablette
from mappers.electroplanet.beaute_sante import beaute_sante
from mappers.electroplanet.small_electromenager import small_electromenager
from mappers.electroplanet.tv import tv

from mappers.electroplanet.fetch_api import fetch_brands
from mappers.electroplanet.big_electromenager import big_electromenager
from mappers.Helpers.generale_purposed_functions import get_jwt_token_or_fail
from mappers.Helpers.electroplanet import get_options_from_api
from mappers.Helpers.fetch_from_local import get_mapped_procuts


mapper_credetials = {"username": "electroplanet_mapper", "password": "electroplanetMapperSupero2022"}
login_url = "http://localhost:9999/login"
url_post = "http://127.0.0.1:9999/products?website=electroplanet"
payload = json.dumps(mapper_credetials)
headers = {'Content-Type': 'application/json'}

#to avoid memory leaks
product_names = []
#Fetching Products
list_of_mapped_product_names = get_mapped_procuts()

def post_list_of_product(res_to_post_fastapi, token):
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
    payload = json.dumps(res_to_post_fastapi)
    response = requests.request("POST", url_post, headers=headers, data=payload)
    print(response.text)
    print(f"response.elapsed.total_seconds() = {response.elapsed.total_seconds()}")

if __name__ == '__main__':
    print("[+] preparing to get token")
    s = requests.session()
    token = get_jwt_token_or_fail(s, login_url, headers, payload)

    print("[+] getting options from API")
    get_options_from_api(token)
    print("[+] getting product namres from API")

    # print('\t=> Starting : smartphones_tablette()')
    # listof_products = smartphones_tablette(token,s,fetch_brands(token, 'electroplanet_smartphones_tablette' , s) , list_of_mapped_product_names)
    # post_list_of_product(listof_products, token)
    #
    # print('\t=> Starting : beaute_sante()')
    # listof_products = beaute_sante(fetch_brands(token, 'electroplanet_smartphones_tablette' , s))
    # post_list_of_product(listof_products, token)
    #
    # print('\t=> Starting : small_electromenager()')
    # listof_products = small_electromenager(fetch_brands(token, 'electroplanet_smartphones_tablette' , s))
    # post_list_of_product(listof_products, token)
    #
    # print('\t=> Starting : big_electromenager()')
    # listof_products = big_electromenager(fetch_brands(token, 'electroplanet_smartphones_tablette' , s))
    # post_list_of_product(listof_products, token)


    listof_products = tv(fetch_brands(token, 'electroplanet_smartphones_tablette' , s))
    # post_list_of_product(listof_products, token)

