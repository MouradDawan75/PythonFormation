# set (ensemble): c'est une collection non ordonnée sans doublons
# De plus, ce le type set supporte les opérations sur les ensembles telles que l'union,
# l'intersection, la différence et la différence symétrique

# Syntaxe pour déclarer un ensemble vide:
e = set()

panier = {"pomme", "banane", "pomme", "orange"}

print(panier)

a = set('abracadabra') # conversion d'une chaine en set
b = set('alacazam')

print(">>>> Union:")
# lettres dans a ou dans b ou dans les 2
# 2 syntaxes:

print(a | b)
print(a.union(b))

print(">>> Intersection:")
# lettres dans a et dans b
#  syntaxes:

print(a & b)
print(a.intersection(b))

print(">>> Différence")
# a - b: lettres dans a mais pas dans b
# 2 syntaxes:
print(a - b)

print(a.difference(b))

print(">>>> Différence symétrique:")
# lettres dans a ou dans b mais pas dans les 2
# 2 syntaxes:
print(a ^ b)
print(a.symmetric_difference(b))

# Le type Set supporte la syntaxe Comprehension Set

ensemble = set('abracadabra')

# Construire un nouvel ensemble ne contenant que les lettres différentes de a,b et c

resultat = {lettre for lettre in ensemble if lettre not in 'abc'}

print(resultat)