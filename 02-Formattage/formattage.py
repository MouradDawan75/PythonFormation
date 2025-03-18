age = 50
prenom = "Marie"

# Concaténation: En Python, on ne peut concaténer que des chaines
print("Prénom: "+prenom+" Age: "+str(age))

# Utiliser une virgule comme séprateur: Pas besoin de convertir les types numérique en str, de plus
# la virgule génère un éspace
print("Prénom:",prenom,"Age:",age)

# A partir de Python 3: ajout de de la fonction format
print("Prénom: {} Age: {}".format(prenom,age))

# A partir de Python 3.6: ajout de fstring -> syntaxe simplifiée de la fonction format
print(f"Prénom: {prenom} Age: {age}")

# Entre accolades: on peut soit insérer des variables, soit des des expressions

print(f"{3 + 5}") # exemple d'une expression
print(f"{int(10.5)}")

print(">>>>>>>>>> Chaines multilignes:")
# chaine verbatime

print("""
    Ceci est une
chaine sur 
plusieurs lignes.
""")

print('''
    Ceci est une
chaine sur 
plusieurs lignes.
''')

# Caratères d'échappement:
# \n\r: retour à la ligne
# \t: tabulation
# \b: back space
# \s: space
# \': ignorer '
# \": ignorer les "
# \\: ignorer le \ 

print("\tCeci est une\nchaine sur\nplusieurs lignes.")

print("ceci \"est\" une chaine")

chemin = "c:\\test\\notes.txt"
print(chemin)

print("Prénom:",prenom,"Age:",age, sep="/")