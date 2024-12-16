# Il existe 3 types d'erreurs possibles:
# - Erreur de compilation (de syntaxe): eles sont détectées automatiquement par l'IDE
# - Exception: est une erreur qui provoque l'arrêt de l'application
# - Code fonctionnel qui renvoi un résultat inattendu - faire du debbugage

# Pour éviter l'arrêt de l'application, les exceptions doivent gérées
# Pour gérer les les exceptions, on utilise le boc try-except

# Il existe plusieurs types d'exceptions, chacune d'elle porte le nom de l'erreur qu'elle
# génère.
# Il existe aussi un type anonyme (générique), Exception

nb = input('votre nombre: ')

try:
    nb = int(nb)
    print(10 / 0)
    

except ZeroDivisionError:
    print('exception gérée......')

except ValueError:
    print('conversion gérée.....')

print('>>>>>>>>>>>>>>>>>>>>>> type générique:')

# Obligatoire: une ressource (fichier, bd..) doit être libérée à la fin de son utilisation.

nb = input('votre nombre: ')

try:
    nb = int(nb)
    print(10 / 0)
    # Ouverture d'un fichier en lecture
    

# except Exception as e:
#     print('exception générique gérée......')
#     print(e)

# syntaxe simplifiée du type générique
except:
    print('exception gérée...')

else:
    # bloc optionnel qui s'exécute si aucune erreur n'est générée dans le try
    print('bloc else.......')

finally:
    # boc optionnel qui s'exécute tout e temps: exception ou pas
    print('bloc finally.....')
    # # Fermeture du fichier 
    # Sert dans la pratique à libérer les ressources utilisées dans le try

# Lecture d'un nombre saisi valide:
while True:
    nb = input('Votre nombre:')
    try:
        nb = int(nb)
        #break
        

    except:
        print('Nombre invalide....')

    else:
        break




print('suite du script................')