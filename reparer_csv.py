import csv

with open("etudiants.csv", newline="") as fichier:
    lecteur = csv.DictReader(fichier)
    lignes = list(lecteur)

print(lignes[0])  # {'nom': 'Awa', 'age': '19', 'filiere': 'MPSI'}
