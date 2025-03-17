# Bloc conditionnel:
# est un ensemble d'instructions qui ne s'exécute que si une condition est vérifiée

age = 12

if age < 18:
    print('mineur')
    print('toujours mineur')

print('fin du bloc....')

# Les 2 points (:) symbolisent le début d'un bloc d'instructions. Tant que les instructions ont indentées
# de la même façon, on est toujours dans le même bloc.

if age < 18:
    print('mineur')
elif age <= 25:
    print('jeune adulte')
else:
    print('adulte')

# On peut aussi combiner des conditions, en utilisant les opérateurs logiques:

age = 28

# les parenthèses sont optionnelles

if (age >= 18) and (age <= 25):
    print("Vous avez entre 18 et 25 ans")

age = 18
derogation = True
if (age >= 18) or (derogation == True):
    print('Au moins 18 ans ou avoir une dérogation')

# En Python, un bloc vide n'est pas valide syntaxiquement
# Néaumoins, il est possible de créer un bloc vide valide syntaxiquement en utilisant le mot clé pass

if age > 18:
    pass
    # a compléter

print('suite du script.....')

print(">>>>>>>>> Opérateur ternaire:" )
# Syntaxe qui permet de remplacer un if/else classique

# Syntaxe classique: plus lisible

if age < 18:
    print('mineur')
else:
    print('majeur')

# Syntaxe ternaire:

print('mineur') if age < 18 else print('majeur')

# Depuis Python 3.10, ajout de match/case. Syntaxe permettant de remplacer les elif qui s'imbriquent

note = 0

match note:

    case 0|1|2|3|4|5|6|7|8|9:
        print('En dessous de la moyenne')
    case 10|11|12|13|14:
        print('Juste la moyenne')

    # pour les autres cas:
    # 2 syntaxes:
    # case other:
    # case _:

    # case other:
    #     print('Good job')

    case _:
        print('Good job')


# Raccourcis clavier:
# commenter des lignes sélectionnées: ctr + k + ctr + u
# décommenter des lignes sélectionnées: ctr + k + ctr + u