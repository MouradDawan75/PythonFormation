
# Fonction de lecture d'un fichier texte
# Pour générer la documentation technique des fonctions:
# Dans vs code: ajoutez l'extension autodocstring

def lecture_fichier_texte(chemin_absolut: str) -> str:
    """Fonction de lecture d'un fichier texte.

    Args:
        chemin_absolut (str): Chemin complet du fichier à lire.
        Ex: c:\\dossier\\fichier.txt

    Raises:
        Exception: Génère une exception si le chemin est invalide.

    Returns:
        str: Renvoie le contenu du fichier
    """

    try:
        with open(chemin_absolut, 'r', encoding='utf-8') as flux:
            contenu = flux.read()

        return contenu

    except Exception as e:
        #raise: mot clé permettant de soulever des exceptions
        # garder une trace du e dans un fichier de logs
        raise Exception('Chemin invalide.....')


# Fonction d'écriture dans un fichier texte

def ecriture_fichier_texte(chemin_absolut: str, contenu: str, mode_ajout: bool = False) -> None:
    """Fonction d'écriture dans un fichier texte.

    Args:
        chemin_absolut (str): _Chemin complet du fichier. Ex: c:\\dossier\\fichier.txt
        contenu (str): Contenu à insérer dans le fichier
        mode_ajout (bool, optional): Pourun accès en mode ajout, mettre ce parm à True 

    Raises:
        Exception: Si le chemin est invalide, la fct génère une exception
    """
    mode = 'w'
    if mode_ajout:
        mode = 'a'
        contenu = '\n'+contenu
    try:
        with open(chemin_absolut,mode,encoding='utf-8') as flux:
            flux.write(contenu)

    except Exception as e:
        #garder une trace du e dans un fichier de logs
        raise Exception('Chemin invalide......')