import datetime

#GLOBAL Vars
uno_iphones_links = [
    { "link" : "https://uno.ma/iphone-maroc/iphone-11-pro-max-maroc/?limit=100" , "product_name" : "iPhone 11 PRO MAX" , "id_store" : 1,"subcategory" : 1},
    { "link" : "https://uno.ma/iphone-maroc/iphone-11-pro-maroc/?limit=100" , "product_name" : "iPhone 11 PRO" , "id_store" : 1,"subcategory" : 1},
    { "link" : "https://uno.ma/iphone-maroc/iphone-11-maroc/?limit=100" , "product_name" : "iPhone 11" , "id_store" : 1,"subcategory" : 1},
    { "link" : "https://uno.ma/iphone-maroc/iphone-12-pro-max-maroc/?limit=100" , "product_name" : "iPhone 12 PRO MAX" , "id_store" : 1,"subcategory" : 1},
    { "link" : "https://uno.ma/iphone-maroc/iphone-12-pro-maroc/?limit=100" , "product_name" : "iPhone 12 PRO" , "id_store" : 1,"subcategory" : 1},
    { "link" : "https://uno.ma/iphone-maroc/iphone-12-maroc/?limit=100" , "product_name" : "iPhone 12" , "id_store" : 1,"subcategory" : 1},
    { "link" : "https://uno.ma/iphone-maroc/iphone-12-mini-maroc/?limit=100" , "product_name" : "iPhone 12 Mini" , "id_store" : 1,"subcategory" : 1},
    { "link" : "https://uno.ma/iphone-maroc/iphone-8-plus-maroc/?limit=100" , "product_name" : "iPhone 8 PLUS" , "id_store" : 1,"subcategory" : 1},
    { "link" : "https://uno.ma/iphone-maroc/iphone-7-maroc/?limit=100" , "product_name" : "iPhone 7" , "id_store" : 1,"subcategory" : 1},
    { "link" : "https://uno.ma/iphone-maroc/iphone-se-maroc/?limit=100" , "product_name" : "iPhone Se" , "id_store" : 1,"subcategory" : 1},
    { "link" : "https://uno.ma/iphone-maroc/apple-iphone-13-pro-maroc/?limit=100" , "product_name" : "iPhone 13 PRO" , "id_store" : 1,"subcategory" : 1},
    { "link" : "https://uno.ma/iphone-maroc/apple-iphone-13-maroc/?limit=100" , "product_name" : "iPhone 13" , "id_store" : 1,"subcategory" : 1},
    { "link" : "https://uno.ma/iphone-maroc/apple-iphone-13-mini-maroc/?limit=100" , "product_name" : "iPhone 13 Mini" , "id_store" : 1,"subcategory" : 1},
    { "link" : "https://uno.ma/iphone-maroc/iphone-xr-maroc/?limit=100" , "product_name" : "iPhone Xr" , "id_store" : 1,"subcategory" : 1},
]

uno_ipads_links = [
    { "link" : "https://uno.ma/ipad-maroc/ipad-pro-129-maroc" , "product_name" : "iPad PRO 12.9" , "id_store" : 1,"subcategory" : 2},
    { "link" : "https://uno.ma/ipad-maroc/ipad-pro-11-maroc" , "product_name" : "iPad PRO 11" , "id_store" : 1,"subcategory" : 2},
    { "link" : "https://uno.ma/ipad-maroc/ipad-air-maroc" , "product_name" : "iPad Air 10.9" , "id_store" : 1,"subcategory" : 2},
    { "link" : "https://uno.ma/ipad-maroc/ipad-10-2-pouces-maroc" , "product_name" : "iPad 10.2" , "id_store" : 1,"subcategory" : 2},
    { "link" : "https://uno.ma/ipad-maroc/ipad-mini-maroc" , "product_name" : "iPad Mini" , "id_store" : 1,"subcategory" : 2},
]


