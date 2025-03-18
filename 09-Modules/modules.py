# Les différentes syntaxes pour les imports

import math,random,statistics

math.sqrt(25)

# On peut aussi modifier le nom du module importé: définir des alias

import random as rd

rd.randint(1,10)

# On peut aussi importer des éléments spécifiques à partir d'un module

from math import sqrt,acos,cos
sqrt(25)

# On peut aussi modifier le nom de l'élément spécifique importé

from math import sqrt as racine_carree

racine_carree(25)

# Un module Python est un fichier (.py) contenant générelement des fonctions, des classes ou des constantes
# Un package est un répertoire contenant des modules.

# Important: le nom d'un module ou d'un package doit être en miniscules, sans éspace ni undescore et doit commencer par une lettre.

# Pour convertir un répertoire en package Python, ce dernier doit contenir le fichier __init__.py qu'on peut laisser vide.

# Pour les versions Python < 3.3: __init__.py est obligatoire
# Pour les versions Python >= 3.3: __init__.py n'est pas nécessaire pour un package Python, mais il est recommandé de le générer 
# comme même pour des raisons de compatibilité 

# Appeler fonction1() définie dans myfunctions.py

# Option1: importer la fonction
from mypackage.myfunctions import fonction1


#Option2: importer tout le module
#from mypackage import myfunctions

# Un module importé est toujours exécuté
# Comment empécher l'exécution d'un module importé?

# Pour un module exécuté: __name__ == '__main__'
# Pour un module importé: __name__ == 'nom module importé'

from mypackage.myconstantes import SERVER,PASSWORD,USER,PORT

# Lecture des variables d'environnement de windows
import os

os.environ.get('PYTHON_TEST')



