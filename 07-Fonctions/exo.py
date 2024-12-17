#1)

def somme_liste(entiers: list[int]) -> int:
    
    s = 0
    for e in entiers:
        s += e

    return s

lst = [10,15,2,5,8]

r = somme_liste(lst)
print(r)

#2)
def moyenne_liste(entiers: list[int]) -> float:
    s = somme_liste(entiers)
    nb = len(entiers)
    return s / nb

print(moyenne_liste([1,2]))

#3)
def table_multiplication(nombre, premier_multiple, dernier_multiple):
    for i in range(premier_multiple, dernier_multiple + 1):
        print(f'{nombre} x {i} = {nombre * i}')



table_multiplication(11,1,12)

#4)

from mesfonctions import convertir_minutes_en_heures, convertir_heures_en_minutes, saisie_nombre_valide

while True:

    choix = input('''
1 - Convertir heures en minutes
2 - Convertir minutes en heures
3 - Quitter

''')
    if choix == '3':
        break

    if choix == '1':
        heures = input('Heures à convertir: ')
        while True:
            try:
                heures = int(heures)
                break
            except:
                print('nombre invalide')

        print(f'{heures}h = {heures * 60}m')

    if choix == '2':
        minutes = input('Minutes à convertir: ')
        while True:
            try:
                minutes = int(minutes)
                break
            except:
                print('nombre invalide')

        print(f'{minutes}m = {minutes // 60}h {minutes % 60}m')


print('>>>>>>>>>>>>>>>>>>>> code optimisé:')

while True:

    choix = input('''
1 - Convertir heures en minutes
2 - Convertir minutes en heures
3 - Quitter

''')
    if choix == '3':
        break

    if choix == '1':
        heures = saisie_nombre_valide('Heures à convertir')
        convertir_heures_en_minutes(heures)

    if choix == '2':
        minutes = saisie_nombre_valide('Minutes à convertir')
        convertir_minutes_en_heures(minutes)
