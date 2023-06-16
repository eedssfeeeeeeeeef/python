import random

class Personne:
    def __init__(self, nom):
        self.nom = nom
        self.annee = None
        self.temps = None

def Saisie():
    t = []  # Tableau pour stocker les personnes
    while True:
        nom = input("Entrez le nom de la personne (ou 'q' pour quitter) : ")
        if nom == 'q':
            break
        personne = Personne(nom)  # Création d'une instance de la classe Personne
        t.append(personne)  # Ajout de la personne au tableau
    return t

def calculAnnee(t, annee_min, annee_max):
    for personne in t:
        print(f"Personne: {personne.nom}")
        print(f"Choisissez une période pour le voyage dans le temps (entre {annee_min} et {annee_max})")
        annee_debut = int(input("Année de début : "))
        annee_fin = int(input("Année de fin : "))
        personne.annee = random.randint(annee_debut, annee_fin)

def calculTemps(t):
    periode_saut = 10
    annee_retour = 2017
    for personne in t:
        temps = 0
        while personne.annee != annee_retour:
            if personne.annee < annee_retour:
                personne.annee += periode_saut
            else:
                personne.annee -= periode_saut
            temps += 10
        personne.temps = temps

# Exemple d'utilisation
t = Saisie()
calculAnnee(t, 2007, 2037)
calculTemps(t)

# Affichage des résultats
print("Résultats :")
for personne in t:
    print(f"Nom: {personne.nom} | Année: {personne.annee} | Temps: {personne.temps} secondes")
