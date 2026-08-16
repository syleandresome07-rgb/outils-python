import os

dossier ='.'        # Le point signifie le dossier courant
compteur_dossier =0
compteur_fichier =0
for element in os.listdir(dossier):
    chemin_complet =os.path.join(dossier, element)
    if os.path.isdir(chemin_complet):
        print(f"[Dossier] {element}")
        compteur_dossier +=1
    else:
        print(f"[Fichier] {element}")
        compteur_fichier +=1

print(f"[Nombre de dossier] {compteur_dossier}\n[Nombre de fichier] {compteur_fichier}")