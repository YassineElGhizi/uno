from typing import List
import requests
from mappers.ikea.helpers import post_list_of_product,get_ikea_products, login_url, headers, payload, get_category_id_ikea, get_item_color_id, get_options_from_api
from mappers.Helpers.generale_purposed_functions import get_jwt_token_or_fail

def main() -> List:
    results = get_ikea_products()
    res_to_post_fastapi = []

    for r in results:
        tmp_d = {}
        item_options = []

        tmp_d["current_price"] = r["current_price"]
        tmp_d["category_in_store"] = r["category_in_store"]
        tmp_d["category_in_store_to_id"] = get_category_id_ikea(r["category_in_store"])
        tmp_d["link"] = r["link"]
        tmp_d["image_url"] = r["image_url"]
        tmp_d["current_price"] = r["current_price"]
        tmp_d["prod_name"] = r["name_in_store"].split(',')[0]
        tmp_d["name_in_store"] = r["name_in_store"]
        tmp_d["details"] = r["details"]

        tmp_d["brand_id"] = 507


        id_color = get_item_color_id(r["name_in_store"])
        if id_color != None:
            item_options.append(id_color)


        tmp_d['options'] = item_options
        res_to_post_fastapi.append(tmp_d)

    # [print(i , '\n') for i in res_to_post_fastapi]
    print(f"len (res_to_post_fastapi) = {len(res_to_post_fastapi)}")
    # quit()
    return res_to_post_fastapi


if __name__ == "__main__":
    print("[+] preparing to get token")
    s = requests.session()
    token = get_jwt_token_or_fail(s, login_url, headers, payload)

    print("[+] getting options from API")
    get_options_from_api(token)

    listof_products = main()
    post_list_of_product(listof_products, token)

