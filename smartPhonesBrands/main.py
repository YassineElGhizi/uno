import requests
from bs4 import BeautifulSoup

res = requests.get('https://gadgets360.com/mobiles/all-brands')

soup = BeautifulSoup(res.text, features="html.parser")


brand_cards = soup.findAll('h3')

for a in brand_cards:
    try:
        if 'Mobile Phones' in a.get_text():
            print(
                f"insert into brands(names, Specialite, description, logo) values ('{a.get_text().replace('Mobile Phones' , '').strip()}' , '[\"5\"]' , '' , '');"
            )
    except:
        pass

