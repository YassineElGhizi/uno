a ='me":"Apple iPhone 11 Pro 64 Go (Or, Neuf, 1 An de Garantie)","sku":"MWC52AA\/A","description":"Pr'

tmp = (a.split('"sku":"')[1]).split('","description"')[0]
tmp = tmp.replace('\/' , '/')

print(tmp)