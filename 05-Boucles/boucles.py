# Bloc répététif:
# for:
# 1- sert à parcourir tous les éléments d'une collection
# 2- Traitement répététif dont le nombre d'itérations est connu

# while: boucle conditionnelle
# - Traitement répététif dont le nombre d'itérations n'est pas connu, mais dépendant d'une condition

print(">>>>>>>>>> Boucle for:")

#1- Parcourir tous es élément d'une collection
# range est une fonction qui renvoie une collection d'entiers allant de 0 à n-1
nombres = range(10)  #de 0 à 9

for e in nombres:
    print(e)

prenom = "thomas"

for caractere in prenom:
    print(caractere)

#2- Traitement répététif avec un nbre d'itérations connu
# Affichez hello 5 fois dans la console

for i in range(5):
    print('hello')

print(">>>>>>>>>> Boucle while:")

x = 0
# Affichez la chaine hello tant que x est inférieur à 5

while x < 5:
    print('hello')
    x += 1

# Demandez la saisie d'un nombre compris entre 1 et 10.
# Tant que le nombre saisi n'est pas valide, redemandez la saisie d'un autre

print(">>>>> Boucle while infinie:")
# Boucle infinie: explicite
while True:
    nb = int(input('Votre nombre: '))
    if nb > 1 and nb < 10:
        break

#quit() : permte de mettre fin au script

print(">>>>> Boucle while finie:")
# Boucle finie: condition explicite

nb = 0

while not( nb > 0 and nb < 10):
    nb = int(input('Votre nombre: '))

# Demandez la saisie d'un nombre pair. Tant que le nombre n'est pas, redemandez
# la saisie d'un autre

while True:
    nb = int(input('Nombre pair: '))
    if nb % 2 == 0:
        break


nombres = range(10)
for e in nombres:
    print(e)
    # sortir si l'élément en cours est égal à 5
    if e == 5:
        break


print(">>>>>> break et continue:")

prenom = "sylvain"

for lettre in prenom:

    if lettre == 'y':
        continue # force le passage à l'itération suivante -> la suite de la boucle n'est pas exécuté

    if lettre == 'i':
        break

    print(lettre) #slva
