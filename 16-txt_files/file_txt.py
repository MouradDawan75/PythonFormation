
# module permattant la gestion paths

import os

#Etape 1: construire le chemin du fichier:

#chemin_fichier = "c:\\notes.txt"

print(__file__) # contient le chemin du fichier en cours: c:\......\file_txt.py

chemin_dossier_en_cours = os.path.dirname(__file__) # c:\...\16-txt_files

#chemin_fichier = chemin_dossier_en_cours+"\\notes.txt"

#join: fct qui génère un chemin valide selon l'os utilisé
chemin_fichier = os.path.join(chemin_dossier_en_cours, 'demo.txt')

#Etape 2: appeler la fct open()
# Elle prend plusieurs params:
# - chemin du fichier
# - mode d'accès: r: read - w: wrtie - a: append
#             poue les modes: w et a, si le fichier n'existe pas, il sea crée par la fct open
# - encoding: utf-8

# stream (flux): est une sorte de canal intermédiaire entre une source et une destination

flux = open(chemin_fichier,'a',encoding='utf-8') 
flux.write('ceci est le contenu du fichier.....')
flux.close()

# Lecture d'un fichier:
#1- construction du chemin
#2- Appel de la fct open

flux = open(chemin_fichier,'r', encoding='utf-8')
contenu = flux.read()
flux.close()

print(contenu)

# Context Manager (with resource): à la fin du bloc le context manager
# s'occupe de liberer la ressource utilisée

print('>>>>>>>>>>>>>>>>>> Context Manager:')

with open(chemin_fichier,'r', encoding='utf-8') as fichier:
    print(fichier.read()) # Vous arrivez à la fin du fichier, 
                           # la prochiane lecture n'aura aucun caractère à lire
    fichier.seek(0) # seek: permet de remettre le curseur au début du fichier
    # seek(5): renvoie le 6ème caractère
    # whence = 0 - partir du début du fichier
    # whence = 1 - partir de la position actuele du curseur
    # whence = 2: partir de la fin du fichier
    #flux.close() - code exécuté par le with
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    print(fichier.read())

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

#print(fichier.read())

from filehelper import lecture_fichier_texte, ecriture_fichier_texte

chemin_fichier = os.path.join(chemin_dossier_en_cours,'myFile.txt')

ecriture_fichier_texte(chemin_fichier, 'contenu du fichier........', mode_ajout=True)

print(lecture_fichier_texte(chemin_fichier))

print("******************* Module os:")
print(os.getcwd()) # renvoie le chemin du dossier principal: c:\\

# Création de répertoire:

chemin_dossier = os.path.join(chemin_dossier_en_cours, 'rep')

if os.path.exists(chemin_dossier):
    print('Dossier existant...')
else:
    os.mkdir(chemin_dossier)

print(">>>>>>> Parcourir un rép:")

for f in os.listdir(chemin_dossier_en_cours):
    print(f)

# Exo: Lire tous les fichiers .txt du dossier en cours et insérer le contenu dans un fichier
# spy.txt
# Contenu de ce fichier doit ressembler à:
# >>>>>>>>>>>>>> nom_fichier_lu
# contenu

contenu = ""

for f in os.listdir(chemin_dossier_en_cours):

    if f.endswith('.pdf'):
        chemin = os.path.join(chemin_dossier_en_cours,f)
        contenu += ">>>>>>>> "+f+'\n'+lecture_fichier_texte(chemin)+'\n'


if contenu:
    chemin_sortie = os.path.join(chemin_dossier_en_cours, 'spy.txt')
    ecriture_fichier_texte(chemin_sortie, contenu)
else:
    print('Aucun fichier trouvé........')
