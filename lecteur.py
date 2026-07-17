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
# On récupère une liste de tous les fichiers .md dans le répertoire courant. Mais il faut 
# se demander s'il y en a ou pas... donc on va vérifier si la liste est vide ou non.
if len(liste_fichiers) == 0:
    print("Aucun fichier .md trouvé dans le répertoire courant.")
else:
    print(f"Fichiers .md trouvés : {liste_fichiers}")
    lecteur = FileReader(liste_fichiers[0])
    print(lecteur.read_file())

# ainsi, si la longueur de la liste est de zero (nulle), on affiche un message d'erreur. 
# Sinon, on crée une instance de FileReader avec le premier fichier de la liste qui sera lu 
# et son contenu affiché. Cela permet de gérer le cas où 
# il n'y a pas de fichiers .md dans le répertoire courant.
