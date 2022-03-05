import json
from typing import List

from requests import Session

def fetch_brands(token:str, s:Session) -> List:
    try:
        url = f"http://localhost:9999/brands"
        headers = {'Content-Type': 'application/json','Authorization': f'Bearer {token}'}
        response = s.get(url , headers=headers)
        return json.loads(response.text)
    except:
        return []

