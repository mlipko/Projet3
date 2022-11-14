#DEBUT
#on admet que random renvoie un chiffre aléatoire entre 0 et 2 inclus
import random
#définir une variable scoreJoueur à 0 et une variable scoreOrdi à 0

#définir un tableau contenant les choix que l'ordi choisira aléatoirement [pierre, feuille, ciseau]
tableau = ["pierre", "feuille", "ciseau"]
#Definir une fonction "regles" comprenant les règles de supériorité du pierre feuille ciseau ayant pour paramètre le choix du joueur et le choix de l'ordi
def regles(choixJoueur, choixOrdi):
    scoreJoueur = 0
    scoreOrdi = 0
    #Si choixJoueur est égal à choixOrdi
    if choixJoueur == choixOrdi:
        #alors retourner égalité
        return "égalité"
    #Sinon si choixJoueur est égal à pierre et choixOrdi est égal à feuille
    elif choixJoueur == "pierre" and choixOrdi == "feuille":
        #alors incrementer scoreOrdi de 1
        #retourner "l'ordi a gagné"
        scoreOrdi = scoreOrdi + 1
        return "l'ordi à gagné"
    #Sinon si choixJoueur est égal à feuille et choixOrdi est égal à ciseau
    elif choixJoueur == "feuille" and choixOrdi == "ciseau":
        #alors incrementer scoreOrdi de 1
        #retourner "l'ordi a gagné"
        scoreOrdi = scoreOrdi + 1
        return "l'ordi à gagné"
    #Sinon si choixJoueur est égal à ciseau et choixOrdi est égal à pierre
    elif choixJoueur == "ciseau" and choixOrdi == "pierre":
        #alors incrementer scoreOrdi de 1
        #retourner "l'ordi a gagné"
        scoreOrdi = scoreOrdi + 1
        return "l'ordi à gagné"
    #Sinon si choixJoueur est égal à feuille et choixOrdi est égal à pierre
    elif choixJoueur == "feuille" and choixOrdi == "pierre":
        #alors incrémenter scoreJoueur de 1
        #retourner "l'ordi a gagné"
        scoreJoueur = scoreJoueur + 1
        return "tu as gagné!"
    #Sinon si choixJoueur est égal à ciseau et choixOrdi est égal à feuille
    elif choixJoueur == "ciseau" and choixOrdi == "feuille":
        #alors incrémenter scoreJoueur de 1
        #retourner "l'ordi a gagné"
        scoreJoueur = scoreJoueur + 1
        return "tu as gagné!"
    #Sinon si choixJoueur est égal à pierre et choixOrdi est égal à ciseau
    elif choixJoueur == "pierre" and choixOrdi == "ciseau":
        #alors incrémenter scoreJoueur de 1
        #retourner "l'ordi a gagné"
        scoreJoueur = scoreJoueur + 1
        return "tu as gagné!"
#Definir une fonction "jeu" permettant de lancer la partie de pierre feuille ciseau avec en paramètre le choix du joueur
def jeu (choix):


    #recuperer dans la fonction des règles le gagnant, le perdant ou l'égalité

    #retourner le choix du joueur, de l'ordi et le gagnant
    return "====================\nTon choix : " + choix + " le choix de l'IA : " + choixIA +"\n" + regles(choix, choixIA)
 
#initialisation d'une variable "rejouer" permettant de relancer la partie
rejouer = 0

#Tans que rejouer n'est pas égal à "non":
while rejouer != "non":

    #Alors selection d'un élèment aléatoire dans le tableau
    #Demander le choix du joueur et le stocker dans une variable choix
    choix = input("====================\nFait ton choix \npierre, feuille, ciseau\n")
    choixIA = tableau[random.randint(0, 2)]
    regles(choix, choixIA)
    #afficher le gagnant, le choixJoueur et le choixOrdi, puis le scoreJoueur et scoreOrdi
    print(jeu(choix)+ "\n=====================\n Ton score : " + scoreJoueur + "\n scoreOrdi " + scoreOrdi+"\n ====================")
    #demander au joueur s'il souhaite rejouer
#FIN