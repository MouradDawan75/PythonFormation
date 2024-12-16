age = 38
prenom = "Roger"

print(">>>>> Concaténation:")

print("Prénom: "+prenom+" Age: "+str(age))

print(">>>> Utiliser la virgule comme séparateur:")

print("Prénom:",prenom,"Age:",age)

# Depuis Python 3, ajout de la fonction format

print("Prénom: {} Age: {}".format(prenom,age))

# Depuis Python 3.6, ajout de fstring -> syntaxe simplifiée de la fct format

print(f"Prénom: {prenom} Age: {age}")

# Entre accolades, on peut soit insérer des variables, soit des expressions

print(f"{3 + 5}") # exemple d'une expression
print(f"{int(10.55)}")

# Caractéres d'échappement:
# \n: retour à la ligne
# \t: tabulation
# \s: space
# \b: backspace

print("\tCeci est une\nchaine sur\nplusieurs lignes")

chemin = "c:\\test\\notes.txt"

chaine = "ceci est \"une\" chaine" 

print(">>> Chaines multilignes:")
# Chaine verbatime:

texte = """
    Ceci est une
chaine sur 
plusieurs lignes
"""

print(texte)