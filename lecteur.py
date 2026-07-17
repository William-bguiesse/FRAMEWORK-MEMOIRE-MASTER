# On pourrait envisager un plan pour ce fichier du genre :
# 1. une classe qui gere le fichier (son repertoire)
# 2. une classe qui lit le fichier et retourne son contenu
# 3. une classe pour l'enregistrement du contenu dans une variable
import glob 

class FileReader:
    def __init__(self, fichier: str):
        self.fichier = fichier
        self.contenu = None

    def read_file(self) -> str:
        with open(self.fichier, 'r', encoding='utf-8') as file:
            self.contenu = file.read()
        return self.contenu
    
liste_fichiers = glob.glob("*.md") 
# utilisation de glob pour chercher tous les fichiers qui se termine par .md 
# et les stocker dans la variable liste_fichiers
