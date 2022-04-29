import json
import requests
from mappers.Helpers.uno import uno_colors, uno_storage, uno_ram, uno_taille_ecrant, uno_type_hd,uno_connector_adapter, uno_type_stockage,uno_power, uno_lenght


def get_product_name_from_product_title(prod_title, list_of_prod_names) -> str:
    for i in list_of_prod_names:
        if i.lower() in prod_title[0].lower():
            return i
    else:
        return prod_title[1]

def organise_options_from_json(json):
    for j in json:
        if j["id_parent"] == 1:
            uno_colors.append(j)
        if j["id_parent"] == 2:
            uno_storage.append(j)
        if j["id_parent"] == 3:
            uno_ram.append(j)
        if j["id_parent"] == 5:
            uno_taille_ecrant.append(j)
        if j["id_parent"] == 6:
            uno_type_hd.append(j)
        if j["id_parent"] == 152:
            uno_connector_adapter.append(j)
        if j["id_parent"] == 187:
            uno_type_stockage.append(j)
        if j["id_parent"] == 156:
            uno_power.append(j)
        if j["id_parent"] == 4:
            uno_lenght.append(j)


def get_jwt_token_or_fail(session, login_url, headers,payload):
    response = session.post(login_url, headers=headers, data=payload)
    if response.status_code == 401:
        print("[-] err 401 : Invalid username and/or password")
        quit()
    print("[+] token recieved with success")
    return json.loads(response.text)['token']


def get_product_names(session, prodcut_url, headers, payload):
    response = session.post(prodcut_url, headers=headers, data=payload)
    return json.loads(response.text)['token']





