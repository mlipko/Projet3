#DEBUT
#on admet que random renvoie un chiffre aléatoire entre 0 et 2 inclus
#définir une variable scoreJoueur à 0 et une variable scoreOrdi à 0
#définir un tableau contenant les choix que l'ordi choisira aléatoirement [pierre, feuille, ciseau]
#Definir une fonction "regles" comprenant les règles de supériorité du pierre feuille ciseau ayant pour paramètre le choix du joueur et le choix de l'ordi
    #Si choixJoueur est égal à choixOrdi
        #alors retourner égalité
    #sinon si choixJoueur est égal à pierre et choixOrdi est égal à feuille
        #alors incrementer scoreOrdi de 1
        #retourner "l'ordi a gagné"
    #Sinon si choixJoueur est égal à feuille et choixOrdi est égal à ciseau
        #alors incrementer scoreOrdi de 1
        #retourner "l'ordi a gagné"
    #Sinon si choixJoueur est égal à ciseau et choixOrdi est égal à pierre
        #alors incrementer scoreOrdi de 1
        #retourner "l'ordi a gagné"
    #Sinon si choixJoueur est égal à feuille et choixOrdi est égal à pierre
        #alors incrémenter scoreJoueur de 1
        #retourner "l'ordi a gagné"
    #Sinon si choixJoueur est égal à ciseau et choixOrdi est égal à feuille
        #alors incrémenter scoreJoueur de 1
        #retourner "l'ordi a gagné"
    #Sinon si choixJoueur est égal à pierre et choixOrdi est égal à ciseau
        #alors incrémenter scoreJoueur de 1
        #retourner "l'ordi a gagné"
#Definir une fonction "jeu" permettant de lancer la partie de pierre feuille ciseau avec en paramètre le choix du joueur
    #enregistrer dans la variable choix de l'ordi un élèment aléatoire du tableau grace à un nombre aléatoire entre 0 et 2
    #recuperer dans la fonction des règles le gagnant, le perdant ou l'égalité
    #retourner le choix du joueur, de l'ordi et le gagnant

#initialisation d'une variable "rejouer" permettant de relancer la partie
#Tans que rejouer n'est pas égal à "non":
    #Alors selection d'un élèment aléatoire dans le tableau
    #Demander le choix du joueur et le stocker dans une variable choix
    #afficher le gagnant, le choixJoueur et le choixOrdi, puis le scoreJoueur et scoreOrdi
    #demander au joueur s'il souhaite rejouer
#FIN