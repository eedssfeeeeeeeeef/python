class Personne:
    def __init__(self, nom, prenom, numero, nom_rue, telephone, code_postal, ville):
        self.nom = nom
        self.prenom = prenom
        self.numero = numero
        self.nom_rue = nom_rue
        self.telephone = telephone
        self.code_postal = code_postal
        self.ville = ville


def saisie_tab():
    annuaire = []
    while True:
        nom = input("Nom (ou 'q' pour quitter la saisie) : ")
        if nom.lower() == 'q':
            break

        prenom = input("Prénom : ")
        numero = input("Numéro dans la rue : ")
        nom_rue = input("Nom de la rue : ")
        telephone = input("Numéro de téléphone : ")
        code_postal = input("Code postal : ")
        ville = input("Ville : ")

        personne = Personne(nom, prenom, numero, nom_rue, telephone, code_postal, ville)
        annuaire.append(personne)
        print("La personne a été ajoutée à l'annuaire.")

    return annuaire


def critere_recherche():
    print("Choisissez le critère de recherche :")
    print("1. Nom")
    print("2. Prénom")
    print("3. Nom de la rue")
    print("4. Numéro de téléphone")
    print("5. Code postal")
    print("6. Ville")

    choix = input("Entrez le numéro correspondant au critère : ")
    return choix


def recherche(annuaire, critere):
    valeur_recherche = input("Entrez la valeur à rechercher : ")

    personnes_trouvees = []
    for personne in annuaire:
        if critere == "1" and personne.nom.lower() == valeur_recherche.lower():
            personnes_trouvees.append(personne)
        elif critere == "2" and personne.prenom.lower() == valeur_recherche.lower():
            personnes_trouvees.append(personne)
        elif critere == "3" and personne.nom_rue.lower() == valeur_recherche.lower():
            personnes_trouvees.append(personne)
        elif critere == "4" and personne.telephone == valeur_recherche:
            personnes_trouvees.append(personne)
        elif critere == "5" and personne.code_postal == valeur_recherche:
            personnes_trouvees.append(personne)
        elif critere == "6" and personne.ville.lower() == valeur_recherche.lower():
            personnes_trouvees.append(personne)

    return personnes_trouvees


def affiche_tab(annuaire, personnes):
    if personnes:
        print("Personnes trouvées :")
        for personne in personnes:
            print("Nom :", personne.nom)
            print("Prénom :", personne.prenom)
            print("Numéro dans la rue :", personne.numero)
            print("Nom de la rue :", personne.nom_rue)
            print("Numéro de téléphone :", personne.telephone)
            print("Code postal :", personne.code_postal)
            print("Ville :", personne.ville)
    else:
        print("Aucune personne trouvée avec les critères de recherche spécifiés.")


# Programme principal
annuaire = saisie_tab()

while True:
    print("\n----- Menu principal -----")
    print("1. Rechercher une personne")
    print("2. Quitter")
    choix_menu = input("Choisissez une option : ")

    if choix_menu == "1":
        critere = critere_recherche()
        personnes_trouvees = recherche(annuaire, critere)
        affiche_tab(annuaire, personnes_trouvees)
    elif choix_menu == "2":
        break
