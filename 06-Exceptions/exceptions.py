# Il y'à 3 types d'erreurs:
# Erreurs de compilation (syntaxe): elles sont détectées automatiquement par l'IDE
# Exceptions: se sont des erreurs qui provoquent l'arrêt de l'application
# Code fonctionnel qui renvoi un résultat inattendu - faire du debbugage

# Pour éviter l'arrêt de l'application, on doit gérer l'exception.
# Pour gérer une exception, on utilise le bloc try/except

# Il existe plusieurs types d'exceptions, chacune d'elle porte le nom de l'erreur qu'elle génère.
# Il existe aussi un type générique (Exception) qu'on  peut utiliser aussi.



try:
    chaine = 'test' + '5'
    print(10 / 2)
    

except ZeroDivisionError:
    print('exception gérée......')

except TypeError:
    print('exception concaténation gérée.....')


print(">>>>>>>>>>>>> Type générique Exception:")


# Obligation: une ressource (fichiers, base de données...) doit être libérée à la fin de son utilisation.

try:
    chaine = 'test' + 5
    print(10 / 2)
    # Ouverture d'un fichier en lecture/écriture
    
    
    

# except Exception as ex:
#     print('exception générique gérée......')
#     print(ex)
#     #ex contient les détails de l'exception générée

# syntaxe simplifiée de except Exception :
except:
    print('exception générique gérée......')
    

else:
    # bloc optionnel qui s'exécute si aucune erreur n'est générée par le try
    print('bloc else.......')
    

finally:
    # bloc optionnel qui s'exécute tout le temps: exception ou pas
    print('bloc finally......')
    #fermeture du fichier
    #Dans la pratique, le bloc finally sert à libérer les ressources utlisées dans le try

# Tant que le nombre saisi n'est pas valide, le user doit saisir un autre

while True:
    nb = input('Votre nombre:')
    try:
        nb = int(nb)
        

    except:
        print('Nombre invalide....')

    else:
        print(nb)
        break


print('suite du script.........')

