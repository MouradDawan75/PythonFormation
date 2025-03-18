# ceci est un commentaire: ligne ignorée par l'interpréteur
# fonction d'écriture dans la console (terminal)
print("test affichage")

# fonction de lecture à partir du terminal
nom = input("votre nom:")
print(nom)

# Points importants:
# Connaitre la syntaxe: fstring -> Python >= 3.6 f"{variable}"
# Connaitre les types de données
# Savoir faire des contrôles: conditions -> match/case : Python >= 3.10
# Savoir gérer les traitements répététifs: boucles
# Savoir gérer les erreurs
# Savoir manipuler les collections 

import os, subprocess

p = subprocess.run(['ipconfig'], capture_output=True, text=True)
print(p.stdout)

