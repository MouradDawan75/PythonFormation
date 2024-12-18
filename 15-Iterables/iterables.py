# Les collections de Python sont des itérables.
# Itérables ordonnés: list, tuple et str
# Itérables non ordonnés: dict - set

print('-----------enumerate: utilisable uniqueent avec les itérables ordonnés')

prenom = 'jean'

for e in enumerate(prenom):
    print(e) # e est un tuple contenant (index, valeur_associée
    
lst = ['a','b','c']

for i in enumerate(lst):
    print(i)

print('>>>>>>>>>>>> Valeurs dites vraies:')

print(bool(1))
print(bool(-1))
print(bool("chaine non vide"))
print(bool([1,2])) # collection non vide
print(bool(True)) 

chaine = ""

if chaine:
    print('chaine non vide')
else:
    print('chaine vide')



print('>>>>>>>>>>>> Valeurs dites fausses:')
print(bool(0))
print(bool('')) # chaine vide
print(bool([])) # collection vide
print(bool(None)) 
print(bool(False)) 

print(">>>>>>>>>>>>>>> Fonctions: all et any")

print(">>> All:")

iterable1 = [0,1,0,1]
iterable2 = [0,0,0,0]
iterable3 = [1,1,1,1]
iterable4 = [0,1,2,3]
iterable5 = ['a','b','c']

# all: permet de vérifier si toutes les valeurs dans une collection sont vraies
print(all(iterable1))
print(all(iterable2))
print(all(iterable3)) # True
print(all(iterable4))
print(all(iterable5)) # True

print(">>> any:")
# permet de vérifier qu'au moins une valeur est vraie dans une collection

print(any(iterable1))
print(any(iterable2)) # False
print(any(iterable3))
print(any(iterable4))
print(any(iterable5))

# Autres fonctions natives:
len(iterable1)
sum(iterable1)
min(iterable1)
max(iterable1)

print(">>>>> Iterator")

# Objet permettant de faire des itérations sur une collection

prenoms = ('Marc','Jean','Fabrice')

# récupérer l'Iterator: c'est une sorte de curseur pointant vers les éléments dela collection
it = iter(prenoms) 

print(next(it))
print(next(it))
print(next(it))

# Syntaxe pour faire des conversions: type(valeur_a_convertir)

# x est une varibale de type int - x est une instance de la class int
x = 10

if type(x) == int:
    print('x est un entier')

# isinstance est une fct native permattant de vérifier le type d'une variable
print(isinstance(x, int))
