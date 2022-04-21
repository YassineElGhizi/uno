import requests
from bs4 import BeautifulSoup as BS
import re

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

# s = requests.session()
# res = s.get('https://www.techradar.com/news/top-portable-chargers' , headers=headers)
# soup = BS(res.text , features="html.parser")
#
# h3_tags = soup.findAll('h3')

# [print(  re.sub(r'[~^0-9]', '', (h.get_text()).lower().replace('power bank' , '')[3::])   ) for h in h3_tags]

#
# l= [
#     'imuto ,mah ',
#     'anker powercore ,mah ',
#     'mophie powerstation wireless xl ,mah ',
#     'mophie powerstation plus xl ,mah ',
#     'veho pebble p pro ,mah ',
#     'omars mini  ,mah battery',
#     'anker astro e ,mah ',
#     'mophie powerstation mini universal battery',
#     'eafu ',
#     'jvgoal s mah',
#     'anker powercore  ',
#     'okzu ,mah battery pack',
#     'maxoak ,mah ',
#     'charmast ,mah ',
#     'yobon ,mah ',
#     'jiga ,mah ',
#     'bextoo  ,mah',
#     'poweroak , mah ',
#     'belkin ,mah ',
#     'iniu  ',
#     'anker  powercore slim ,mah',
#     'anker  ,',
#     'tntor ,mah ',
#     'babaka ,mah ',
#     'mophie powerstation all-in-one ,mah ',
#     'anker magnetic wireless ,mah ',
#     'charmast wireless ',
#     'iwalk magnetic wireless ',
#     'magsafe battery pack',
#     'anker powercore iii wireless ',
#     'kilponen solar , mah',
#     'pxwaxpy solar  mah',
#     'a addtop solar charger ,mah ',
#     'hiluckey wireless solar charger',
#     'djroll ,mah ',
#     'anker powercore solar ,mah',
# ]
#
#
#
# [print( (i.replace(',mah' , '').strip())) for i in l]


l=[
'imuto',
'anker powercore',
'mophie powerstation',
'veho pebble',
'omars mini',
'anker astro e',
'eafu',
'jvgoal',
'okzu',
'maxoak',
'charmast',
'yobon',
'jiga',
'bextoo',
'poweroak',
'belkin',
'iniu',
'tntor',
'babaka',
'iwalk',
'magsafe',
'kilponen solar',
'pxwaxpy solar',
'a addtop',
'hiluckey',
'djroll',
'anker',
]

for i in l:
    print(f'insert into mapped_prod_names(name) values("{i}");')
