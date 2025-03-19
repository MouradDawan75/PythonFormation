#Set: est une collection non ordonnée sans doublons. De plus, le type Set supporte les opérations sur les ensembles
# telles que l'union, l'intersection, la différnce et la différence symétrique

# Set vide:
s = set()


panier = {'Pomme', 'Banane', 'Pomme', 'Orange'}

print(panier)


a = set('abracadabra') #conversion d'une chaine en set
b = set('alacazam')

print(a)
print(b)

print('>>>Union:')
# lettres dans a ou dans b ou dans les deux
#2 syntaxes:

print(a | b)
print(a.union(b))

print(">>> Intersection:")
# lettres dans a et dans b
# 2 syntaxes:
print(a & b)
print(a.intersection(b))

print('>>> Différence:')
# lettres dans a mais pas dans b
# 2 syntaxes:
print(a - b)
print(a.difference(b))

print(">>> Différence symétrique:")
# lettres dans a ou dans b mais pas dans les 2
# 2 syntaxes:
print(a ^ b)
print(a.symmetric_difference(b))

# Suppression des doublons dans une liste
lst = [1,1,2,2,3,3]

lst = set(lst) # conversion en set -> pour supprimer: risque de perte de l'index
lst = list(lst) # conversion en list

print(lst)

print(">>>> Set supporte la syntaxe Comprehension Set")

ensemble = set('abracadabra')

# Construire un nouveau set ne contenant que les lettres différentes de a,b et c

# Syntaxe classique:
result = set()

for lettre in ensemble:

    # if lettre != 'a' and lettre !='b' and lettre != 'c':
    #     result.add(lettre)

 
    if lettre not in 'abc':
        result.add(lettre)


print(result)

# Comprehension Set

ensemble_new = {lettre for lettre in ensemble if lettre not in 'abc'}