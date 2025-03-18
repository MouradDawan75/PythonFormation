import random
import os

aleatoire = random.randint(1,100)

for i in range(6):

    if i < 5:
        print(f'{i+1} tentative')
    else:
        print('Dernière tentative')

    
   
    nombre = input('Votre nombre: ')
    os.system('cls') # commande clear screen 

    try:
        nombre = int(nombre)
        if nombre == aleatoire:
            print(f'Trouvé. Alatoire = {aleatoire}')
            break

        if nombre < aleatoire:
            print('Plus grand')
        else:
            print('Plus petit')

        if i == 5:
            print(f'Perdu! Aléatoire = {aleatoire}')

    except:
        print('Nombre invalide...')


print(">>>>>>>>>>>>>>> Boucle while:")

compteur = 0

while True:

    nb = input('Votre nombre: ')
    compteur += 1
    try:
        nb = int(nb)
        if nb == aleatoire:
            break

        if compteur == 6:
            break

        if nb < aleatoire:
            print('Pus grand')
        else:
            print('Plus petit')

    except:
        print('Nombre invalide.....')