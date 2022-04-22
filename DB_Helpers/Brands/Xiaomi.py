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
s = requests.session()
res = s.get('https://www.gsmarena.com/xiaomi-phones-f-80-0-p7.php' , headers=headers)
soup = BS(res.text , features="html.parser")



tmp = soup.find('div' , {'class': 'makers'})
spans = tmp.findAll('span')

[print(i.get_text()) for i in spans]







