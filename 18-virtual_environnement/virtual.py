
# Un environnement virtuel est une copie de l'installation de python qui est sensée contenir
# les modules externes nécessaires au projet en cours.

#################### Etapes à mettre en place au début d'un projet
# 1- Créer un env. virtuel en utilisant le module venv de Python
# Commande à exécuter dans le terminal: python -m venv myenv (nom_env_virtual)
# 2- Activer l'env. virtuel en exécutant le fichier myenv/scripts/activate
# commande à exécuter dans le terminal: .\myenv\Scripts\activate

# Si Power Shell bloque l'exécution du fichier activate
# Démarrer PS en tant qu'admin
# Exécutez cette commande: Set-ExecutionPolicy RemoteSigned -> répon dre par O

# Dans vs code -> choisir la version Python de myenv (en bas à droite)n

# 3- Instaler les modules externes nécessaires au projet en cours


########################## Etapes à mettre en place à la fin du projet
# On génère un fichier (requirements.txt) contenant la liste des modules externes utilisés
# dans le projet

# Commande à exécuter dans le terminal:
# pip freeze --local > requirements.txt
# 
# Pour installer les modules listés dans requirements.txt:
# commande dans le terminal: pip install -r requirements.txt
 

import os
import json

# Pour les fichiers JSON: 2 fcts load - dump

print(">>>>>>>>>>>>>>> Gestion des fichiers JSON avec: load() et dump()")

chemin_dossier = os.path.dirname(__file__)
chemin_json = os.path.join(chemin_dossier, 'videos.json')

with open(chemin_json, 'r', encoding='utf-8') as flux:
    contenu = json.load(flux)

print(type(contenu))

chaine = json.dumps(contenu)

print(chaine.count('Video'))
print(chaine.count('type'))


# lst = []
# for dictionnaire in contenu.get('items'):
#     d = dictionnaire.get('payload')

#     for cle in d.keys():
#         if cle == 'type':
#             lst.append(contenu.get(cle))

# print(len(lst))


    
