import requests
import os,csv,json

# Un environnement virtuel est une copie de Python

# Bonnes Pratiques:

################################## Au début d'un projet, on crée un env. virtuel 
# contenant les modules externes nécessaires au projet en question

# Pour créer un env. virtuel, on utilise le module venv de python

# Dans le terminal (Vs Code ou Windows):
# 1- python -m venv nom_de_l'env._virtuel (la copie générée est celle de la version Python sélectionnée dans Vs Code)

# 2 -Activer l'env. virtuel en exécutant le fichier activate.bat qui se trouve dans myenv\scripts: .\myenv\Scripts\activate

# Si le terminal de Power Shell em^cher l'exécution du fichier d'activation:

# Démarrez le terminal PowerShell en tant qu'admin
# et exécutez a commande suivante:
# Set-ExecutionPolicy RemoteSigned et réponse par O pour oui

# Dans Vs Code vérifiez que l'intérpéteur sélectionné est celui de l'env. virtuel


##################################### A la fin du projet:
# on génère un fichier .txt contenant la liste des modules externes installés dans l'env. virtuel nécessaires au fonctionnement du projet

# Commande a exécuter dans le terminal:
# pip freeze --local > requirements.txt


# Pour installer les modules listés dans requirements.txt:
# Commande dans le terminal:

# pip install -r requirements.txt

print('test')

# Dans le site Python:
# vérifiez la version de l'interpréteur et la date de fin de support
# Dans pypi: vérifiez la date de la dernière mise à jours des modules externes installés