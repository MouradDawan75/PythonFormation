# list: est une collection ordonnée avec doublons autorisés

# Listes vides:

l1 = []
l2 = list()

# En Python, il n'ya aucune restriction sur le type des éléments d'une liste

demo = [10,True,11.5,'test', [10,False]]

# Dans la pratique, on crée souvent des listes cohérentes d'objets

notes = [2,6,7,9]

# Ajouts:

notes.append(6)
print(notes)

# L'index dans une collection commence à 0
notes.insert(0,10)
print(notes)

# Modifications

notes[0] = 50
print(notes)

# Suppressions

#supprime l'élément fournit en paramètre
notes.remove(6)
print(notes)

# supprime et renvoie le dernier élément par défaut
element_supprime = notes.pop()
print(notes)
print(element_supprime)

# count et index:

print(notes.count(50))
print(notes.index(50))

print(">>>>>> Atteindre un élément d'une liste:")
notes = [2,6,7,9]

taille = len(notes) # 4

print(f'Première note: {notes[0]}')
print(f'Dernière note: {notes[taille - 1]}') # index commence à 0

# Python autorise les indexs négatifs

print(f'Dernière note: {notes[-1]}')
print(f'Avant dernière note: {notes[-2]}')

print(">>>>>>>>>>>>> Parcourir une liste:")

notes = [2,6,7,9]

print(">>> For:")

for n in notes:
    print(n)

print(">>> While:")

taille = len(notes)
index = 0
while index < taille:
    print(notes[index])
    index += 1


print(">>> For + l'index:")

for i in range(len(notes)):
    print(notes[i])


print(">>>>> Les autres fonctions:")

notes = [2,6,7,9]

# Inverser la liste
notes.reverse()

print(notes)

# Trier la liste
notes.sort()

print(notes)

# Etendre la liste
notes.extend([10,15])

print(notes)

print(">>>>>>>>>> Slicing:")

# Slicing: mécanisme permettant de construite des sous listes à partir de listes existantes sans les modifier

prenoms = ['Simon', 'Elodie', 'Younes', 'Alain','Mourad', 'Dawan', 'Antoine']

list1 = prenoms[0:3] # de index 0 à 2 (n-1)
print(list1)

list2 = prenoms[:3] # du début jusqu'à 2 (n-1)
print(list2)

list3 = prenoms[:] # du début jusqu'à la fin -> une copie
print(list3)

list4 = prenoms[::2] # du début jusqu'à la fin avec un pas de 2
print(list4)

# Affichez les 3 premiers éléments de la liste
print('>>>>> 3 premiers')

print(prenoms[0:3])

# Affichez les 3 derniers éléments de la liste
print('>>>>> 3 derniers')
print(prenoms[-3:])

# Supprimer les 3 premiers éléments de la liste

print('>>>>>suppression des 3 premiers')
print(prenoms[3:])

print(prenoms) # liste de départ non modifier suite à la suppression


print('>>>>>suppression des 3 premiers et remplacement de la liste de départ')
prenoms = prenoms[3:] #écraser la liste de départ

print(prenoms)