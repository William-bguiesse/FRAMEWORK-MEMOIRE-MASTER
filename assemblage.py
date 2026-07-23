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
