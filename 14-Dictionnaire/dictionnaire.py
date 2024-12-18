# dict: est une collection non ordonnée qui fonctionne par association clé:valeur
# Dans un dictionnaire physique, le mot est la clé, sa définition est la valeur.
# Dans un dict les clés sont uniques

# Syntaxe dict vide:

d1 = {}
d2 = dict()

d = {
    "python" : "langage de programmation",
    "version" : "13.3"
}

# Un dict peut être utilisé pour regrouper les caractéristiques d'un objet

user = {
    "nom" : "DUPONT",
    "prenom" : "Marc",
    "age" : 60
}

print(user["nom"])
# print(user["Nom"]) -> si clé inexistante -> renvoie une exception

print(user.get('nom'))
print(user.get('Nom')) # si clé inexistante -> renvoie None

# si la clé n'existe pas: elle sera créée avec la valeur associée
user['contrat'] = 'CDD'
print(user)

# si la clé existe, sa valeur est remplacée
user['contrat'] = 'CDI'
print(user)

# On peut aussi avoir des dict complèxes:

utilisateur = {
    "nom" : "DUPONT",
    "prenom" : "Marc",
    "age" : 60,
    "telephones" : ['06060606','07070707'],
    "adresse" : {
        "rue" : "3 rue Machin",
        "code_postal" : 92000
    }
}

# Affichez chaque num. de tél.:
for t in utilisateur.get('telephones'):
    print(t)

# Affichez la rue:
print(utilisateur.get('adresse').get('rue'))

# Exo

# Demandez la saisie d'un mot. Construisez un dictionnaire dont les clés sont les caractéres
# et les valeurs sont le nombre d'occurrence de chaque caractére dans le mot saisi
# Ex: test -> {"t": 2, "e": 1, "s": 1}

mot = input('Votre mot: ')
d = {}

for lettre in mot:
    d[lettre] = mot.count(lettre)

print('___________Parcourir un dict:')

d = {
    'a': 1,
    'b': 2
}

# Le for par défaut ne renvoie que les clés

for element in d:
    print(f'Clé: {element} - Valeur: {d.get(element)}')

# For sur les clés via a fct keys():
for cle in d.keys():
    print(cle)

# For sur les valeurs via la fct values()
for value in d.values():
    print(value)

for item in d.items():
    print(item) # item est tuple contenant (clé,valeur)

# item est un tuple, on peut extraire ses éléments
for k,v in d.items():
    print(k,v)