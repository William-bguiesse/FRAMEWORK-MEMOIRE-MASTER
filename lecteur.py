import glob 
import json

class MarkdownReader:
    def __init__(self, fichier: str):
        self.fichier = fichier
        self.contenu = None

    def read_file(self) -> str:
        with open(self.fichier, 'r', encoding='utf-8') as file:
            self.contenu = file.read()
        return self.contenu

class JSONReader:
    def __init__(self, fichier: str):
        self.fichier = fichier
        self.contenu = None

    def read_file(self) -> dict:
        with open(self.fichier, 'r', encoding='utf-8') as file:
            self.contenu = json.load(file)
        return self.contenu

liste_fichiers = glob.glob("*.md") 
if len(liste_fichiers) == 0:
    print("Aucun fichier .md trouvé dans le répertoire courant.")
else:
    print(f"Fichiers .md trouvés : {liste_fichiers}")
    lecteur = MarkdownReader(liste_fichiers[0])
    print(lecteur.read_file())

liste_fichiers_json = glob.glob("*.json")
if len(liste_fichiers_json) == 0:
    print("Aucun fichier .json trouvé dans le répertoire courant.")
else:
    print(f"Fichiers .json trouvés : {liste_fichiers_json}")
    lecteur_json = JSONReader(liste_fichiers_json[0])
    print(lecteur_json.read_file())
