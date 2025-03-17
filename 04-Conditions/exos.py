#1)
nb = int(input('Votre nombre: '))

reste_division = nb % 2

if reste_division == 0:
    print('pair')
else:
    print('impair')

#2)
mot = input('Votre mot: ')

if 'e' in mot:
    print(f'{mot} contient e')
else:
    print(f'{mot} ne contient pas e')