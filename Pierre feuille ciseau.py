import random
scoreJoueur = 0
scoreOrdi = 0
tableau = ["pierre", "feuille", "ciseau"]

def regles(choixJoueur, choixOrdi):
    if choixJoueur == choixOrdi:
        return "égalité"
    elif choixJoueur == "pierre" and choixOrdi == "feuille":
        return "l'ordi à gagné"
    elif choixJoueur == "feuille" and choixOrdi == "ciseau":
        return "l'ordi à gagné"
    elif choixJoueur == "ciseau" and choixOrdi == "pierre":
        return "l'ordi à gagné"
    elif choixJoueur == "feuille" and choixOrdi == "pierre":
        return "tu as gagné!"
    elif choixJoueur == "ciseau" and choixOrdi == "feuille":
        return "tu as gagné!"
    elif choixJoueur == "pierre" and choixOrdi == "ciseau":
        return "tu as gagné!"
    elif choixJoueur != "pierre" or choixJoueur != "feuille" or choixJoueur != "ciseau":
        return "choix invalide, réessaie"

def jeu (choix):
    return "=====================\nTon choix : " + choix + " le choix de l'IA : " + choixIA +"\n" + regles(choix, choixIA)

rejouer = 0
choix = 0

while rejouer != "oui":
    rejouer = 0
    choix = input("\nFait ton choix \npierre, feuille, ciseau\n")
    choixIA = tableau[random.randint(0, 2)]
    if regles(choix, choixIA) == "tu as gagné!":
        scoreJoueur = scoreJoueur+1
    elif regles(choix, choixIA) == "l'ordi à gagné":
        scoreOrdi = scoreOrdi+1
    print(jeu(choix)+ "\n=====================\n Ton score : " + str(scoreJoueur) + "\n scoreOrdi " + str(scoreOrdi)+"\n=====================")
    if scoreJoueur == 3 :
        print("Tu as gagné, félicitation!")
        scoreOrdi=0
        scoreJoueur=0
        break
    elif scoreOrdi == 3:
        print("L'ordi à gagné, dommage...")
        scoreOrdi=0
        scoreJoueur=0
        break
    