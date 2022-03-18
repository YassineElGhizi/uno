from mappers.electroplanet.smartphone_tablette import smartphones_tablette
import requests
import json
from mappers.electroplanet.fetch_api import fetch_brands

mapper_credetials = {"username": "electroplanet_mapper", "password": "electroplanetMapperSupero2022"}
login_url = "http://localhost:9999/login"
payload = json.dumps(mapper_credetials)
headers = {'Content-Type': 'application/json'}

if __name__ == '__main__':
    print("[+] preparing to get token")
    s = requests.session()
    response = s.post(login_url, headers=headers, data=payload)
    if response.status_code == 401:
        print("[-] err 401 : Invalid username and/or password")
        quit()
    print("[+] token recieved with success")
    token = json.loads(response.text)['token']
    smartphones_tablette(token, s, fetch_brands(token, 'electroplanet_smartphones_tablette' , s))