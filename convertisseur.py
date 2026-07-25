import markdown

class Convertisseur:
    def __init__(self, texte_markdown):
        self.texte_markdown = texte_markdown

# on defini la classe Convertisseur avec un constructeur qui prend en paramètre 
# le texte en markdown et le stocke dans l'attribut self.texte_markdown. 
# pour l'instant, il ne se passe rien.

    def conversion_en_html(self):
        conversion_html = markdown.markdown(self.texte_markdown)
        return conversion_html

# ici, la méthode convertion_en_html utilise la fonction markdown.markdown 
# pour convertir le texte en markdown stocké dans self.texte_markdown en HTML. 
# Elle retourne ensuite le code HTML résultant.


    
