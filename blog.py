import requests
from bs4 import BeautifulSoup as BS

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
    'accept': '/',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-language': 'en-US,en;q=0.9',
    'DNT': '1',
    'Referer': 'https://google.com'
}

def get_cats_link(session):
    r = session.get('https://nautil.us/' , headers=headers)
    soup = BS(r.text, features='html.parser')
    cats_container = (soup.findAll('ul' , {'class' : 'header-links'})[0]).findAll('a')
    return list(map( lambda i: i.get('href'), cats_container))

def scrape_article(cat_links, session):
    for c in cat_links:
        r = session.get(c , headers=headers)
        soup = BS(r.text, features='html.parser')
        items = soup.findAll('div' , {'class' : 'article-list_item-content'})
        for x in items:
            print(x)
            print('\n')

        quit()



if __name__ == '__main__':
    s = requests.session()
    categories = get_cats_link(s)
    scrape_article(categories, s)

