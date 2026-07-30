from pathlib import Path
from lecteur import MarkdownReader, JSONReader
from convertisseur import Convertisseur, JsonConvertisseur


class Moteur:
    """Automatisateur de conversion de fichiers (.md et .json) vers HTML."""

    def __init__(self):
        # Dictionnaire de correspondance
        self.correspond = {
            ".md": (MarkdownReader, Convertisseur),
            ".json": (JSONReader, JsonConvertisseur),
        }

    def conversion_fichier(self, chemin_fichier: Path) -> str:
        type_file = chemin_fichier.suffix.lower()
        if type_file not in self.correspond:
            raise ValueError(f"Format non supporté : {type_file}")

        # Récupération dynamique et conversion
        LecteurClass, ConvertisseurClass = self.correspond[type_file]
        lecteur = LecteurClass(str(chemin_fichier))
        donnees = lecteur.read_file()
        convertisseur = ConvertisseurClass(donnees)
        return convertisseur.conversion_en_html()

    def build(self, dossier_source: str = ".", dossier_sortie: str = "public"):
        dist = Path(dossier_sortie)
        dist.mkdir(exist_ok=True)
        count = 0

        for f in Path(dossier_source).glob("*"):
            if (
                f.is_file()
                and f.name.lower() != "readme.md"
                and f.suffix.lower() in self.correspond
            ):
                print(f"Conversion de : {f.name}")
                html_body = self.conversion_fichier(f)
                page = f"<!DOCTYPE html>\n<html lang='fr'>\n<head><meta charset='UTF-8'><title>{f.stem}</title></head>\n<body>\n{html_body}\n</body>\n</html>"
                (dist / f"{f.stem}.html").write_text(page, encoding="utf-8")
                count += 1