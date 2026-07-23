import glob 
from lecteur import MarkdownReader 
from convertisseur import Convertisseur

# 1. Récupérer tous les fichiers markdown avec glob.
fichier_a_lire = glob.glob("*.md")
fichiers_valides = [f for f in fichier_a_lire if f.lower() != "readme.md"]
# on règle un problème en excluant le fichier README.md de la liste des fichiers à lire.



