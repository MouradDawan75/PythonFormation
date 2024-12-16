import random

aleatoire = random.randint(1,100)

# Boucle For:

print('Devinez le nombre aléatoire compris entre 1 et 100:')

for i in range(1,7):
    nb = input('Votre nombre :')
    try:
        nb = int(nb)
        if nb == aleatoire:
            print(f'Trouvé en {i} tentatives. Alétoire = {aleatoire}')
            break

        if nb < aleatoire:
            print('PLus grand')
        else:
            print('Plus petit')

    except:
        print('Nombre invalide...')

print(">>>>>>>>>>> Solution avec une boucle while:")

TENTATIVE_MAX = 6
nb_tentative = 0

while nb_tentative < TENTATIVE_MAX:

    nb = input('Votre nombre :')
    nb_tentative += 1
    try:
        nb = int(nb)
        if nb == aleatoire:
            print(f'Trouvé en {nb_tentative} tentatives. Alétoire = {aleatoire}')
            break

        if nb_tentative == TENTATIVE_MAX:
            print(f'Perdu! Aléatoire = {aleatoire}')

        if nb < aleatoire:
            print('PLus grand')
        else:
            print('Plus petit')

    except:
        print('Nombre invalide...')