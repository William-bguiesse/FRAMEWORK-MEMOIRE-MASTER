# On pourrait envisager un plan pour ce fichier du genre :
# 1. une classe qui gere le fichier (son repertoire)
# 2. une classe qui lit le fichier et retourne son contenu
# 3. une classe pour l'enregistrement du contenu dans une variable
    
class FileReader:
    def __init__(self, fichier: str):
        self.fichier = fichier
        self.contenu = None

# ce premier bloc de code met en place une classe FileReader
# qui prend en parametre le nom du fichier a lire et initialise une variable 
# pour stocker le contenu du fichier.

    def read_file(self) -> str:
        with open(self.fichier, 'r', encoding='utf-8') as file:
            self.contenu = file.read()
        return self.contenu
    
# ce second bloc de code utilise une méthode pour lire le contenu du fichier 
# et le stocker dans la variable contenu, puis il retourne son contenu.
    
if __name__ == "__main__":
    lecteur = FileReader("sample.md")
    print(lecteur.read_file())

# enfin, dans ce dernier bloc de code, on crée une instance de la classe FileReader 
# avec le nom du fichier sample.md et on affiche le contenu du fichier 
# qui est lu par la méthode read_file défini auparavant.

# ainsi, dans ce fichier lecteur.py, nous avons mis en place une structure de base 
# pour lire un fichier texte et stocker son contenu dans une variable qui pourra servir
# pour le second fichier python chargé de la conversion.
