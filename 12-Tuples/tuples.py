# tuple: est une collection ordonnée avec doublons autorisés (c'est un liste en lecture seule)

# tuple vide:

t1 = ()
t2 = tuple()

prenoms = ("Marc","Marie","Jean")

# Eclater un tuple:

p1,p2,p3 = prenoms
print(p1)
print(p2)
print(p3)

# Modification d'un tuple:

#1 - Conversion en liste

prenoms = list(prenoms)

#2- Application des modfis:

prenoms.append('Dawan')
prenoms.remove('Jean')

#3- Conversion en tuple

prenoms = tuple(prenoms)

print(prenoms)