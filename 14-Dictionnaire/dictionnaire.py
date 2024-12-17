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