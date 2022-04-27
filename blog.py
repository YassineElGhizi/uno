import requests
from bs4 import BeautifulSoup as BS
from random import  randint
from time import sleep

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


#GET A TAGS
s = requests.session()
r = s.get('https://pagesix.com/' , headers=headers)
soup = BS(r.text, features='html.parser')

container = soup.find('ul' , {'class' : 'article-loop'})
lis = container.findAll('li')
a_links = []

for l in lis:
    a_links.append(l.find('a').get('href'))

for a in a_links:
    r = s.get(a ,headers=headers)
    soup = BS(r.text , features='html.parser')
    print(f'Article link = {a}')

    #Title
    try:
        blog_title = soup.select_one('#article-wrapper > div.box.article.modal-enabled > div.article-header > h1').get_text().strip()
    except:
        blog_title = soup.select_one('#main > article > div > div > div.layout__item.layout__item--main > div > div.single__header > header > h1').get_text().strip()
    print(f'blog_title = {blog_title}')

    #Date
    try:
        blog_date = soup.select_one('#article-wrapper > div.box.article.modal-enabled > div.article-header > p').get_text().strip()
    except:
        blog_date = soup.select_one('#main > article > div > div > div.layout__item.layout__item--main > div > div.single__header > header > div.article-header__meta > div.date.meta.meta--byline > span:nth-child(1)').get_text().strip()
    print(f'blog_date = {blog_date}')

    #Date Content
    blog_content = soup.select_one('#article-wrapper > div.box.article.modal-enabled > div.article-header > div.entry-content.entry-content-read-more')
    if not blog_content:
        blog_content = soup.select_one('#main > article > div > div > div.layout__item.layout__item--main > div > div.single__content.entry-content.m-bottom')
    print(blog_content)

    #Main Image
    try:
        main_image = soup.select_one('#standard-article-image').get('src')
    except:
        try:
            a_tags = soup.findAll('a')
            for a in a_tags:
                href : str
                href = a.get('href')
                if href.endswith('.jpg'):
                    main_image = href
                    break
        except:
            main_image = None
    print(f'main_image = {main_image}')
    sleep(randint(1,3))
    print('\n\n\n\n\n\n')