s = 'test'
s = s.upper()

# Les Types de base (str, int, float, bool) sont immuables 

texte = ' ceci est une chaine '

print(texte.upper())
print(texte.lower())
print(texte.strip()) # suppression des espaxes de début et de fin
print('ceci' in texte)
print(texte.startswith('ceci')) # False
print(texte.endswith('chaine ')) # True
print(texte.replace('e', 'a'))
print(texte.replace('e', 'a', count=1))
print(texte.index('c'))
print(len(texte))
print(texte.count('c'))
print(texte.find('une'))

print(texte.rstrip())
print(texte.lstrip())

print(">>>>>>>>>>> Découpage d'une chaine:")

tab = texte.split()

print(tab)

chaine = "mot1,mot2,mot3,mot4"

print(chaine.split(sep=",", maxsplit=2))

print("fichier.note.pdf".rsplit('.', maxsplit=1)[1])

# join: permet de construire une chaine à partir d'une liste de chaines

print(' '.join(['python','version','3.13']))

