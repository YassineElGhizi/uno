import datetime
#GLOBAL Vars
items_present_in_page = dict()
cards_links = list()
stockage_list = ['32 Go',
                 '32 Gb' ,
                 '128 Gb',
                 '256 Gb',
                 '512 Gb',
                 '1 Tb' ,
                 '128 Go',
                 '256 Go',
                 '512 Go',
                 '1 To' ,
                 '64 Go' ,
                 '64 Gb',
        ]

colors = ['Bleu Alpin',
          'Red',
          'Graphite',
          'Or' ,
          'Bleu Pacifique',
          'Argent',
          'Argent',
          'Rose',
          'Bleu' ,
          'Minuit' ,
          'Noir' ,
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
          'Lumière Stellaire'
        ]
now = datetime.datetime.now()
scraped_at = "{}-{}-{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)

#Functions
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
        if c.upper() in title:
            return c

    for c in colors:
        if c in title:
            return c
    return "UNKNOWN"

def convert_item_price_to_double(price):
    tmp = price.split("MAD")[0]
    tmp = tmp.split()
    floatprice = "".join(tmp)
    floatprice = floatprice.replace("," , ".")
    return float(floatprice)
