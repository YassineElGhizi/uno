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


#GET A TAGS
s = requests.session()
r = s.get('https://www.justjared.com/')
soup = BS(r.text, features='html.parser')

posts = soup.findAll('div' , {'class' : 'post'})
a_tags = []
for p in posts:
    a = p.find('a').get('href')
    if a.startswith('https://www.justjared.com/'):
        a_tags.append(a)


#Getting Info from each blog
for a in a_tags:
    blog_link = a
    r = s.get('https://www.justjared.com/')
    soup = BS(r.text, features='html.parser')
    main_image = soup.find('div' , {'class' : 'lead-img'})
    main_image = main_image.find('img').get('src')
    tmp = soup.find('div' , {'class' , 'post-header'})
    blog_timestamp = tmp.find('div' , {'class' : 'post-date'}).get_text().strip()

    tmp = soup.find('div', {'class', 'post'})
    blog_title = tmp.find('h1').get_text().strip()

    tmp = soup.find('div' , {'id': 'content'})
    tmp = tmp.find('div' , {'class' : 'post'})
    tmp = tmp.find('div' , {'class' : 'entry'})
    p_tags = tmp.findAll('p')
    for p in p_tags:
        a_tags = p.findAll('a')
        for a in a_tags:
            del a['href']

    print(f'blog_title = {blog_title}')
    print(f'blog_timestamp = {blog_timestamp}')
    print(f'blog_link = {blog_link}')
    print(f'main_image = {main_image}')
    print('===ARTICLE BODY ===')
    for p in p_tags:
        print(p)
    print('\n')


    quit()

