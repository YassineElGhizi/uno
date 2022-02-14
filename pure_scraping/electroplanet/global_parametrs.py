import datetime

#GLOBAL Vars
electroplanet_préparation_culinaire = [
    { "link" : "https://www.electroplanet.ma/petit-electromenager/preparation-culinaire/batteur" , "id_store" : 3,"subcategory" : "Batteur"},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/preparation-culinaire/blender" , "id_store" : 3,"subcategory" : "Blender"},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/preparation-culinaire/hache-viande" , "id_store" : 3,"subcategory" : "Hache viande"},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/preparation-culinaire/hachoir" , "id_store" : 3,"subcategory" : "Hachoir"},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/preparation-culinaire/kitchen-machine" , "id_store" : 3,"subcategory" : "Kitchen machine"},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/preparation-culinaire/mixeur-plongeant" , "id_store" : 3,"subcategory" : "Mixeur plongeant"},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/preparation-culinaire/moulinette" , "id_store" : 3,"subcategory" : "Moulinette"},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/preparation-culinaire/robot-de-cuisine" , "id_store" : 3,"subcategory" : "Robot de cuisine"},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/preparation-culinaire/sorbetiere" , "id_store" : 3,"subcategory" : "Sorbetière"},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/preparation-culinaire/yaourtiere" , "id_store" : 3,"subcategory" : "Yaourtière"},
]

electroplanet_petit_dejeuner = [
    { "link" : "https://www.electroplanet.ma/petit-electromenager/petit-dejeuner/bouilloire" , "id_store" : 3,"subcategory" : "Bouilloire"},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/petit-dejeuner/centrifugeuse" , "id_store" : 3,"subcategory" : "Centrifugeuse"},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/petit-dejeuner/extracteur-de-jus" , "id_store" : 3,"subcategory" : "Extracteur de jus"},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/petit-dejeuner/grill-pain-toaster" , "id_store" : 3,"subcategory" : "Grill pain - toaster"},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/petit-dejeuner/presse-agrume" , "id_store" : 3,"subcategory" : "Grill pain - Presse-agrumes"},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/petit-dejeuner/set-petit-dejeuner" , "id_store" : 3,"subcategory" : "Set petit déjeuner"},
]

electroplanet_accessoires_electromenager = [
    { "link" : "https://www.electroplanet.ma/petit-electromenager/accessoires/accessoires-petit-dejeuner" , "id_store" : 3,"subcategory" : "Accessoires petit déjeuner"},
]

electroplanet_balance_de_cuisine = [
    {"link": "https://www.electroplanet.ma/petit-electromenager/accessoires/accessoires-petit-dejeuner", "id_store": 3, "subcategory": "Balance de cuisine"},
]


electroplanet_cafetière_et_expresso = [
    {"link": "https://www.electroplanet.ma/petit-electromenager/cafetiere-et-expresso/cafetiere-classique", "id_store": 3, "subcategory": "Cafetiere classique"},
    {"link": "https://www.electroplanet.ma/petit-electromenager/cafetiere-et-expresso/expresso-a-capsule", "id_store": 3, "subcategory": "Expresso a capsule"},
    {"link": "https://www.electroplanet.ma/petit-electromenager/cafetiere-et-expresso/expresso-avec-broyeur-a-cafe", "id_store": 3, "subcategory": "Expresso avec broyeur a cafe"},
    {"link": "https://www.electroplanet.ma/petit-electromenager/cafetiere-et-expresso/machine-a-cafe-pression", "id_store": 3, "subcategory": "Machine a cafe pression"},
    {"link": "https://www.electroplanet.ma/petit-electromenager/cafetiere-et-expresso/moulin-a-cafe", "id_store": 3, "subcategory": "Moulin a cafe"},
]

electroplanet_cuiseurs = [
    {"link": "https://www.electroplanet.ma/petit-electromenager/cuiseur/cuiseur-a-riz-et-a-vapeur","id_store": 3, "subcategory": "Cuiseur a riz et a vapeur"},
    {"link": "https://www.electroplanet.ma/petit-electromenager/cuiseur/cuiseur-a-vapeur","id_store": 3, "subcategory": "Cuiseur a vapeur"},
    {"link": "https://www.electroplanet.ma/petit-electromenager/cuiseur/cuiseur-classique","id_store": 3, "subcategory": "Cuiseur classique"},
]

electroplanet_cuisson_conviviale = [
    {"link": "https://www.electroplanet.ma/petit-electromenager/cuisson-conviviale/appareil-a-croque-monsieur","id_store": 3, "subcategory": "Appareil à croque monsieur"},
    {"link": "https://www.electroplanet.ma/petit-electromenager/cuisson-conviviale/crepiere","id_store": 3, "subcategory": "Crepiere"},
    {"link": "https://www.electroplanet.ma/petit-electromenager/cuisson-conviviale/gaufrier","id_store": 3, "subcategory": "Gaufrier"},
    {"link": "https://www.electroplanet.ma/petit-electromenager/cuisson-conviviale/grill-a-panini","id_store": 3, "subcategory": "Grill à panini"},
    {"link": "https://www.electroplanet.ma/petit-electromenager/cuisson-conviviale/grill-a-viande","id_store": 3, "subcategory": "Grill à viande"},
]

