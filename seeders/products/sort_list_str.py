ma_str = [
'Cable Chargeur',
'iPad 10.2',
'iPad Air 10.9',
'iPad Mini',
'iPad PRO 11',
'iPad PRO 12.9',
'iPhone 11',
'iPhone 11 PRO',
'iPhone 11 PRO MAX',
'iPhone 12',
'iPhone 12 Mini',
'iPhone 12 PRO',
'iPhone 12 PRO MAX',
'iPhone 13',
'iPhone 13 Mini',
'iPhone 13 PRO',
'iPhone 13 PRO MAX',
'iPhone 7',
'iPhone 8 PLUS',
'iPhone Se',
'iPhone 6S',
'iPhone X',
'iPhone 6',
'Macbook Air',
'Macbook Pro 13',
'Macbook Pro 14',
'Macbook Pro 16',
'Macbook Pro',
'iMac 27 pouce',
'iPad 24 pouce',
'Apple Mac Mini',
'Apple watch series 7',
'Apple watch series 6',
'Apple watch SE',
'Apple watch serie 3',
'Accessoires',
'Apple Tv',
'accessoires Iphone',
'accessoires Mac',
'powerbank',
'coques Iphone',
'Disque dur externe',
'Tablette Graphique',
'Ecouteurs',
'POCO',
'REDMI NOTE',
'REDMI NOTE 10',
'REDMI NOTE 11',
'NOVA Y60',
'NOVA 9',
'NOVA',
'NOVA 8I',
'A03',
'NOTE10',
'ALCATEL',
'A7',
'A7 LITE',
'A74',
'A54',
'A94',
'A22',
'A32',
'A22',
'A8',
'A30',
'A02',
'A50',
'A30',
'F3',
'RENO6 Z',
'MEDIAPAD T5',
'800',
'800 TA-1189',
'11T',
'3.4 TA-1288',
'110 TA-1192',
'105 TA-1203',
'11T',
'S7 FE',
'S21 FE',
'TAB S7',
'TAB S7+',
'FOLIO VIEW XL NIGHT',
'FOLIO VIEW PRIME NIGHT',
'TAB MATEPAD T10S',
'TAB KEYTAB',
'MI11 LITE',
'Note 11S',
'MI 11 LITE',
'MATEPAD T10S',
'MATEPAD T10',
'S20+',
'S10',
'S10E',
'S10',
'A3',
'2720 TA-1170 DS NENA1',
'TEL DECT D285',
'TEL DECT',
'MATEPAD',
]
ma_str.sort(key = len, reverse=True)

[print(f'insert into mapped_prod_names(name) values(\"{s}\");') for s in ma_str]