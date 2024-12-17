
import math

math.sqrt(25)

# On peut aussi modifier le nom du module importé

import random as rd

rd.randint(1,10)

# On peut aussi importer des éléments spécifiques à partir d'un module

from random import randint

randint(1,10)

# On peut aussi modifier e nom de l'élément spécifique importé

from math import sqrt as racine_carree

racine_carree(25)

# On peut aussi importer tous les éléments d'un module
# Syntaxe la moins utilisée en pratique: on doit connaitre toutes les fcts du module

from math import *


# Un Module Python est fichier .py qui contient généralement des fonctions, des classes
# ou des constantes

# Un Package Python, est un répertoire contenant des modules
# Pour convertir un répertoire en package python, ce dernier doit contenir le fichier
# __init__.py, qu'on peut laisser vide.

# Python < 3.3: __init__.py est obligatoire
# Python >= 3.3: __init__.py n'est pas nécessaire mais il recommandé de le générer.

# Obligation: le nom d'un package ou d'un module doit en miniscules, sans éspaces ni 
# undescrore et doit commencer par une lettre

# Appeler fonction1:

from mypackage.myfunctions import fonction1

# Un module importé est toujours exécuté

# __name__ == '__main__' pour un module exécuté
# __name__ == 'nom_module' pour un module importé

#print(__name__)

# Import des éléments du module
from mypackage.myconstantes import SERVER,PORT,USER,PASSWORD

# Import du module
from mypackage import myconstantes
