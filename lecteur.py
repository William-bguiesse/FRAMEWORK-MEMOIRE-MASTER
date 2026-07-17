# Il faut reflechir à une methode pour créer un lecteur de fichiers markdown ou JSON. 
# pour commencer, le lecteur doit savoir quoi chercher. On pourrait envisager : 
fichier = "sample.md"
# On aurait donc ici stocké le fichier dans une variable qu'on mettra plus dans le lecteur.
# il faudrait ensui utiliser une commande lisant son contenu. Dans la documentation de python,
#  on peut utiliser la fonction open() pour ouvrir le fichier et lire son contenu.

with open(fichier, 'r') as f:
    contenu = f.read()

# avec cette méthode, on peut lire le contenu du fichier et 
# le stocker dans une variable.

# Rien que pour le moment, on peut afficher le contenu du fichier pour vérifier que tout fonctionne correctement.
print(contenu)

# on va commit ceci pour le moment, on essayera d'ameliorer certaine choses plus tard.