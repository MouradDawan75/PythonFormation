chaine = 'test'

chaine = chaine.upper()

print(chaine)

# Les objets de type string sont immuables

print(">>>>> Fonctions sur les chaines:")

texte = ' ceci est une chaine '

print(texte.strip()) # supprime les éspces au début et la fin 
print(texte.startswith('ceci')) # False
print(texte.endswith('chaine ')) # True
print(texte.upper()) # majuscules
print(texte.lower()) # miniscule
print(texte.count('ceci'))
print(texte.index('ceci'))
print(texte.capitalize())
print('Taille:', len(texte)) # prend en compte les espaces

print(">>> rstrip - lstrip")

print(texte.rstrip())
print(texte.lstrip())

print(">>>> Découpage d'une chaine")
mots = texte.split()

print(mots)

chaine_csv = 'mot1,mot2,mot3,mot4'

print(chaine_csv.split(sep=','))

print(chaine_csv.split(sep=',', maxsplit=2))

fichier = "test.txt.pdf"

# Extension d'un fichier
print(fichier.rsplit(sep='.', maxsplit=1)[1])


texte = ' ceci est une chaine '
print(texte.replace('e', 'a'))
print(texte.replace('e', 'a', 2))

# join: inverse de split: permet de cosntruire une chaine en choisissant un séparateur

print(' '.join(['ceci', "est", 'un', 'paragraphe']))

s = '12589'

print(s.isdigit())
print(s.isnumeric())
print(s.islower())
print(s.isupper())

saisie = input('Votre nombre: ')

if(saisie.isnumeric()):
    nb = int(saisie)
    print(nb)
else:
    print('Que des chiffres......')


