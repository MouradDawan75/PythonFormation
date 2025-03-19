#1)Nouvelle liste ne contenant que les nombres positifs
nombres = range(-10,10)


# Comprehension List:
nombres_positifs = [e for e in nombres if e >= 0] # pour un if sans else, le for arrive en premier

#Syntaxe classique:

nb_positifs = []

for e in nombres:
    if e >= 0:
        nb_positifs.append(e)



#2)Nouvelle liste en inversant les nombres impairs. Résultat attendu: 0,-1,2,-3,4,-5.......
nombres = range(10)


#Syntaxe Comprehension List:

nombres_inverses = [e if e % 2 == 0 else -e for e in nombres] # pour un if/else, le for arrive en dernier

print(nombres_inverses)

# Syntaxe classique

nb_inverses = []

for e in nombres:
    if e % 2 == 0:
        nb_inverses.append(e)
    else:
        nb_inverses.append(-e)

print(nb_inverses)

#3) Affichez le nombre d'éléments supérieurs à 3 dans cette liste
my_liste = [3,2,6,7,1,9,12,11]

#Syntaxe classique

compteur = 0
for e in my_liste:
    if e > 3:
        compteur += 1

print(compteur)

#Comprehension List
print(len([e for e in my_liste if e > 3]))

#4) Différence entre listA et listB

listA = [1,2,3,4]
listB = [1,2]

# Syntaxe classique

liste_difference = []

for e in listA:
    if e not in listB:
        liste_difference.append(e)


# Comprehension List:

liste_difference_resultat = [e for e in listA if e not in listB]
print(liste_difference)
print(liste_difference_resultat)

def difference_deux_listes(list1: list[int], list2: list[int]) -> list[int]:
    """Fonction qui renvoie la différence entre 2 listes d'entiers

    Args:
        list1 (list[int]): Liste d'entiers
        list2 (list[int]): Liste d'entiers

    Returns:
        list[int]: liste contenant uniquement les éléments de list1 ne faisant pas partie de list2
    """
    resultat = []
    for e in list1:
        if e not in list2:
            resultat.append(e)

    return resultat