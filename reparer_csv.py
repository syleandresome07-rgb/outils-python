import csv

with open("etudiants.csv", newline="") as fichier:
    lecteur = csv.DictReader(fichier)
    lignes = list(lecteur)

print(lignes[0])  # {'nom': 'Awa', 'age': '19', 'filiere': 'MPSI'}

for ligne in lignes:
    if ligne["age"] == "":
        print(f"Ligne incomplète : {ligne['nom']} n'a pas d'âge renseigné")

vues = set()
for ligne in lignes:
    identifiant = (ligne["nom"], ligne["age"], ligne["filiere"])
    if identifiant in vues:
        print(f"Doublon détecté : {ligne['nom']}")
    vues.add(identifiant)
