import requests
import json

from mappers.electroplanet.smartphone_tablette import smartphones_tablette
from mappers.electroplanet.fetch_api import fetch_brands
from mappers.Helpers.generale_purposed_functions import get_jwt_token_or_fail
from mappers.Helpers.electroplanet import get_options_from_api

from mappers.Helpers.fetch_from_local import get_mapped_procuts


mapper_credetials = {"username": "electroplanet_mapper", "password": "electroplanetMapperSupero2022"}
login_url = "http://localhost:9999/login"
payload = json.dumps(mapper_credetials)
headers = {'Content-Type': 'application/json'}

#Fetching Products
list_of_mapped_product_names = get_mapped_procuts()

if __name__ == '__main__':
    print("[+] preparing to get token")
    s = requests.session()
    token = get_jwt_token_or_fail(s, login_url, headers, payload)

    print("[+] getting options from API")
    get_options_from_api(token)

    smartphones_tablette(token,s,fetch_brands(token, 'electroplanet_smartphones_tablette' , s))