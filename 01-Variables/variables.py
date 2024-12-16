# Une variable est une zone mémoire contenant une valeur typée
# Types numériques: int, float, complex
# Type textuel: str
# Type boolean: bool
# Type collections: range, list, set, tuple, dict

# En java le typage est statique: int x = 10
# Python utilise le typage dynamique:

entier = 10
floattant = 10.5
chaine1 = 'ceci est une chaine'
chaine2 = "autre chaine"
complexe = 4 + 2j # j est le nombre imaginaire

print(entier)
# Conventions de nommage:
# - le nom d'une variable commence soit par une lettre soit par un underscore
# - Python est sensible à la casse
# - Pour les noms composés, Python utilise snake_case: my_int

# Constante: est une variable dont on ne peut pas modifier le contenu
# La notion de cosntante n'existe pas réellement en Python, c'est plus une convention 
# de nommage

MA_CONSTANTE = 10
#MA_CONSTANTE = "texte"

# Variables nulles: None
x = None
print(x)

print(">>>>>> Connaitre le type d'une variable:")

print(type(entier))
print(type(chaine1))
print(type(floattant))

print(">>>>> ID des variables:")

x = 10

print(id(x))
y = x

print(id(y))

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Conversion de type:")

v = 10.5
i = int(v)

print(i)

f = float(i)
s = str(i)

nb1 = int(input("Premier nombre: "))

nb2 = int(input("Second nombre: "))

somme = nb1 + nb2

print("somme = " + str(somme))

# On a une certaine liberté dans l'écriture des types flottants

n = 0.99
n = .99
n = 00.99

# Syntaxe valide pour les grands nombres:

nb = 123_456_789
print(nb)

print(">>>>>>>>>>>>>>>Nombres aléatoire:")

import random

a = random.randint(1,10)
print(a)