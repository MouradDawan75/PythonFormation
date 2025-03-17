print(">>>>>>>>>>>>>> Opérateurs arithmétiques:")

print("** Addition:")
a = 7
b = 2
c = a + b
c += 2 # équivalent de c = c + 2
print(f"c = {c}")

print("** Soustraction:")
a = 7
b = 2
c = a - b
c -= 2 # équivalent de c = c - 2
print(f"c = {c}")

print("** Multiplication:")
a = 7
b = 2
c = a * b
c *= 2 # équivalent de c = c * 2
print(f"c = {c}")

print("** Division:")
a = 7
b = 2
c = a / b
c /= 2 # équivalent de c = c / 2
print(f"c = {c}")

print("** Division entière:")
a = 7
b = 2
c = a // b
c //= 2 # équivalent de c = c // 2
print(f"c = {c}")

print("** Reste de la division entière : Modulo")
a = 7
b = 2
c = a % b
c %= 2 # équivalent de c = c % 2
print(f"c = {c}")

print("** Puissance:")
a = 7
b = 2
c = a ** b
c **= 2 # équivalent de c = c ** 2
print(f"c = {c}")

print(">>>>>>>> Opérateurs de comparaison:")

# > >= < <= == (égalité) !=(différent): renvoient un boolean
nb1 = 5
nb2 = 7

print(nb1 > nb2)
print(nb1 >= nb2)
print(nb1 < nb2)
print(nb1 <= nb2)
print(nb1 == nb2)
print(nb1 != nb2)

print(">>>>>>> Opérateurs logiques:")
# and, or et not: renvoient un boolean
# Table logique
# A     B    A and B    A or B
# v     v       v          v
# v     f       f          v
# f     f       f          f
# 

print((nb1 < nb2) and (nb1 > 0)) # True  

nombre = int(input("Un nombre compris entre 1 et 10: "))
if nombre >= 1 and nombre <= 10:
    print('valide')
else:
    print('invalide')

print(">>>>>> Affectations multiples:")

# Si des variables sont du même et possèdent la même valeur, on peut faire:

v1=v2=v3=15
print(v1)
print(v2)
print(v3)

# Si des variables ne sont pas du même type, on peut faire: non recommandée en pratique

var1,var2,var3 = 25,True,"test"

print(">>>>>>>>>>>>>> Les opérateurs: is et in")

list1 = [1,2,3]
list2 = [1,2,3]

print(list1 == list2) # True: même contenu
print(list1 is list2) # False: 2 objets (id) différents en mémoire

print(id(list1))
print(id(list2))

# l'opérateur in permet de vérifier si un élément fait partie ou pas d'une collection

print(1 in list1) # True
print(5 in list2) # False

chaine = 'ceci est une chaine' # un objet str est une collection de caractères
print('ceci' in chaine)
print('Une' in chaine)

# re: regular expression
import re

txt = "test texte"
resultat = re.search("^test.*texte$",txt)
print(resultat)

# Pour des calculs complèxes, on peut importer le module math
import math

math.sqrt(16) # racine carrée
math.ceil(-4.7) # renvoie l'entier immédiatement supérieur: -4
math.exp(2)
math.factorial(3)
math.pow(5) # puissance