# Fonction: est un ensemble d'instructions réutilisable
# 2 types de méthodes:
# Procédure: est une méthode qui ne renvoie aucun résultat (Ex: print())
# Fonction: est une méthode qui renvoie un résultat (ex: input())

# Syntaxe pour créer des fcts:
# def nom_fonction(params): instructions


def fonction1():
    print('contenu de fct1......')

# Appel de fct1:
fonction1()

# Sans les parenthèses, il s'agit d'une variable contenant l'id de la fonction en mémoire
print(fonction1)

f = fonction1
f()
print(type(f))

# Exemple d'une fct avec des params:

def repeter(message,nb_affichage):
    # for i in range(nb_affichage):
    #     print(message)
    x = 0
    while x < nb_affichage:
        print(message)
        x += 1


repeter('hello', 5)

# Exemple d'une fct qui renvoie un résultat:

def carre(nb):
    return nb ** 2

r = carre(5)
print(r)

def somme(x,y):
    return x+y

print(somme(5,10))

# print(somme("test",10))

# Depuis Python 3.5, ajout des annotations de types:
# Mécanisme qui permet zaux dév de spécifier le types de params attendus par une fct

x:int = 10
s:str = 'test'
b:bool = False

b = 'test'

def add(x:int, y:int) -> int:
    return x+y

print(">>>>>>>>>>>>>> Fonction avec des paramétres optionnels:")

# Les params optionnels, possèdent une valeur par défaut et sont définis après
# les params obligatoires

def fct(x, alpha=10, beta=15):
    print(x,alpha,beta)

fct(99)

fct(99,50,60) # en cas de besoin on peut modifier les valeurs initiales des params optionnels

# Appeler une fct avec des pamaétres nommnés sans tenir compte de leur position
# dans la fct

fct(beta=55, x=11)
print('texte1', end=" ")
print('texte2')

def prix_ttc(prix_ht: float, tva:float = 0.2) -> float:
    return prix_ht * (1 + tva)


print(prix_ttc(80))
print(prix_ttc(60))
print(prix_ttc(60, tva=0.35))

print(">>>>>>>>>>>>> Fonction qui renvoie plusieurs résultats:")

def calculs(x,y):
    s = x+y
    p = x*y
    return s,p
    
r = calculs(10,5)
print(type(r))
print(r)

# Eclater un tuple:
my_somme,my_produit = calculs(10,5)
print("somme = ",my_somme)
print("produit = ",my_produit)

print(">>>>>>>>>>>> Fonction qui accèpte en entrée un nbre varaible de params:")

print(10, True, 'test', 10.5)

def somme_variable(*entiers:int) -> int:
    # entiers est un typle à taille variable
    s = 0
    for e in entiers:
        s += e

    return s

print(somme_variable(10,5))
print(somme_variable(10,5, 6))
print(somme_variable(10,5, 6, 10))

print(">>>>>>>>>>>>> Fonction qui prend en param une autre fonction:")

def addition(x,y):
    return x+y

def soustraction(x,y):
    return x-y

def multi_calculs(fct, x,y):
    return fct(x,y)

print(multi_calculs(addition, 10,5))
print(multi_calculs(soustraction, 10,5))
print(multi_calculs(lambda x,y: x*y, 10,5))

print(">>>>>>> Quelques natives de Python:")

lst = [10,2,30, 42,12]

sum(lst)
min(lst)
max(lst)
len(lst)
round(2.55668,2)

def sup10(x):
    return x > 10

print(list(filter(sup10, lst)))

# Expression Lambda: fonction anonyme  appelée aussi fct à une seule instruction avec un 
# return implicite

produit = lambda x,y: x*y 
print(produit(10,5))


# Les expressions lambda sont utilisées dans fcts qui prennent en params d'autres fcts
print(list(filter(lambda x: x > 30, lst)))

print(">>>>>>>>>>>>> Variables locales - Variables globales:")

# b et c sont globales visibles dans tout le script

b = 10
c = 10

def modif():

    # les params définis dans une fct sont appelés variables locales
    # visibles uniquement dans la fct

    global b
    b = 15
    c = 15
    v = 20
    print("====================================")
    print(locals())
    print("====================================")

modif()

print(f'b = {b}')
print(f'c = {c}')

print(globals())

