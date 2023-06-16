def nbMotsAvecVoyelle(nomf):
    compteur = 0
    voyelles = ['a', 'e', 'i', 'o', 'u']
    
    with open(nomf, 'r') as fichier:
        for ligne in fichier:
            mot = ligne.strip().lower()
            if mot[0] in voyelles:
                compteur += 1
    
    return compteur

def compterChaqueMot(nomf1, nomf2):
    with open(nomf1, 'r') as fichier1, open(nomf2, 'w') as fichier2:
        mot_precedent = ''
        compteur = 0
        
        for ligne in fichier1:
            mot = ligne.strip().lower()
            
            if mot == mot_precedent:
                compteur += 1
            else:
                if mot_precedent:
                    fichier2.write(f"{mot_precedent} {compteur}\n")
                
                mot_precedent = mot
                compteur = 1
        
        # Écriture du dernier mot et son compteur
        if mot_precedent:
            fichier2.write(f"{mot_precedent} {compteur}\n")
