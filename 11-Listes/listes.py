# list: est une collection ordonnée avec doublons autorisés

# Listes vides:

l1 = []
l2 = list()

notes = [2,6,7,9]

# Ajouts

notes.append(9)
print(notes)

notes.insert(1,9)
print(notes)

# Modifications:
notes[1] = 50
print(notes)

# Suppressions:

notes.remove(9)
print(notes)

notes.pop()
print(notes)

print(">>>>>>>>>>> Atteindre un élément d'une liste:")

notes = [2,6,7,9]

print(f'Première note: {notes[0]}') # l'index commence à 0
print(f'Dernière note: {notes[len(notes) - 1]}')

# Python autorise les indexs négatifs

print(f'Dernière note: {notes[-1]}')

print(">>>>>>>>>>>>>> Parcourir une liste:")

notes = [2,6,7,9]


print('>>> For:')

for n in notes:
    print(n)

print(">>> while:")

i = 0
while i < len(notes):
    print(notes[i])
    i += 1

print(">>> For + index:")

for n in range(len(notes)):
    print(notes[n])

print(">>>>>>>>>>>>> Slicing:")

# Slicing: mécanisme permettant de créer des sous listes à partir de listes existantes,'Marc

prenoms = ['Jean','Marie','Marc','Juliette']

list1 = prenoms[0:3] # de index 0 à 2 (n - 1)
print(list1) 

list2 = prenoms[:3] # du début jusqu'à n - 1
print(list2)

list3 = prenoms[:] # du début jusqu'à la fin - copie
print(list3)

list4 = prenoms[::2] # du début jusqu'à la fin avec un pas de 2
print(list4)

print(">>>>>>>>> Comprehension List:")

# mécanisme permettant de créer de nouvelles listes à partir de listes existantes
# en modifiant le contenu des listes de départ

nombres = range(10)

# Construire une nouvelle liste en doublant tous les éléments de la liste de départ

# syntaxe classique

nombres_doubles = []

for e in nombres:
    nombres_doubles.append(e * 2)

# Syntaxe Comprehension List:

new_list = [e * 2 for e in nombres]
print(new_list)

# Cette syntaxe autorise l'utilisation de fcts:

nombres = range(10)

def carre(x):
    return x ** 2

liste_nombres_carres = [carre(e) for e in nombres]

print(liste_nombres_carres)

nombres = range(10)

# Nouvelle liste ne contenant que les nombres pairs:

nombres_pairs = [e for e in nombres if e % 2 == 0]

print(nombres_pairs)

print(">>>>>>>>>>>>> Multiples conditions:")

nombres = range(10)

# nouvelle liste e contenant que les nombres pairs supérieurs à 2

# 2 syntaxes:

# Utilisation des opérateurs logiques: and

lst1 = [e for e in nombres if e % 2 == 0 and e > 2]

# Utiisation de plusieurs if:

lst2 = [e for e in nombres if e % 2 == 0 if e > 2]

print(">>>>>> random pour les listes:")

from random import choice, sample, shuffle

cartes = [x for x in range(1,11)]

print(">>>> choice: un élément aléatoire à partir d'une liste")
print(choice(cartes))

print(">>>sample: ensemble d'éléments aléatoires:")

print(sample(cartes, k=5))

print(">>>>>shuffle: mélanger les éléments d'une liste")

shuffle(cartes)
print(cartes)