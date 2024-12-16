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

