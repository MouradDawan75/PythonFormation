# Contrairement un fichier texte, un fichier json en plus du texte contient des données 
# (chaines, valeurs numériques, listes.......)

import os
import json

# Pour les fichiers JSON: 2 fcts load - dump

print(">>>>>>>>>>>>>>> Gestion des fichiers JSON avec: load() et dump()")

chemin_dossier = os.path.dirname(__file__)
chemin_json = os.path.join(chemin_dossier, 'users.json')

# Lecture d'un JSON:

with open(chemin_json, 'r', encoding='utf-8') as flux:
    contenu = json.load(flux)


#print(contenu) # contenu est une liste de dict

for user in contenu:
    print(f'Name: {user.get('name')} - Latitude: {user.get('address').get('geo').get('lat')}')
    print("===============================")
    print("_______________ Les clés du dict:")
    for cle in user.keys():
        print(cle)

        # Vérifier le type de la valeur associée à la clé
        # si c'est un dict -> lister les clés
        if isinstance(user.get(cle), dict):
            for key in user.get(cle):
                print("___________", key)


# Ecriture dans un fichier json:

chemin_sortie_json = os.path.join(chemin_dossier, 'sortie.json')

with open(chemin_sortie_json, 'w', encoding='utf-8') as flux:
    # Contruction du contenu à insérer
    # soit un dict - soit une liste de dict

    data = {
        "python" : "langage de programmation",
        "version" : "3.13"
    }

    json.dump(data,flux, indent=4, ensure_ascii=False) 
    # ensure_ascii=True -> tous les char non ascii seront ignorés

# Exo: à partir de users.json, construire un autre fichier resultat.json ne contenant 
# que les clés/valeurs name et email

# Etape 1: lecture de users.json - déjà effectuée à la ligne 14


# Etape 2: contruction du contenu à insérer: une liste de dict
liste_dict = []

for u in contenu:
    d = {
        'name': u.get('name'),
        'email': u.get('email')
    }
   

    liste_dict.append(d)


# Etape 3: insértion du contenir dans resultat.json
chemin_resultat = os.path.join(chemin_dossier, 'resultat.json')

with open(chemin_resultat, 'w', encoding='utf-8') as flux:
    json.dump(liste_dict, flux, indent=4, ensure_ascii=False)


# Pour les chaines JSON: 2 fcts loads - dumps -> pour convertir des chaines en objet (dict)

print(">>>>>>>>>>>>>>> Gestion des chaines JSON avec: loads() et dumps()")

player_str = '{"first_name": "FEDERER", "last_name": "Roger", "sport": "football"}'

#player_str = "{'first_name': 'FEDERER', 'last_name': 'Roger' ,'sport': 'football'}"

print(type(player_str)) # str

# Conversion d'une chaine json en objet (dict)
json_objet = json.loads(player_str)

print(type(json_objet)) # dict

print(json_objet['first_name'])
print(json_objet.get('first_name'))

# MAJ d'une clé d'un dict:
json_objet['sport'] = 'tennis'

print(json_objet)

# MAJ de plusieurs clés d'un dict:

autre_player_str = '{"first_name": "NADAL", "last_name": "Rafael", "sport": "tennis", "age": 36}'

autre_json_objet = json.loads(autre_player_str)

json_objet.update(autre_json_objet)

print(json_objet)

# Suppression d'une clé dans un dict:

# option1: utilisation du del
del json_objet['age']
print(json_objet)


# option2: utilisation de la fct pop()
json_objet.pop('sport')

print(json_objet)

# Conversion d'un objet JSON (dict) en str:

with open(chemin_json, 'r', encoding='utf-8') as flux:
    data = json.load(flux)

# data est une liste de dict

chaine = json.dumps(data)

print(chaine)

# Api Rest est un ensemble de ressources (images, article d'un journal...), où chaque ressource
# possède un ID (URI: Uniform Resource Identifier - end point), une méthode d'accès et elle
# peut être publique ou privée
# 
# Toutes ces infos sont founies via la documentation de l'api
# Une Api Rest n'est pas limitée au format JSON, elle peut renvoyée du texte, du xml, du binaire... 

# Pour faire à une api rest en Python, on utilise le module externe requests
# Pour gérer les modules externes, on utilise le pip

# 3 commandes à connaitre:
# pip instal nom_module
# pip uninstal nom_module
# pip list 

import requests

URI = "https://restcountries.com/v3.1/all"

# json(): permet de parser la réponse de l'api en json

reponse = requests.get(URI).json()

#print(reponse)
# reponse est une liste de dict

for pays in reponse:
    print(f'Name: {pays.get('name').get('common')}')