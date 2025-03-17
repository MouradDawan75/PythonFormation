#1)Affichez tous les nombres de 1 (inclus) à 10 (inclus) -> range

#Sol1:
for i in range(11):
    if i != 0:
        print(i)

#Sol2:
for i in range(10):
    print(i+1)

#Sol3: On peut modifier l'index de départ de range: commence à 0 par défaut
for i in range(1,11):
    print(i)


#2)Affichez tous les nombres pairs de 1 (inclus) à 10 (inclus) -> range

# Sol1:
for i in range(1,11):
    if i % 2 == 0:
        print(i)

# Sol2: On peut modifier le pas de range: égal à 1 par défaut
for i in range(2,11,2):
    print(i)

#3)

while True:

    choix = input('''
        Choisir une opération

        - Addition: tapez a 
        - Soustraction: tapez s
        - multiplication: tapez m 
        - Division: tapez d 
        - Quitter: tapez q 

    ''')

    # Gestion de la sortie de la boucle infinie
    if choix == 'q':
        print('Fin du programme....')
        break

    # Gestion d'un choix saisi invalide:
    if choix not in 'asmd':
        print('Choix invalide')
        continue

    # Demandez 2 nombres
    nb1 = float(input('Premier nombre: '))
    nb2 = float(input('Second nombre: '))

    # Gestion de la division par 0
    if(choix == 'd' and nb2 == 0):
        # demandez un second nombre différent de 0. Tant que nb2 n'est pas différent de 0: 
        # redemandez la saisie d'un autre
        while True:
            nb2 = float(input('Second nombre différent de zéro: '))
            if( nb2 != 0):
                break


    # Afficher le résutat:
    match choix:

        case 'a':
            print(f'{nb1} + {nb2} = {nb1 + nb2}')

        case 's':
            print(f'{nb1} - {nb2} = {nb1 - nb2}')

        case 'a':
            print(f'{nb1} x {nb2} = {nb1 * nb2}')

        case 'd':
            print(f'{nb1} / {nb2} = {nb1 / nb2}')
 
