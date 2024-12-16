# Bloc itératif:
# Si le nombre d'itérations est connu, on utilise la boucle for
# Si le nbre d'itérations n'est pas connu et que le bloc dépend d'une condition,
# on peut utiliser la boucle while

# For est pratique pour parcourir tous les éléments d'une collection

nombres = range(10) # renvoie une séquence d'entiers alant de 0 à n - 1
for e in nombres:
    print(e)

# Afficher la chaine hello 5 fois

for x in range(5):
    print('hello')

# while: boucle conditionnelle:

x = 0

while x < 5:
    print(x)
    x += 1

# Demandez la saisie d'un nombre compris etre 1 et 10 et lui redemander tant que le nombre 
# n'est pas bon

n = 0
while (not 1 <= n <= 10):
    n = int(input('Votre nombre:')) 

# Utilisation d'une boucle infinie
while True:
    n = int(input('Votre nombre:')) 
    if(1 <= n <= 10):
        break

print(">>>>>>> Parcourir une chaine ")

prenom = "roger"

for lettre in prenom:
    print(lettre)

taille = len(prenom)
compteur = 0

while compteur < taille:
    print(prenom[compteur]) # l'index dans une collection commence à 0
    compteur += 1


print(">>>>>>>>> break et continue:")

prenom = "sylvain"

for lettre in prenom:

    if lettre == 'y':
        continue # force le passage à l'itération suivante - la suite de la boucle n'est pas exécutée

    if lettre == 'i':
        break

    print(lettre) # slva

# Raccourcis clavier:
# Pour commenter des lignes sélectionnées: ctr + k + ctr + c 
# Pour décommenter des lignes sélectionnées: ctr + k + ctr + u 