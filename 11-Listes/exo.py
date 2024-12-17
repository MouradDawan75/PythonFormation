#1) Construire une liste ne contenant que les nombres positifs
nombres = range(-10, 10)

nombres_positifs = [e for e in nombres if e >= 0] # pour un if sans else le for arrive en premier

#2) construire une nouvelle liste en inversant les nombres impairs: 0,-1,2,-3,4......

nombres = range(10)

# pour un if/else, le for arrive en dernier
nombres_inverses = [e if e % 2 == 0 else -e for e in nombres]

#3) Affichez le nombre d'éléments supérieurs à 3
lst = [3,6,5,2,9]

print(len([e for e in lst if e > 3]))

#4)  Différence entre 2 listes

listA = [1,2,3,4]
listB = [1,2]

# listA - listB

liste_difference = [e for e in listA if e not in listB]

print(liste_difference)

#5)

def somme_liste_entiers_pairs_distincts(entiers: list[int]) -> int:

    # Construire une liste ne contenant que les entiers pairs distincts
    lst = []

    for e in entiers:
        if e % 2 == 0 and e not in lst:
            lst.append(e)

    return sum(lst)

print(somme_liste_entiers_pairs_distincts([2,3,2,4,5,4,6]))