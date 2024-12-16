print(">>>>>> Opérateurs arithmétiques:")

print("\t____Addition:")
a = 5
b = 3
c = a + b
c += 2 # c = c + 2 -> syntaxe simplifiée
print(f'c = {c}')

print("\t____Soustraction:")
a = 5
b = 3
c = a - b
c -= 2 # c = c - 2 -> syntaxe simplifiée
print(f'c = {c}')

print("\t____Multiplications:")
a = 5
b = 3
c = a * b
c *= 2 # c = c * 2 -> syntaxe simplifiée
print(f'c = {c}')

print("\t____Division:")
a = 5
b = 3
c = a / b
c /= 2 # c = c / 2 -> syntaxe simplifiée
print(f'c = {c}')

print("\t____Division entière:")
a = 5
b = 3
c = a // b
c //= 2 # c = c // 2 -> syntaxe simplifiée
print(f'c = {c}')

print("\t____Reste de la division entière:")
a = 5
b = 3
c = a % b
c %= 2 # c = c % 2 -> syntaxe simplifiée
print(f'c = {c}')

print("\t____Puissance:")
a = 5
b = 3
c = a ** b
c **= 2 # c = c ** 2 -> syntaxe simplifiée
print(f'c = {c}')

print(">>>>>>>>>>>>> Opérateurs de comparaison:")

# > >= < <= == (égalité) != (différent)

print(">>>>>>>>>>>>> Opérateurs logiques:")

# and (et logique) or (ou logique) ! (non logique)

# A     B    A and B    A or B
# v     f       f          v
# v     v       v          v
# f     f       f          f

print((a > 0) and (a < b))  

print(">>>>>> Affectations multiples:")

# Si des variables sont du mm type et possèdent la mm valeur, on peut faire:
v1=v2=v3=10

print(f'v1 = {v1}')
print(f'v2 = {v2}')
print(f'v3 = {v3}')

v3 = 16

print(f'v1 = {v1}')
print(f'v2 = {v2}')
print(f'v3 = {v3}')

# Si des variables ne sont pas du mm type, on peut faire:

var1,var2,var3=10,True,'test' # syntaxe non recommandée en pratique

print(">>>>>> Opérateurs: is et in")

list1 = [1,2,3]
list2 = [1,2,3]

print(list1 == list2) # True: car le mm contenu
print(list1 is list2) # Fase: car 2 objets (ids) différents en mémoire

# L'opérateur in permet de vérifier si un élement fait partie ou pas d'une collection
print(1 in list1)
print(5 in list2)

prenom = "roger" # une chaine est une collection de caractéres

print('r' in prenom)
print('er' in prenom)

list3 = [1,2]

print(list3 in list1) # False: car ist1 ne contient que des int

list4 = [1,2,3,[1,2]]

print(list3 in list4)