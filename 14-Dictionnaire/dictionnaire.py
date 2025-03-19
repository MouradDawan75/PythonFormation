#dict: est une collection non ordonnée qui fonctionne par association clé:valeur (avec une syntaxe JSON)
# Dans un dictionniare physique, le mot est la clé, sa définition est la valeur.
# Les clés dans un dictionnaire sont uniques.

# dict vide:

d1 = {}
d2 = dict()

# Un dict est utilisé pour regrouper les caractéristques d'un objet

user = {
    "nom" : "DUPONT",
    "prenom": "Jean",
    "age" : 65
}

# Afficher le nom:
print(user["nom"])
#print(user["Nom"]) > si clé inexistante -> Exception

print(user.get('nom'))
print(user.get('Nom')) # None-> si clé inexistante -> renvoie None

# On peut avoir aussi des dictionnaires complèxes:

utilisateur = {
    "nom" : "DUPONT",
    "prenom": "Jean",
    "age" : 65,
    "telephones" : ['06060606', '070707070'],
    "adresse" : {
        "rue": "15 rue Machin",
        "code_postal" : 75015
    }
}

# Affichez chaque num. de tél:
for t in utilisateur.get('telephones'):
    print(t)

# Affichez le nom de la rue:
print(utilisateur.get('adresse').get('rue'))

# On peut compléter un dict: ajouter des clés

utilisateur['contrat'] = 'CDD' # si clé inexsitante: elle sera créée

print(utilisateur)

utilisateur['contrat'] = 'CDI' # si clé existante: elle sera écrasée

print(utilisateur)

print(">>>>>>>>>>>>>>>>> Parcourir un dictionnaire:")

d = {
    "a" : 1,
    "b" : 2
}

print(">>>> For par défaut:")
# renvoie uniquement les clés
for element in d :
    print(element)


print(">>> For sur les clés:")

for cle in d.keys():
    print(f'Clé: {cle} - Valuer: {d.get(cle)}')


print(">>> For sur les valeurs:")

for v in d.values():
    print(v)


print(">>>> For sur les items")
for i in d.items():
    print(i) # i est un tuple (clé, valeur)

# Unpacking: déballage d'un tuple

for cle,valeur in d.items():
    print(cle, valeur)

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Appelle d'une API Rest:")

# WebService REST ou  API REST: est une application sans IHM (interface homme/machine) - c'est un style d'architecture

# Api REST: Representation State Transfert: n'est  pas limitée au format JSON: elle peut renvoyée du texte, du xml et du binaire (fichiers)
# Il s'agit d'un ensemble de ressources (images, article d'un journal....) 
# où chaque ressource possède un ID (URI: Uniform Resource Identifier - appelé aussi endpoint), une méthode d'accès (GET, DELETE, POST, PUT) et elle
# peut être publique ou privée

# Toutes ces infos sont fournies dans la documentation de l'API

# Pour utiliser des API Rest en Python, il faut installer le module requests
# pip: gestionnaire des modules externes

# pip install nom_module
# pip uninstall nom_module
# pip list

# pypi est le réferentiel en ligne des modules Python

# import requests

# URI = 'https://restcountries.com/v3.1/all'

# #json(): permet de formatter le contenu en json

# reponse = requests.get(URI).json()

# #print(reponse) c'est une liste de dictionniares

# country = input('Votre pays: ')

# for pays in reponse:
#     if pays.get('name').get('common') == country:
#         print(f"Nom: {pays.get('name').get('common')} - Capitale: {pays.get('capital')} - Population: {pays.get('population')}")
#         print('Pays limitrophes:')
#         print(pays.get('borders'))
#         for code in pays.get('borders'):
#             details = requests.get(f'https://restcountries.com/v3.1/alpha/{code}').json()
#             print(f"Nom: {details[0].get('name').get('common')}")

print(">>>>> Dictionary Comprehension:")

d = {
    "a" : 1,
    "b" : 2
}

# Inverser le dict d:
# Syntaxe classique:

resultat = dict()

for k,v in d.items():
    resultat[v] = k


print(resultat)

# Syntaxe Dictionay Comprehension:

result = {v:k for k,v in d.items()}
print(result)

dict1 = {'a':1, 'b':2, 'c':3, 'd': 4, 'c': 5}

# nouveau dict en doublant les valeurs de dict1

dict2 = {k:v*2 for k,v in dict1.items()}

print(dict2)

# A partir de dict1, construire un nouveau dict ne contenant que les valeurs paires supérieures à 2

dict3 = {k:v for k,v in dict1.items() if v % 2 == 0 if v > 2}

print(dict3)

print(">>>>>>>>>>>>>>>>>>>> Complément chapitre Fonctions:")

def func(*args, **kvagrs):
    #print(type(args)) # tuple -> pour les paramètres anonymes
    #print(type(kvagrs)) # dict -> pour les paramètres nommées
    print(args)
    print(kvagrs)
    
    
    
func(1,2)
func(x=10,y=20)

def generate_dict(**params):
    return params


print(generate_dict(nom='DUPONT',prenom='Jean',age=60))
print(generate_dict(axe_x=['nom','prénom'], axe_y=['DUPONT','Jean']))