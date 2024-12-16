# Bloc conditionnel: est un ensemble d'instructions qui ne s'exécute que si une condition
# est vérifiée

age = 26

if age > 18:
    print("Majeur")
    print("Toujours majeur")

print("Fin du bloc if")

# Les : (2 points) représentent le début d'un bloc. Tant que les instrutions sont indentées
# de la mm façon, on est toujours dans le mm bloc

if age < 18:
    print('mineur')
elif age <= 25:
    print('jeune adulte')
else:
    print("majeur")

if age > 18 and age <= 25:
    print('Jeune adulte')

# Syntaxe simpifiée, pour remplacer le and logique
if 18 < age <= 25:
    print('Jeune adulte') 

# Opérateur ternaire: syntaxe simplifiée permettant de rempacer le if/else classique
# ou de faire des affectations conditionnelles

# if/else classique:

if age < 18:
    print('mineur')
else:
    print('majeur')

# Syntaxe ternaire:

print('mineur') if age < 18 else print('majeur')

resultat = None

if age < 18:
    resultat = 'mineur'
else:
    resultat = 'majeur'

# Syntaxe ternaire:
resultat = 'mineur'  if age < 18 else 'majeur'

# Depuis Python 3.10, ajout du match/case:

note = 5

match note:

    case 0|1|2|3|4|5|6|7|8|9:
        print('En dessous de la moyenne')

    case 10|11|12|13:
        print('Juste la moyenne')

    # Pour les autres cas, 2 syntaxe:
    # soit case other:
    # soit case _:

    # case other:
    #     print('Good job')

    case _:
        print('Good job')

# Un bloc vide n'est pas valide syntaxiquement. Le mot clé pass permet de définir
# un bloc vide valide syntaxiquement

if age < 18:
    pass

print('Fin')
