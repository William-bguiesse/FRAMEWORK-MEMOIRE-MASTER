import glob 
from lecteur import MarkdownReader 
from convertisseur import Convertisseur

# 1. Récupérer tous les fichiers .md du dossier
tous_les_fichiers = glob.glob("*.md")

# 2. Filtrer pour ignorer README.md (quelle que soit sa casse)
fichiers_a_lire = [f for f in tous_les_fichiers if f.lower() != "readme.md"]

print(f"Fichiers markdown valides trouvés : {fichiers_a_lire}")

# 3. Si on trouve au moins un fichier, on lit le premier
if fichiers_a_lire:
    fichier_cible = fichiers_a_lire[0]
    print(f"\nLecture du fichier : {fichier_cible}\n" + "-"*30)
    
    lecteur = MarkdownReader(fichier_cible)
    texte_brut = lecteur.read_file()
    
    print(texte_brut)
else:
    print("Aucun fichier .md à lire (hors README.md).")