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

def age_valide(valeur_texte):
    try:
        return int(valeur_texte)
    except ValueError:
        return None  # on ne peut pas convertir -> valeur invalide

for ligne in lignes:
    age_converti = age_valide(ligne["age"])
    if age_converti is None and ligne["age"] != "":
        print(f"Âge invalide pour {ligne['nom']} : '{ligne['age']}'")
