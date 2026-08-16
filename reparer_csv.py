import csv

with open("etudiants.csv", newline="") as fichier:
    lecteur = csv.DictReader(fichier)
    lignes = list(lecteur)

print(lignes[0])  # {'nom': 'Awa', 'age': '19', 'filiere': 'MPSI'}

for ligne in lignes:
    if ligne["age"] == "":
        print(f"Ligne incomplète : {ligne['nom']} n'a pas d'âge renseigné")
