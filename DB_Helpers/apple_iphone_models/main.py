import requests
from bs4 import BeautifulSoup as BS

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-language': 'en-US,en;q=0.9',
    'DNT': '1',
    'Referer': 'https://google.com'
}


# def remove_text_between_prentessies(txt : str):
#     start = txt.find("(")
#     end = txt.find(")")
#     if start != -1 and end != -1:
#         return txt[start + 1:end]
#     else:
#         return txt
#
#
# s = requests.session()
# res = s.get('https://support.apple.com/en-us/HT201296' , headers=headers)
# soup = BS(res.text , features="html.parser")
#
# h2_tags = soup.findAll('h2')
#
# [print(remove_text_between_prentessies( h.get_text())) for h in h2_tags]


l = [
'iPhone 13 Pro Max',
'iPhone 13 Pro',
'iPhone 13',
'iPhone 13 mini',
'iPhone 12 Pro Max',
'iPhone 12 Pro',
'iPhone 12',
'iPhone 12 mini',
'iPhone 11 Pro',
'iPhone 11 Pro Max',
'iPhone 11',
'iPhone XS',
'iPhone XS Max',
'iPhone XR',
'iPhone X',
'iPhone 8',
'iPhone 8 Plus',
'iPhone 7',
'iPhone 7 Plus',
'iPhone 6s',
'iPhone 6s Plus',
'iPhone 6',
'iPhone 6 Plus',
'iPhone 5s',
'iPhone 5c',
'iPhone 5',
'iPhone 4s',
'iPhone 4',
'iPhone 3GS',
'iPhone 3G'
]

def Sorting(lst):
    lst.sort(key=len)
    return lst


for i in Sorting(l):
    print(f'insert into mapped_prod_names(name) values(\"{i}\");')