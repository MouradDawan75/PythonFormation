# 1) Affichez tous les nombres de 1 à 15 inclus -> range

# sol1:
for i in range(16):
    if(i != 0):
        print(i)

# sol2:

for i in range(15):
    print(i+1)

# sol3: on peut aussi modifier l'index de départ qui commence à 0 par défaut
for i in range(1, 16):
    print(i)

# 2) Affichez tous les nombres pairs de 1 à 10 inclus -> range

# sol1:
for i in range(1,11):
    if(i % 2 == 0):
        print(i)

# sol2: on peut aussi modifier le pas de la fct range

for i in range(2,11,2):
    print(i)

#3)

while True:

    choix =  input = '''

     Choisir une opération:

    - Addition: tapez a
    - Soustraction: tapez s
    - Multiplication: tapez m
    - Division: tapez d
    - Quitter: tapez q
    '''

    # Gestion du break
    if choix == 'q':
        print('Fin du programme....')
        break

    # Gestion d'un choix invalide
    if choix not in 'asmd':
        print('Choix invalide')
        continue

    # Lecture des 2 floats
    nb1 = float(input('Premier nombre: '))
    nb2 = float(input('Second nombre: '))

    while True:
        if(choix == 'd' and nb2 == 0):
            print('Nombre 2 doit être différent de 0')
            nb2 = float(input('Second nombre: '))
            if(nb2 != 0):
                break

    # Affichage du résultat:
    match choix:

        case 'a':
            print(f'{nb1} + {nb2} = {nb1 + nb2}')

        case 's':
            print(f'{nb1} - {nb2} = {nb1 - nb2}')

        case 'm':
            print(f'{nb1} x {nb2} = {nb1 * nb2}')

        case 'd':
            print(f'{nb1} / {nb2} = {nb1 / nb2}')