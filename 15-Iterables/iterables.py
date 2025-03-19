# Les collections Python sont des itérables
# Les itérables ordonnés: list,tuple, str
# Les itérables: set, dict

print('>>>>> Enumerate:')

# utilisable uniquement avec les itérables ordonnés:

prenom = 'David'

for i in enumerate(prenom):
    print(i) # i est un tuple contenant (element, index)


lst = ['test','chaine']

for e in enumerate(lst):
    print(e)

print(">>>>>>>>>>>>>>> Valeurs dites vraies:")
print(bool(1))
print(bool(True))
print(bool(-1))
print(bool([1,2])) # collection non vide
print(bool('test')) # chaine non vide

chaine = '1'

if chaine:
    print('Chaine non vide')
else:
    print('chaine vide')

print(">>>>>>>>>>>>>>> Valeurs dites fausses:")
print(bool(0))
print(bool([])) # Collection vide
print(bool(''))
print(bool(None))
print(bool(False))

print(">>>>>>>>> Fonctions: all et any")
iterable1 = [0,1,0,1]
iterable2 = [1,1,1,1]
iterable3 = [0,0,0,0]
iterable4 = ['a','b', 'c','d']

print(">> all:")
# Vérifier si toutes les valeurs sont vraies
print(all(iterable1))
print(all(iterable2))
print(all(iterable3))
print(all(iterable4))

print(">> any:")
# Vérifier si au moins une valeur est vrais
print(any(iterable1))
print(any(iterable2))
print(any(iterable3))
print(any(iterable4))

# Autres fonctions natives:
len(iterable4)
sum(iterable4)
min(iterable4)
max(iterable4)