electroplanet_cuisson_festive = [
    {"link": "https://www.electroplanet.ma/petit-electromenager/cuisson-festive/machine-a-barbe-a-papa", "id_store": 3,"subcategory": "Machine a barbe a papa"},
    {"link": "https://www.electroplanet.ma/petit-electromenager/cuisson-festive/machine-a-pop-corn", "id_store": 3,"subcategory": "Machine a pop corn"},
]


electroplanet_four_et_micro_ondes = [
    {"link": "https://www.electroplanet.ma/petit-electromenager/four-et-micro-onde/four-posable", "id_store": 3,"subcategory": "Four posable"},
    {"link": "https://www.electroplanet.ma/petit-electromenager/four-et-micro-onde/micro-onde", "id_store": 3,"subcategory": "Micro-ondes"},
    {"link": "https://www.electroplanet.ma/petit-electromenager/four-et-micro-onde/rechaud", "id_store": 3,"subcategory": "Rechaud"},
]

electroplanet_friteuses = [
    {"link": "https://www.electroplanet.ma/petit-electromenager/friteuse/friteuse-classique", "id_store": 3,"subcategory": "Friteuse classique"},
    {"link": "https://www.electroplanet.ma/petit-electromenager/friteuse/friteuse-sans-huile", "id_store": 3,"subcategory": "Friteuse sans huile"},
]

electroplanet_Machine_a_gateaux = [
    {"link": "https://www.electroplanet.ma/petit-electromenager/machine-a-gateaux/machine-a-biscuit", "id_store": 3,"subcategory": "Machine à biscuit"},
    {"link": "https://www.electroplanet.ma/petit-electromenager/machine-a-gateaux/machine-a-tarte", "id_store": 3,"subcategory": "Machine a tarte"},
    {"link": "https://www.electroplanet.ma/petit-electromenager/machine-a-gateaux/machine-a-madeleine", "id_store": 3,"subcategory": "Machine a madeleine"},
    {"link": "https://www.electroplanet.ma/petit-electromenager/machine-a-gateaux/machine-a-pain", "id_store": 3,"subcategory": "Machine a pain"},
    {"link": "https://www.electroplanet.ma/petit-electromenager/machine-a-gateaux/machine-a-popcake", "id_store": 3,"subcategory": "Machine a popcake"},
]


electroplanet_mijoteur =  [
    {"link": "https://www.electroplanet.ma/petit-electromenager/mijoteur/multicuiseur-intelligent", "id_store": 3,"subcategory": "Multicuiseur intelligent"},
]

electroplanet_Pack_preparation_culinaire = [
    {"link": "https://www.electroplanet.ma/petit-electromenager/pack-preparation-culinaire/pack-preparation-culinaire", "id_store": 3,"subcategory": "Pack preparation culinaire"},
]


electroplanet_Barbecue_et_plancha = [
    {"link": "https://www.electroplanet.ma/petit-electromenager/barbecue-et-plancha/barbecue-et-plancha-electrique","id_store": 3, "subcategory": "Barbecue et plancha electrique"},
]

electroplanet_refrigerateur = [
    {"link": "https://www.electroplanet.ma/gros-electromenager/refrigerateur/mini-bar","id_store": 3, "subcategory": "Mini bar"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/refrigerateur/petit-refrigerateur","id_store": 3, "subcategory": "Petit Refrigerateur"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/refrigerateur/refrigerateur-4-portes","id_store": 3, "subcategory": "Refrigerateur 4 portes"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/refrigerateur/refrigerateur-americain-duo-jumelable","id_store": 3, "subcategory": "Refrigerateur americain duo jumelable"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/refrigerateur/refrigerateur-americain-side-by-side","id_store": 3, "subcategory": "Refrigerateur americain side by side"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/refrigerateur/refrigerateur-avec-congelateur-en-bas","id_store": 3, "subcategory": "Refrigerateur avec congelateur en bas"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/refrigerateur/refrigerateur-avec-congelateur-en-haut","id_store": 3, "subcategory": "Refrigerateur avec congelateur en haut"},
]