uno_mac_links = [
    { "link" : "https://uno.ma/mac-maroc/macbook-air-maroc/" , "product_name" : "Macbook Air" , "id_store" : 1,"subcategory" : 3},
    { "link" : "https://uno.ma/mac-maroc/macbook-pro-13-maroc" , "product_name" : "Macbook Pro 13" , "id_store" : 1,"subcategory" : 3},
    { "link" : "https://uno.ma/mac-maroc/macbook-pro-14-maroc" , "product_name" : "Macbook Pro 14" , "id_store" : 1,"subcategory" : 3},
    { "link" : "https://uno.ma/mac-maroc/macbook-pro-16-maroc" , "product_name" : "Macbook Pro 16" , "id_store" : 1,"subcategory" : 3},
    { "link" : "https://uno.ma/mac-maroc/imac-maroc/imac-27-pouces-maroc" , "product_name" : "iMac 27 pouce" , "id_store" : 1,"subcategory" : 3},
    { "link" : "https://uno.ma/mac-maroc/imac-maroc/imac-24-pouces-maroc" , "product_name" : "iPad 24 pouce" , "id_store" : 1,"subcategory" : 3},
    { "link" : "https://uno.ma/mac-maroc/mac-mini-maroc/" , "product_name" : "Apple Mac Mini" , "id_store" : 1,"subcategory" : 3},
]

uno_watches_links = [
    {"link": "https://uno.ma/watch-maroc/apple-watch-series-7-maroc", "product_name": "Apple watch series 7", "id_store": 1,"subcategory": 4},
    {"link": "https://uno.ma/watch-maroc/apple-watch-series-6-maroc", "product_name": "Apple watch series 6", "id_store": 1,"subcategory": 4},
    {"link": "https://uno.ma/watch-maroc/apple-watch-se-maroc", "product_name": "Apple watch SE", "id_store": 1,"subcategory": 4},
    {"link": "https://uno.ma/watch-maroc/apple-watch-series-5-maroc", "product_name": "Apple watch series 5", "id_store": 1,"subcategory": 4},
    {"link": "https://uno.ma/watch-maroc/apple-watch-series-3-maroc", "product_name": "Apple watch serie 3", "id_store": 1,"subcategory": 4},
    {"link": "https://uno.ma/watch-maroc/accessoires-apple-watch-maroc", "product_name": "Accessoires", "id_store": 1,"subcategory": 4},
]


uno_headphones_links = [
    {"link": "https://uno.ma/apple-music-maroc", "product_name": "Ecouteurs", "id_store": 1,"subcategory": 5},
]

uno_tvs_links = [
    {"link": "https://uno.ma/apple-tv-maroc-11", "product_name": "Apple Tv", "id_store": 1, "subcategory": 6},
]

uno_accessoires_links = [
    {"link": "https://uno.ma/accessoires-maroc/cables-chargeurs-maroc/", "product_name": "Cable Chargeur", "id_store": 1, "subcategory": 7},
    {"link": "https://uno.ma/accessoires-maroc/accessoires-iphone-maroc/", "product_name": "accessoires Iphone", "id_store": 1, "subcategory": 7},
    {"link": "https://uno.ma/accessoires-maroc/accessoires-mac-maroc/", "product_name": "accessoires Mac", "id_store": 1, "subcategory": 7},
    {"link": "https://uno.ma/accessoires-maroc/powerbank-maroc/", "product_name": "powerbank", "id_store": 1, "subcategory": 7},
    {"link": "https://uno.ma/accessoires-maroc/coques-etuis-iphone-maroc/", "product_name": "coques Iphone", "id_store": 1, "subcategory": 7},
    {"link": "https://uno.ma/accessoires-maroc/stockage-maroc/", "product_name": "Disque dur externe", "id_store": 1, "subcategory": 7},
    {"link": "https://uno.ma/accessoires-maroc/wacom-maroc/", "product_name": "Tablette Graphique", "id_store": 1, "subcategory": 7},
]

items_present_in_page = dict()
cards_links = list()

garantie_list = [
    '1 An de Garantie',
    '1 an de Garantie',

]

