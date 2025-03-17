# Variable: est une zone mémoire (RAM) contenant une valeur typée
# En python il y'à plusieurs types de données:
# Types de bases:
# types numériques: int (entiers), float (réels), complex 
# type textuel: str (string)
# type boolean: true/false
# Types complèxes:
# type liste: range, tuple, list
# type ensemble: set
# type dictionnaire: dict

# Python pratique le typage dynamique. (En Java le typage est statique: int x = 10)
# C'est l'interpréteur qui détermine le type de la variable selon la valeur qu'on lui a affecté

entier = 10
my_bool = True
flottant = 10.5
chaine1 = 'ceci est une chaine'
chaine2 = "autre chaine"
my_complexe = 5 + 2j # j est le nombre imaginaire

print(entier)
print(my_bool)
print(chaine1)
print(chaine2)
print(my_complexe.real)
print(my_complexe.imag)

# Règles de nommage:
#1- Le nom d'une variables ne peut contenir que des lettres, chiffres et undescores(_) et commence
# soit par une lettre ou un underscore (pas d'accents, d'éspaces ou tiret du 6 -)
#2- Python est case sensitive (sensible à la casse): age at Age sont 2 variables différentes
#3- Pour les noms composés, Python utilise la syntaxe snake_case
# PascalCase: MyBoolean
# camelCase: myBoolean
# snake_case: my_boolean

entier = "test"
print(entier)

# Constante: est une variable dont le contenu ne peut être modifié.
# La notion de constante n'existe pas réellement, c'est juste une convention de nommage

MA_CONSTANTE = 10
MA_CONSTANTE = "test"

# Variables nulles:
x = None
print(x) 

print("******************** Type des variables")

i = 10
print(type(i))

f = 10.5
print(type(f))

s = 'test'
print(type(s))

print("******************** ID des variables")

x = 10
print(id(x))

y = x
print(id(y))

# On a une certaine liberté dans l'écriture des flottants:
f = 0.99
f = .99
f = 00.99

# Pour les grands nombres, cette syntaxe est valide:
n = 156_125_569
print(n)
print(type(n))

print("************* Conversions de types:")

f = 10.5
i = int(f)
print(i)

my_float = float(i)
print(my_float)

s = '65'
z = int(s)
print(z)
print(type(z))

nb1 = int(input('Premier nombre: '))
nb2 = int(input('Second nombre: '))

somme = nb1 + nb2
print("Somme = "+str(somme))

print("**************** Nombres aléatoires:")

import random

a = random.randint(1,10)
print(a)