electroplanet_accessoires_electromenager2 = [
    {"link": "https://www.electroplanet.ma/gros-electromenager/accessoires/accessoires-communs","id_store": 3, "subcategory": "Accessoires communs"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/accessoires/accessoires-cuisson","id_store": 3, "subcategory": "Accessoires cuisson"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/accessoires/accessoires-froid","id_store": 3, "subcategory": "Accessoires froid"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/accessoires/accessoires-lavage","id_store": 3, "subcategory": "Accessoires lavage"},
]


electroplanet_congelateur = [
    {"link": "https://www.electroplanet.ma/gros-electromenager/congelateur/congelateur-armoire", "id_store": 3,"subcategory": "Congelateur armoire"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/congelateur/congelateur-coffre", "id_store": 3,"subcategory": "Congelateur coffre"},
]


electroplanet_cuisiniere = [
    {"link": "https://www.electroplanet.ma/gros-electromenager/cuisiniere/cuisiniere-4-feux", "id_store": 3,"subcategory": "Cuisiniere 4 feux"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/cuisiniere/cuisiniere-5-feux", "id_store": 3,"subcategory": "Cuisiniere 5 feux"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/cuisiniere/cuisiniere-5-feux-cache-bouteille", "id_store": 3,"subcategory": "Cuisiniere 5 feux cache bouteille"},
]


electroplanet_encastrable = [
    {"link": "https://www.electroplanet.ma/gros-electromenager/encastrable/four-encastrable", "id_store": 3,"subcategory": "Four encastrable"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/encastrable/grand-four-encastrable", "id_store": 3,"subcategory": "Grand four encastrable"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/encastrable/lave-vaisselle-encastrable", "id_store": 3,"subcategory": "Lave vaisselle encastrable"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/encastrable/machine-a-laver-encastrable", "id_store": 3,"subcategory": "Machine a laver encastrable"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/encastrable/petit-four-encastrable", "id_store": 3,"subcategory": "Petit four encastrable"},
]


electroplanet_hotte_aspirante = [
    {"link": "https://www.electroplanet.ma/gros-electromenager/hotte-aspirante/hotte-aspirante-ilot", "id_store": 3,"subcategory": "Hotte aspirante ilot"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/hotte-aspirante/hotte-aspirante-visiere", "id_store": 3,"subcategory": "Hotte aspirante visiere"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/hotte-aspirante/hotte-decorative-murale", "id_store": 3,"subcategory": "Hotte decorative murale"},
]



electroplanet_lave_vaisselle = [
    {"link": "https://www.electroplanet.ma/gros-electromenager/lave-vaisselle/lave-vaisselle-pose-libre", "id_store": 3,"subcategory": "Lave vaisselle pose libre"},
]

electroplanet_machine_a_laver = [
    {"link": "https://www.electroplanet.ma/gros-electromenager/machine-a-laver/machine-a-laver-a-hublot", "id_store": 3,"subcategory": "Machine a laver a hublot"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/machine-a-laver/machine-a-laver-ouverture-en-haut", "id_store": 3,"subcategory": "Machine a laver ouverture en haut"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/machine-a-laver/machine-a-laver-sechante", "id_store": 3,"subcategory": "machine a laver sechante"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/machine-a-laver/machine-a-laver-semi-automatique-avec-essorage", "id_store": 3,"subcategory": "Machine a laver semi automatique avec essorage"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/machine-a-laver/machine-a-laver-semi-automatique-sans-essorage", "id_store": 3,"subcategory": "Machine a laver semi automatique sans essorage"},
]



electroplanet_plaque_de_cuisson = [
    {"link": "https://www.electroplanet.ma/gros-electromenager/plaque-de-cuisson/plaque-de-cuisson-a-gaz", "id_store": 3,"subcategory": "Plaque de cuisson a gaz"},
    {"link": "https://www.electroplanet.ma/gros-electromenager/plaque-de-cuisson/plaque-de-cuisson-electrique", "id_store": 3,"subcategory": "Plaque de cuisson electrique"},
]

electroplanet_sèche_linge = [
    {"link": "https://www.electroplanet.ma/gros-electromenager/seche-linge/seche-linge-a-condensation","id_store": 3, "subcategory": "Seche linge a condensation"},
]

electroplanet_accessoires_electromenager3 = [
    {"link": "https://www.electroplanet.ma/entretien-de-la-maison/accessoires/accessoires-entretien-de-la-maison", "id_store": 3,"subcategory": "Accessoires entretien de la maison"},
    {"link": "https://www.electroplanet.ma/entretien-de-la-maison/accessoires/accessoires-entretien-du-linge", "id_store": 3,"subcategory": "Accessoires entretien du linge"},
]


electroplanet_Entretien_du_sol = [
    {"link": "https://www.electroplanet.ma/entretien-de-la-maison/entretien-du-sol/aspirateur","id_store": 3, "subcategory": "Aspirateur"},
    {"link": "https://www.electroplanet.ma/entretien-de-la-maison/entretien-du-sol/aspirette","id_store": 3, "subcategory": "Aspirette"},
    {"link": "https://www.electroplanet.ma/entretien-de-la-maison/entretien-du-sol/nettoyeur-a-vapeur","id_store": 3, "subcategory": "Nettoyeur a vapeur"},
    {"link": "https://www.electroplanet.ma/entretien-de-la-maison/entretien-du-sol/pack-aspirateur","id_store": 3, "subcategory": "Pack aspirateur"},
]

electroplanet_soin_du_ligne = [
    {"link": "https://www.electroplanet.ma/entretien-de-la-maison/soin-du-linge/housse-table-a-repasser", "id_store": 3,"subcategory": "Housse table a repasser"},
    {"link": "https://www.electroplanet.ma/entretien-de-la-maison/soin-du-linge/planches-a-repasser", "id_store": 3,"subcategory": "Planches a repasser"},
    {"link": "https://www.electroplanet.ma/entretien-de-la-maison/soin-du-linge/centrale-vapeur", "id_store": 3,"subcategory": "Centrale vapeur"},
    {"link": "https://www.electroplanet.ma/entretien-de-la-maison/soin-du-linge/defroisseur", "id_store": 3,"subcategory": "Defroisseur"},
    {"link": "https://www.electroplanet.ma/entretien-de-la-maison/soin-du-linge/fer-a-repasser", "id_store": 3,"subcategory": "Fer a repasser"},
]

electroplanet_bebe = [
    {"link": "https://www.electroplanet.ma/sante-beaute-bebe/bebe/biberon", "id_store": 3,"subcategory": "Biberon"},
    {"link": "https://www.electroplanet.ma/sante-beaute-bebe/bebe/sterilisateur-de-biberon", "id_store": 3,"subcategory": "Sterilisateur de biberon"},
]


electroplanet_coiffure = [
    {"link": "https://www.electroplanet.ma/sante-beaute-bebe/coiffure/brosse-soufflante", "id_store": 3,"subcategory": "Brosse soufflante"},
    {"link": "https://www.electroplanet.ma/sante-beaute-bebe/coiffure/fer-a-coiffer", "id_store": 3,"subcategory": "Fer a coiffer"},
    {"link": "https://www.electroplanet.ma/sante-beaute-bebe/coiffure/lisseur", "id_store": 3,"subcategory": "Lisseur"},
    {"link": "https://www.electroplanet.ma/sante-beaute-bebe/coiffure/seche-cheveux", "id_store": 3,"subcategory": "Seche cheveux"},
]

electroplanet_epilation_pour_elle = [
    {"link": "https://www.electroplanet.ma/sante-beaute-bebe/epilation-pour-elle/epilateur", "id_store": 3,"subcategory": "Epilateur"},
]

electroplanet_pack_beaute = [
    {"link": "https://www.electroplanet.ma/sante-beaute-bebe/pack-beaute/pack-beaute", "id_store": 3,"subcategory": "Pack Beaute"},
]

electroplanet_rasage_pour_lui = [
    {"link": "https://www.electroplanet.ma/sante-beaute-bebe/rasage-pour-lui/rasoir", "id_store": 3,"subcategory": "Rasoir"},
    {"link": "https://www.electroplanet.ma/sante-beaute-bebe/rasage-pour-lui/tondeuse", "id_store": 3,"subcategory": "Tondeuse"},
]

electroplanet_Sante_et_bien_etre = [
    {"link": "https://www.electroplanet.ma/sante-beaute-bebe/sante-et-bien-etre/pese-personne", "id_store": 3,"subcategory": "Pese personne"},
]

electroplanet_soin_beaute = [
    {"link": "https://www.electroplanet.ma/sante-beaute-bebe/soin-beaute/appareil-anti-cellulite", "id_store": 3,"subcategory": "Appareil anti cellulite"},
    {"link": "https://www.electroplanet.ma/sante-beaute-bebe/soin-beaute/brosse-nettoyante-visage", "id_store": 3,"subcategory": "Brosse nettoyante visage"},
]

electroplanet_chaufage = [
    { "link" : "https://www.electroplanet.ma/confort-de-la-maison/chauffage/chauffage-a-gaz" , "id_store" : 3,"subcategory" : "Chauffage a gaz"},
    { "link" : "https://www.electroplanet.ma/confort-de-la-maison/chauffage/chauffage-soufflant" , "id_store" : 3,"subcategory" : "Chauffage soufflant"},
    { "link" : "https://www.electroplanet.ma/confort-de-la-maison/chauffage/cheminee-electrique" , "id_store" : 3,"subcategory" : "Cheminee electrique"},
    { "link" : "https://www.electroplanet.ma/confort-de-la-maison/chauffage/convecteur" , "id_store" : 3,"subcategory" : "Convecteur"},
    { "link" : "https://www.electroplanet.ma/confort-de-la-maison/chauffage/radiateur-bain-d-huile" , "id_store" : 3,"subcategory" : "Radiateur bain d huile"},
]


electroplanet_chaufage_eau = [
    {"link": "https://www.electroplanet.ma/confort-de-la-maison/chauffe-eau/chauffe-eau-a-gaz", "id_store": 3,"subcategory": "Chauffe eau a gaz"},
    {"link": "https://www.electroplanet.ma/confort-de-la-maison/chauffe-eau/chauffe-eau-electrique", "id_store": 3,"subcategory": "Chauffe eau electrique"},
    {"link": "https://www.electroplanet.ma/confort-de-la-maison/chauffe-eau/chauffe-eau-solaire", "id_store": 3,"subcategory": "Chauffe eau solaire"},
]


electroplanet_climatisation = [
    {"link": "https://www.electroplanet.ma/confort-de-la-maison/climatisation/climatiseur", "id_store": 3,"subcategory": "Climatiseur"},
    {"link": "https://www.electroplanet.ma/confort-de-la-maison/climatisation/ventilateur", "id_store": 3,"subcategory": "Ventilateur"},
]

electroplanet_traitement_de_air = [
    {"link": "https://www.electroplanet.ma/confort-de-la-maison/traitement-de-l-air/brumisateur", "id_store": 3,"subcategory": "Brumisateur"},
    {"link": "https://www.electroplanet.ma/confort-de-la-maison/traitement-de-l-air/deshumidificateur", "id_store": 3,"subcategory": "Deshumidificateur"},
    {"link": "https://www.electroplanet.ma/confort-de-la-maison/traitement-de-l-air/diffuseur-d-arome-parfum-d-ambiance", "id_store": 3,"subcategory": "Parfum d ambiance"},
    {"link": "https://www.electroplanet.ma/confort-de-la-maison/traitement-de-l-air/purificateur", "id_store": 3,"subcategory": "Purificateur"},

]

electroplanet_tv = [
    {"link": "https://www.electroplanet.ma/tv-photo-video/televiseur/tous-les-televiseur", "id_store": 3,"subcategory": "Televiseur"},
    {"link": "https://www.electroplanet.ma/tv-photo-video/televiseur/smart-tv", "id_store": 3,"subcategory": "Smart tv"},
    {"link": "https://www.electroplanet.ma/tv-photo-video/televiseur/televiseurs-4k-uhd", "id_store": 3,"subcategory": "Televiseurs 4k uhd"},
    {"link": "https://www.electroplanet.ma/tv-photo-video/televiseur/televiseurs-premium-4k-uhd", "id_store": 3,"subcategory": "Televiseurs premium 4k uhd"},
    {"link": "https://www.electroplanet.ma/tv-photo-video/televiseur/televiseurs-8k", "id_store": 3,"subcategory": "Televiseurs 8k"},
    {"link": "https://www.electroplanet.ma/tv-photo-video/televiseur/oled", "id_store": 3,"subcategory": "Oled"},
    {"link": "https://www.electroplanet.ma/tv-photo-video/televiseur/nanocell", "id_store": 3,"subcategory": "Oanocell"},
    {"link": "https://www.electroplanet.ma/tv-photo-video/televiseur/qled", "id_store": 3,"subcategory": "Oled"},
    {"link": "https://www.electroplanet.ma/tv-photo-video/televiseur/miniled-neoqled-qned", "id_store": 3,"subcategory": "Miniled neoqled qned"},
]


electroplanet_accessoires_tv_video = [
    {"link": "https://www.electroplanet.ma/tv-photo-video/accessoires-tv-video/cables-audio-video", "id_store": 3, "subcategory": "Cables audio video"},
    {"link": "https://www.electroplanet.ma/tv-photo-video/accessoires-tv-video/cables-d-alimentation", "id_store": 3, "subcategory": "Cables d alimentation"},
    {"link": "https://www.electroplanet.ma/tv-photo-video/accessoires-tv-video/telecommandes", "id_store": 3, "subcategory": "Telecommandes"},
    {"link": "https://www.electroplanet.ma/tv-photo-video/accessoires-tv-video/multiprises-et-parasurtenseurs", "id_store": 3, "subcategory": "Multiprises et parasurtenseurs"},
    {"link": "https://www.electroplanet.ma/tv-photo-video/support-et-meubles/support-tv", "id_store": 3, "subcategory": "Support tv"},
]


electroplanet_appareil_photo = [
    {"link": "https://www.electroplanet.ma/tv-photo-video/appareil-photo-numerique/appareil-photo-bridge", "id_store": 3,"subcategory": "Appareil photo bridge"},
    {"link": "https://www.electroplanet.ma/tv-photo-video/appareil-photo-numerique/appareil-photo-compact", "id_store": 3,"subcategory": "Appareil photo compact"},
    {"link": "https://www.electroplanet.ma/tv-photo-video/appareil-photo-numerique/appareil-photo-instantane", "id_store": 3,"subcategory": "Appareil photo instantane"},
    {"link": "https://www.electroplanet.ma/tv-photo-video/appareil-photo-numerique/appareil-photo-reflex", "id_store": 3,"subcategory": "Appareil photo reflex"},
]

electroplanet_recepteur_et_abonnement = [
    {"link": "https://www.electroplanet.ma/tv-photo-video/recepteur-et-abonnement/demodulateurs-et-recepteurs-tnt","id_store": 3, "subcategory": "Demodulateurs et recepteurs tnt"},
]

electroplanet_ecoteurs = [
    {"link": "https://www.electroplanet.ma/audio-hi-fi/ecouteurs/ecouteurs-avec-micro","id_store": 3, "subcategory": "Ecouteurs avec micro"},
    {"link": "https://www.electroplanet.ma/audio-hi-fi/ecouteurs/ecouteurs-avec-micro-sans-fil","id_store": 3, "subcategory": "Ecouteurs avec micro sans fil"},
    {"link": "https://www.electroplanet.ma/audio-hi-fi/ecouteurs/ecouteurs-sportifs-avec-micro","id_store": 3, "subcategory": "Ecouteurs sportifs avec micro"},
    {"link": "https://www.electroplanet.ma/audio-hi-fi/ecouteurs/ecouteurs-sportifs-avec-micro-sans-fil","id_store": 3, "subcategory": "Ecouteurs sportifs avec micro sans fil"},
]

electroplanet_Barres_de_son = [
    {"link": "https://www.electroplanet.ma/audio-hi-fi/barres-de-son/barre-de-son", "id_store": 3,"subcategory": "Barre de son"},
]

electroplanet_casques_audio = [
    {"link": "https://www.electroplanet.ma/audio-hi-fi/casque-audio/casque-audio-avec-micro", "id_store": 3,"subcategory": "casque audio avec micro"},
    {"link": "https://www.electroplanet.ma/audio-hi-fi/casque-audio/casque-audio-avec-micro-sans-fil", "id_store": 3,"subcategory": "casque audio avec micro sans fil"},
]

electroplanet_ordinateur_portable =[
    {"link": "https://www.electroplanet.ma/informatique/ordinateur-portable/hybride-2-en-1", "id_store": 3,"subcategory": "hybride 2 en 1"},
    {"link": "https://www.electroplanet.ma/informatique/ordinateur-portable/macbook", "id_store": 3,"subcategory": "Macbook"},
    {"link": "https://www.electroplanet.ma/informatique/ordinateur-portable/netbook", "id_store": 3,"subcategory": "Netbook"},
    {"link": "https://www.electroplanet.ma/informatique/ordinateur-portable/notebook", "id_store": 3,"subcategory": "Notebook"},
    {"link": "https://www.electroplanet.ma/informatique/ordinateur-portable/pc-gamer", "id_store": 3,"subcategory": "Pc gamer"},
    {"link": "https://www.electroplanet.ma/informatique/ordinateur-portable/ultrabook", "id_store": 3,"subcategory": "Ultrabook"},
]

electroplanet_ordinateur_bureau = [
    {"link": "https://www.electroplanet.ma/informatique/ordinateur-bureau/all-in-one", "id_store": 3,"subcategory": "All in one"},
    {"link": "https://www.electroplanet.ma/informatique/ordinateur-bureau/desktop-gamer", "id_store": 3,"subcategory": "Desktop Gamer"},
    {"link": "https://www.electroplanet.ma/informatique/ordinateur-bureau/ecran-pour-pc", "id_store": 3,"subcategory": "Ecran pour pc"},
    {"link": "https://www.electroplanet.ma/informatique/ordinateur-bureau/imac", "id_store": 3,"subcategory": "Imac"},
]

electroplanet_imprimantes_et_scanner = [
    {"link": "https://www.electroplanet.ma/informatique/imprimantes-et-scanner/imprimante-jet-d-encre", "id_store": 3,"subcategory": "Imprimante jet d encre"},
    {"link": "https://www.electroplanet.ma/informatique/imprimantes-et-scanner/imprimante-laser", "id_store": 3,"subcategory": "Imprimante laser"},
    {"link": "https://www.electroplanet.ma/informatique/imprimantes-et-scanner/imprimante-photo", "id_store": 3,"subcategory": "Imprimante photo"},
    {"link": "https://www.electroplanet.ma/informatique/consommable-imprimante/cartouche-encre-d-imprimante", "id_store": 3,"subcategory": "Cartouche encre d imprimante"},
    {"link": "https://www.electroplanet.ma/informatique/consommable-imprimante/toner", "id_store": 3,"subcategory": "Toner"},
]

electroplanet_accessoires_informatique = [
    {"link": "https://www.electroplanet.ma/jeux-consoles/accessoires-gaming/casques-gamers","id_store": 3, "subcategory": "Casques gamers"},
    {"link": "https://www.electroplanet.ma/jeux-consoles/accessoires-gaming/claviers","id_store": 3, "subcategory": "Claviers"},
    {"link": "https://www.electroplanet.ma/jeux-consoles/accessoires-gaming/manettes","id_store": 3, "subcategory": "Manettes"},
    {"link": "https://www.electroplanet.ma/jeux-consoles/accessoires-gaming/souris-gamers","id_store": 3, "subcategory":"Souris gamers"},
    {"link": "https://www.electroplanet.ma/informatique/accessoires/adaptateurs-it","id_store": 3, "subcategory":"Adaptateurs it"},
    {"link": "https://www.electroplanet.ma/informatique/accessoires/cable-d-imprimantes","id_store": 3, "subcategory": "Cable d imprimantes"},
    {"link": "https://www.electroplanet.ma/informatique/accessoires/chargeurs-pc","id_store": 3, "subcategory":"Chargeurs pc"},
    {"link": "https://www.electroplanet.ma/informatique/accessoires/connectique-reseau","id_store": 3, "subcategory":"Connectique reseau"},
    {"link": "https://www.electroplanet.ma/informatique/accessoires/pack-petits-peripheriques","id_store": 3, "subcategory": "Pack petits peripheriques"},
    {"link": "https://www.electroplanet.ma/informatique/accessoires/multiprises-et-parasurtenseurs","id_store": 3, "subcategory": "Multiprises et parasurtenseurs"},

    {"link": "https://www.electroplanet.ma/informatique/peripheriques-informatique/claviers","id_store": 3, "subcategory": "Claviers"},
    {"link": "https://www.electroplanet.ma/informatique/peripheriques-informatique/haut-parleurs-et-enceintes","id_store": 3, "subcategory": "Haut parleurs et enceintes"},
    {"link": "https://www.electroplanet.ma/informatique/peripheriques-informatique/logiciels","id_store": 3, "subcategory": "Logiciels"},
    {"link": "https://www.electroplanet.ma/informatique/peripheriques-informatique/pointeurs-laser","id_store": 3, "subcategory": "Pointeurs laser"},
    {"link": "https://www.electroplanet.ma/informatique/peripheriques-informatique/souris","id_store": 3, "subcategory": "Souris"},
    {"link": "https://www.electroplanet.ma/informatique/peripheriques-informatique/support-ventilateur-pc","id_store": 3, "subcategory": "Support ventilateur pc"},
    {"link": "https://www.electroplanet.ma/informatique/peripheriques-informatique/webcam","id_store": 3, "subcategory": "Webcam"},
]

electroplanet_bagagerie = [
    {"link": "https://www.electroplanet.ma/informatique/bagagerie/sac-a-dos", "id_store": 3,"subcategory": "Sac a dos"},
    {"link": "https://www.electroplanet.ma/informatique/bagagerie/sacoche", "id_store": 3,"subcategory": "Sacoche"},
    {"link": "https://www.electroplanet.ma/informatique/bagagerie/sleeve", "id_store": 3,"subcategory": "Sleeve"},

]


electroplanet_smartphones = [
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/smartphone/iphone", "id_store": 3,"subcategory":"iphone"},
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/smartphone/telephone-android", "id_store": 3,"subcategory":"telephone-android"},
]

electroplanet_tablete_android = [
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/tablettes/ipad", "id_store": 3,"subcategory": "ipad"},
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/tablettes/tablettes-android", "id_store": 3,"subcategory": "tablettes-android"},
]

electroplanet_telephones = [
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/telephone/domestique", "id_store": 3,"subcategory": "Domestique"},
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/telephone/mobile", "id_store": 3, "subcategory": "Mobile"},
]


electroplanet_accessoires_smarphones = [
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/accessoires-smartphone/cover-de-protection", "id_store": 3, "subcategory": "Cover de protection"},
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/accessoires-smartphone/oreillettes-bluetooth", "id_store": 3, "subcategory": "Oreillettes bluetooth"},
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/accessoires-smartphone/perche-selfie-filaire", "id_store": 3, "subcategory": "Perche selfie filaire"},
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/accessoires-smartphone/perche-selfie-sans-fil", "id_store": 3, "subcategory": "Selfie sans fil"},
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/accessoires-smartphone/support-voiture", "id_store": 3, "subcategory": "Support voiture"},
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/accessoires-smartphone/support-voiture", "id_store": 3, "subcategory": "Support voiture"},
]

electroplanet_accessoires_tablettes = [
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/accessoires-tablettes/cover-de-protection","id_store": 3, "subcategory": "Tablettes cover de protection"},
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/accessoires-tablettes/support-voiture","id_store": 3, "subcategory": "Tablettes support voiture"},
]

electroplanet_alimenttion_et_charge = [
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/alimentation-et-charge/adaptateurs-telephone-tablette","id_store": 3, "subcategory": "Adaptateurs telephone tablette"},
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/alimentation-et-charge/batterie-power-bank","id_store": 3, "subcategory": "Batterie power bank"},
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/alimentation-et-charge/cablage","id_store": 3, "subcategory": "Cablage"},
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/alimentation-et-charge/chargeur","id_store": 3, "subcategory": "Chargeur"},
]

electroplanet_objet_connectes = [
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/objets-connectes/montre-connectes","id_store": 3, "subcategory": "Montre connectes"},
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/objets-connectes/montres-et-bracelets-connectes","id_store": 3, "subcategory": "Montres et bracelets connectes"},
]

electroplanet_accessoires_de_cuisine = [
    {"link": "https://www.electroplanet.ma/articles-cuisines/accessoires-de-cuisine/ustensiles-de-cuisine", "id_store": 3,"subcategory": "Ustensiles de cuisine"},
]

electroplanet_article_de_boisson = [
    {"link": "https://www.electroplanet.ma/articles-cuisines/article-de-boisson/cafetieres","id_store": 3, "subcategory": "Cafetieres"},
    {"link": "https://www.electroplanet.ma/articles-cuisines/article-de-boisson/mugs","id_store": 3, "subcategory": "Mugs"},
    {"link": "https://www.electroplanet.ma/articles-cuisines/article-de-boisson/thermos","id_store": 3, "subcategory": "Thermos"},
]

electroplanet_conservation_alimentaire = [
    {"link": "https://www.electroplanet.ma/articles-cuisines/conservation-alimentaire/boites", "id_store": 3,
     "subcategory": "Boites"},
]


electroplanet_cuisson_sur_feux = [
    {"link": "https://www.electroplanet.ma/articles-cuisines/cuisson-sur-feux/autocuiseur", "id_store": 3,"subcategory": "Autocuiseur"},
    {"link": "https://www.electroplanet.ma/articles-cuisines/cuisson-sur-feux/batterie-de-cuisine", "id_store": 3,"subcategory": "Batterie de cuisine"},
    {"link": "https://www.electroplanet.ma/articles-cuisines/cuisson-sur-feux/casserole", "id_store": 3,"subcategory": "Casserole"},
    {"link": "https://www.electroplanet.ma/articles-cuisines/cuisson-sur-feux/cocotte", "id_store": 3,"subcategory": "Cocotte"},
    {"link": "https://www.electroplanet.ma/articles-cuisines/cuisson-sur-feux/couscoussier", "id_store": 3,"subcategory": "Couscoussier"},
    {"link": "https://www.electroplanet.ma/articles-cuisines/cuisson-sur-feux/faitout", "id_store": 3,"subcategory": "Faitout"},
    {"link": "https://www.electroplanet.ma/articles-cuisines/cuisson-sur-feux/marmite", "id_store": 3,"subcategory": "Marmite"},
    {"link": "https://www.electroplanet.ma/articles-cuisines/cuisson-sur-feux/poele", "id_store": 3,"subcategory": "Poele"},
]

electroplanet_filtration_d_eau = [
    {"link": "https://www.electroplanet.ma/articles-cuisines/filtration-d-eau/carafe-filtrante", "id_store": 3,"subcategory": "Carafe filtrante"},
    {"link": "https://www.electroplanet.ma/articles-cuisines/filtration-d-eau/robinet-filtrant", "id_store": 3,"subcategory": "Robinet filtrant"},
]

electroplanet_moules_et_plats = [
    {"link": "https://www.electroplanet.ma/articles-cuisines/moules-et-plats/moules-a-four", "id_store": 3,"subcategory": "Moules a four"},
]

electroplanet_accessoires_gaming = [
    {"link": "https://www.electroplanet.ma/jeux-consoles/accessoires-gaming/camera", "id_store": 3,"subcategory": "Poele"},
    {"link": "https://www.electroplanet.ma/jeux-consoles/accessoires-gaming/support", "id_store": 3,"subcategory": "Poele"},
]


electroplanet_console = [
    {"link": "https://www.electroplanet.ma/jeux-consoles/consoles/consoles-play-station", "id_store": 3,"subcategory": 19},
    {"link": "https://www.electroplanet.ma/jeux-consoles/jeux-video/jeux", "id_store": 3,"subcategory": 19},
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
    '5W',
]

stockage_list = [
                 '32 Go',
                 '32Go',
                 '32 Gb' ,
                 '32Gb' ,
                 '32b' ,
                 '32G' ,
                 '128 Gb',
                 '128Gb',
                 '128G',
                 '128 Go',
                 '128G',
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

    for c in colors:
        if c.upper() in title:
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
    # tmp = price.split("MAD")[0]
    tmp = price.split()
    floatprice = "".join(tmp)
    floatprice = floatprice.replace("," , ".")
    return float(floatprice)
