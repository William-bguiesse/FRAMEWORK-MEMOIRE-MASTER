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


class Jsonconvertisseur:
    def __init__(self, donnees_json):
        self.donnees = donnees_json

    def conversion_en_html(self) -> str:
        if isinstance(self.donnees, dict):
            html = "<div class='json-content'>\n  <ul>\n"
            for cle, valeur in self.donnees.items():
                html += f"    <li><strong>{cle}</strong> : {valeur}</li>\n"
            html += "  </ul>\n</div>"
            return html
# pour tous les couples de clé et valeurs de notre fichier JSON, 
# on crée une liste en HTML grâce aux balises "ul"
        elif isinstance(self.donnees, list):
            html = "<div class='json-content'>\n  <ul>\n"
            for element in self.donnees:
                html += f"    <li>{element}</li>\n"
            html += "  </ul>\n</div>"
            return html

        return f"<div class='json-content'><p>{self.donnees}</p></div>"