screen_size_list = [
    '12.9 pouces',
    '10.9 Pouces',
    '10.2 Pouces',
    '10.2 pouces',
    '11 Pouces',
    '11 pouces',
    '8.3 pouces',
    '13" Puce',
    '13" avec écran Rétina Puce',
    '16" avec écran Rétina Puce',
    '27" avec écran Retina 5K',
    '24" avec écran Retina 4.5K',
    '16" avec écran Rétina',
]

connextion_adapter = [
    'Wi-Fi + 4G',
    'Wi-Fi + Cellular',
    'Wi-Fi + 4G / Cellulaire',
    'Wi-Fi',
    'Wi-Fi',
]

power = [
    '30W',
    '12W',
    '20W',
    '5W'
]

stockage_list = [
                 '32 Go',
                 '32Go',
                 '32 Gb' ,
                 '32Gb' ,
                 '32b' ,
                 '128 Gb',
                 '128Gb',
                 '128G',
                 '128 Go',
                 '256 Gb',
                 '256 Go',
                 '256Go',
                 '256G',
                 '256Gb',
                 '256b',
                 '512 Gb',
                 '512Gb',
                 '512G',
                 '512 Go',
                 '512Go',
                 '1 Tb' ,
                 '1Tb' ,
                 '1T' ,
                 '1 To' ,
                 '2 Tb',
                 '2Tb',
                 '2T',
                 '2 To',
                 '64 Go' ,
                 '64 Gb',
                 '64Gb',
                 '64G',
        ]

colors = [
        'Violet',
        'Bleu Alpin',
        'Red',
        'Graphite',
        'Or' ,
        'Bleu Pacifique',
        'Argent',
        'Argent',
        'Rose',
        'Blue',
        'Bleu',
        'Minuit' ,
        'Noir' ,
        'NOIR' ,
        'Blanc' ,
        'Rouge',
        'Vert Nuit',
        'Vert',
        'Jaune',
        'Gold' ,
        'Silver',
        'Black',
        'Midnight',
        'Pacific Blu' ,
        'Green' ,
        'Pink' ,
        'Gris',
        'Lumière Stellaire',
        ]

ram = [
    '8 Go RAM',
    '8 Go',
    '16 Go RAM',
    '16 Go',
    '32 Go RAM',
    '32 Go',
    '64 Go RAM',
    '64 Go',
    '128 Go RAM',
    '128 Go',
    '4 Go RAM'
    '4 Go'
    '256 Go RAM',
    '256 Go',
]

stockage_type = [
    'SSD',
    'ssd',
    'HDD',
    'hdd',
]

device_lenght = [
    '2M',
    '1M',
    '3M',
    '4M',
    '2 m',
    '1 m',
    '3 m',
    '4 m',
]


now = datetime.datetime.now()
scraped_at = "{}-{}-{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)

#Functions

def find_device_power(title):
    for i in power:
        if i in title:
            return i
    return "UNKNOWN"

def find_device_lenght(title):
    for i in device_lenght:
        if i in title:
            return i
    return "UNKNOWN"

def find_device_stockage(title):
    for st in stockage_list:
        if st.upper() in title:
            return st

    for st in stockage_list:
        if st in title:
            return st

    return "UNKNOWN"

def find_device_color(title):
    for c in colors:
        if c in title:
            return c
    return "UNKNOWN"

def find_device_garantie(title):
    for i in garantie_list:
        if i in title:
            return i
    return "UNKNOWN"

def find_device_screen_size(title):
    for i in screen_size_list:
        if i in title:
            return i
    return "UNKNOWN"

def find_device_connextion_adapter(title):
    for i in connextion_adapter:
        if i in title:
            return i
    return "UNKNOWN"


def find_device_ram(title):
    for i in ram:
        if i in title:
            return i
    return "UNKNOWN"

def find_device_type_stockage(title):
    for i in stockage_type:
        if i in title:
            return i
    return "UNKNOWN"

def convert_item_price_to_double(price):
    tmp = price.split("MAD")[0]
    tmp = tmp.split()
    floatprice = "".join(tmp)
    floatprice = floatprice.replace("," , ".")
    return float(floatprice)
