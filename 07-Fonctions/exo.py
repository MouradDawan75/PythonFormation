# 1) fonction qui renvoie la somme d'une liste d'entiers. 

def somme_liste(entiers):

    s = 0
    for e in entiers:
        s = s + e

    return s

lst = [10,58,12]
r = somme_liste(lst)
print(r)

# 2)fonction qui renvoie la moyenne d'une liste d'entiers.

def moyenne_liste(entiers):
    somme = somme_liste(entiers)
    #nombre_elements = len(entiers) -> len fonction qui renvoie la taille d'une collection

    nb_elements = 0
    for e in entiers:
        nb_elements += 1

    return somme / nb_elements


l = [10,15,20]
m = moyenne_liste(l)
print(m)

# 3) fonction qui affiche la table de multiplication d'un nombre où le premier et le dernier sont des paramètres

def table_multiplication(nombre, premier_multiple, dernier_multiple):
    for i in range(premier_multiple, dernier_multiple + 1):
        print(f'{nombre} x {i} = {nombre * i}')

table_multiplication(11,1,12)
table_multiplication(7,1,10)

# Menu:

while True:
    choix = input('''
        1) Convertir heures en minutes
        2) Convertir minutes en heures
        3) Quitter

    ''')

    if choix == '3':
        break

    if choix == '1':
        heures = int(input('Nombre heures: '))
        print(f'{heures}h = {heures * 60}m')

    if choix == '2':
        minutes = int(input('nombre minutes: '))
        print(f'{minutes}m = {minutes // 60}h {minutes % 60}m')


# Optimiser un script Python:

from mes_fonctions import afficher_menu, convertir_heures_en_minutes, convertir_minutes_en_heures, choix1, choix2


while True:
    choix = afficher_menu()

    if choix == '3':
        break

    if choix == '1':
        choix1()

    if choix == '2':
        choix2()


