# Fonction: est un ensemble d'instructions réutilisable

# 2 types de fonctions:
# Fonction qui renvoie un résultat -> input()
# Fonction qui ne renvoie aucun résultat -> print() -> None

# Syntaxe:
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

