# Mémoire de Master 1 : création d'un framework python de convertion de fichier.

L'objectif de ce projet de mémoire est de mettre un place progressivement, tout au long des commits (**étapes**), un plan de construction d'un framework python capable de générer une sortie HTML à partir de code markdown ou de fichier JSON.

## Installation :

Ce projet utilise le gestionnaire de paquets moderne `uv` pour la mise en place de l'environnement virtuel de travail et s'appuie sur un environnement moderne et léger :
* **Gestionnaire de paquets :** `uv` (remplaçant rapide et moderne de pip)
* **Moteur de template :** `Jinja2` (génération des structures HTML)
* **Parser Markdown :** `markdown` (conversion du texte brut en HTML)
* **Configuration :** `PyYAML` (lecture des métadonnées)

## Architecture du projet :

L'architecture du projet devra s'articuler autour de differents fichier py qui se connecteront entre eux pour tirer le potentiel du framework. On distinguera donc : 
* un fichier de gestion du framework (qui fonctionnera autour de l'idée d'une CLI)
* un fichier de lecture, ayant pour rôle de tirer d'un texte markdown ou json les données sous forme brut, les stocker et les utiliser dans le fichier suivant
* un fichier de conversion, qui devra prendre les données HTML du précédent fichier puis y appliquer les code HTML necessaire
* un fichier servant de sortie au resultat attendu.

```bash
# 1. Cloner le projet
git clone <lien-de-ton-repo>
cd framework-master

# 2. Installer les dépendances et créer l'environnement virtuel
uv sync