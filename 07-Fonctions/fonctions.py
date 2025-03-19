# Fonction: est un ensemble d'instructions réutilisable

# 2 types de fonctions:
# Fonction qui renvoie un résultat -> input()
# Fonction qui ne renvoie aucun résultat -> print() -> None

# Syntaxe:
# Bonne pratique: choisir des noms explicites en respectant la convention snake_case
# def nom_fonction(paramètres): bloc d'instructions

# Exemple d'une fonction

def my_fonction():
    print('my fonction........')

# Appelle de my_fonction:

my_fonction()

# Sans les parenthèses, il s'agit d'une variable contenant l'id de la fonction en mémoire
my_fonction
print

print(my_fonction)

f = my_fonction
f()

# Exemple d'une fonction avec des paramètres (arguments)

def repeter(message, nombre_de_fois):
    # for i in range(nombre_de_fois):
    #     print(message)

    compteur = 0
    while True:
        print(message)
        compteur += 1
        if compteur == nombre_de_fois:
            break

repeter('hello', 5)

# Exemple d'une fonction qui renvoie un résultat

def carre(nombre):
    r = nombre ** 2
    return r

resulat = carre(5)

def addition(nombre1, nombre2):
    return nombre1 + nombre2

print(addition(10, 15))
#print(addition(10, 'test'))

# Annotations de types:
# Depuis Python 3.5, le langage propose un moyer d'indiquer aux déveoppeur le type de paramètres attendus par une fonction

x:int = 10
s:str = 'test'
b:bool = True

x = 'test'
# Même en pratiquant les annotations de types, le typage reste dynamique
print(x)

def somme(nb1:int, nb2:int) -> int:
    return nb1 + nb2

print(">>>>>>>>>>>>>> Fonctions avec des paramètres optionnels:")

def fct(x, alpha=10,beta=11):
    print(x,alpha,beta)

fct(100) # elle utilise les valeurs initiales de alpha et beta
fct(150,15,16) # on a la possibilité de modifier en cas de besoin les valeurs initiales des paramètres de la fct

# Les paramètres optionnels possèdent une valeur par défaut et sont définis après les paramètres obligatoires

# Appelle d'une fonction avec des paramètres nommés sans tenir compte de leur position dans la fonction
fct(beta=99,x=15)

def prix_ttc(prix_ht:float, tva:float=0.2) -> float:
    return prix_ht * (1 + tva)

print(prix_ttc(80))
print(prix_ttc(tva=0.35, prix_ht=80))

print('test1', end=' ')
print('test2')
print('test', 10,True,10.5, 15)

print(">>>>>>>>>> Fonction avec un nombre variable de paramètres:")

def somme_variable(*entiers: int) -> int:
    #*entiers: est un tuple (liste non modifiable)

    s = 0
    for e in entiers:
        s = s + e

    return s

print(somme_variable(10,20))
print(somme_variable(10,20,30))
print(somme_variable(10,20,30,40))


print('>>>>>>>>>>> Fonction plusieurs résultats:')

def somme_produit(x:int, y:int) :
    s = x + y
    p = x * y
    return s,p

resultat = somme_produit(10,15)
print(resultat)
print(type(resultat))

# Unpacking - déballage d'un tuple: extraire les éléments d'un tuple


sm,pr = resultat
print(sm)
print(pr)

print(">>>>>>>>>>>> Variable locale - Variable globale:")

# b et c sont globales: visibles dans tout le script
b = 10
c = 10

def modifier_variables():
    global b # demande explicite à la fonction pour manipuler la variable globale b
    b = 15
    c = 15
    v = 11
    # variables locales: sont définies dans une fonction -> non visibles en dehors de la fonction
    print("======================================================")
    print(locals())
    print("======================================================")


modifier_variables()

print(f'b = {b}')
print(f'c = {c}')

print(globals())

print(">>>>>>>>>>>>>>>> Fonctions natives de Python:")

lst = [10,5,20]
print(sum(lst)) # somme
print(len(lst)) # taille: nombre d'élément
print(min(lst))
print(max(lst))
print(round(3.5689, 2))

import statistics

print(statistics.mean(lst)) # moyenne

quit() # arrêter l'exécution d'un script

print('suite du script.......................')
   