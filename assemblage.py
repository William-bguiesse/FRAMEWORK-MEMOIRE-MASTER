import glob 
from lecteur import MarkdownReader 
from convertisseur import Convertisseur

# 1. Récupérer tous les fichiers markdown avec glob.
fichier_a_lire = glob.glob("*.md")
fichiers_valides = [f for f in fichier_a_lire if f.lower() != "readme.md"]
# on règle un problème en excluant le fichier README.md de la liste des fichiers à lire.

if not fichiers_valides:
    print("Aucun fichier Markdown trouvé pour la conversion.")
# si aucun fichier markdown n'est trouvé, le "if not" equivaut à une liste vide. 
# On affiche donc un message d'erreur expliquant qu'aucun fichier n'a été trouvé pour la conversion.

else:
    print("--- Fichiers Markdown disponibles ---")
    for index, fichier in enumerate(fichiers_valides, start=1):
        print(f"{index}. {fichier}") 
# ici, on crée une lsite des fichiers markdown, et avec enumerate, on indexe un numero à chacun
# pour faciliter le choix pour l'utilisateur dans la selection de ces derniers. 
# 1. On va utiliser "input" pour que l'utilisateur tape le numero qui est indexé à chaque fichier. 
# 1. On demande le numéro
    choix = input("\nEntrez le numéro du fichier : ")

    # 2. On modifie un peu le code pour s'assurer que la réponse de l'utilisateur soit bien d
if choix.isdigit() and 1 <= int(choix) <= len(fichiers_valides):
    fichier_selectionne = fichiers_valides[int(choix) - 1]
    print(f"Fichier choisi : {fichier_selectionne}")
    
    # on va creer une variable "lecteur" qui va contenir le fichier selectionné par l'utilisateur 
    # lors de la commande input précédemment utilisé.
    lecteur = MarkdownReader(fichier_selectionne)
    texte = lecteur.read_file()
    # Avec le convertisseur du fichier convertisseur.py, on va pouvoir importer notre méthode
    # qui nous permet la conversion du md en HTML.
    convertisseur = Convertisseur(texte)
    html = convertisseur.conversion_en_html()

# On affiche ici le résultat du fichier converti.
    print("\n--- Résultat HTML ---")
    print(html)
# maintenant, on ne veut pas juste une sortie print dans le terminal, on veut un fichier HTML. 
# L'objectif sera de creer une variable qui stockera le fichier qui a été converti.
# Avec la commande "rplit" on dit à python : 
# DECOUPE AU PREMIER POINT QUE TU VOIS EN PARTANT DE LA DROITE ET GARDE LE PREMIER ELEMENT 
# PUIS, AJOUTE ".htm" A LA FIN DU MOT.
    nom_de_sortie = fichier_selectionne.rsplit(".", 1)[0] + ".html"

else:
    print("Choix invalide. Veuillez relancer et entrer un numéro de la liste.")