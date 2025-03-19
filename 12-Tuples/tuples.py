#Tuple: est une collection ordonnée avec doublons autorisés.
# Un Tuple est une liste en lecture seule (liste constante)

# Tuple vide:
t1 = ()
t2 = tuple()

prenoms = ('Simon', 'Elodie', 'Antoine')

prenoms.count('Simon')
prenoms.index('Simon')

#prenoms[0] = 'Dawan'

# Unpacking: déballage d'un tuple: extraire les éléments d'un tuple

p1,p2,p3 = prenoms

print(p1)
print(p2)
print(p3)

# Modification d'un tuple:

#1- Conversion en liste
prenoms = list(prenoms)


#2- Application des modifications

prenoms.append('Dawan')
prenoms.remove('Simon')

#3- Conversion en tuple
prenoms = tuple(prenoms)

print(prenoms)