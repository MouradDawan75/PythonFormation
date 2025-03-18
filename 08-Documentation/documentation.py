# Dette technique: désigne un code non documenté, mal documenté ou pas assez documenté
# Dans Vs Code: installer l'extension autodocstring
# Cette extension utilise la syntaxe Google dans la doc technique, qui est la plus utilisée dans Python

# Il est possibe de documenté un module

"""Ce module contient des fonction très utilies
"""

def somme(x:int, y:int) -> int:
    """Fonction qui renvoie la somme de 2 entiers

    Args:
        x (int): est un entier
        y (int): est un entier

    Returns:
        int: somme de x et y
    """
    return x+y

import math

print(math.__doc__) # doc du module math

print("*************************************")

# 2 syntaxes pour afficher la doc d'une fonction: __doc__ ou help

print(math.acos.__doc__)

print("*************************************")

print(help(math.sqrt))

print(__doc__) # doc de ce module (fichier en cours)

print(somme.__doc__) # doc de la fonction somme de ce module