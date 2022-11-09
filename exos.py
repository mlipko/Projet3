#DEBUT

#EXO 1

r=12000
s=1250
e=10
rh=230
assertion1 = ( (365*3)/(24-(16-8)))*(rh) > r #true
print(assertion1)
assertion2 = e*s<r #false
print(assertion2)
assertionFinale = assertion1 == assertion2
print(assertionFinale) #false


#EXO 2

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y
     
#Définir une fonction qui divise x par y et retourne le resultat
def divide(x, y):
    #Si y est egale à 0
    if y == 0:
        #Alors écrire un message d'erreur
        print("ERREUR : Cannot divide by 0")
        #retourner vide
        return
    #Sinon
    else:
        #Alors retourner x / y
        return x / y

def modulo (x, y):
    return x % y

def salaireNet(Brut, coefficient):
    return Brut * coefficient/100
def salaireParSeconde(salaireHoraire, HeureParJourOuvré, NbJourOuvréParAn):
    return salaireHoraire*HeureParJourOuvré*NbJourOuvréParAn

#Definir une fonction withdrawFees qui retire un pourcentage à un totale en fonction d'un total et d'un pourcentage
def withdrawFees(total, percent):
    #Definir Fees en fonction d'un total et d'un pourcentage
    fees = total * (percent / 100)
    #soustraire fees au total
    result = total - fees
    #retourner la valeur obtenue
    return result

#Définir une fonction qui retourne le salaire net en fonction du salaire brut (float) et du secteur d'activité (isPublic > booleen)
def calculBrutEnNet(salaireBrut, isPublic):
    if isPublic:
        #Alors je soustrais 15% de mon salaire Brut a mon salaire brut et je l'assigne a la variable salaireNet
        # salaireNet = salaireBrut - (salaireBrut /(15/100))
        salaireNet = withdrawFees (salaireBrut, 15)
    else:
        #Alors je soustrais 23% de mon salaire Brut a mon salaire brut et je l'assigne a la variable salaireNet
        salaireNet = withdrawFees (salaireBrut, 23)
    return salaireNet


#EXO 3
#Definir une fonction de jeu ayant un caractère de paramètrable
def jeu(paramètre):
    #initialiser une variable string
    string = input("devine la lettre :")
    #enregistrer le caractère parametrable dans une variable
    caractere = paramètre
    #boucle tant que le caractère n'est pas trouvé input non egal à string
    while caractere != string:
        #assigner à une variable un caractère aleatoire de type string à l'aide de la fonction input
        string = input("devine la lettre :")
    #retourner la variable string
    return string

#envoyer le message indiquant le caractère trouvé en utilisant la fonction du jeu
print("caractère trouvé : " +jeu ("h"))


prenom ="mathias"

nom = "lipko"

identite = nom+prenom #retourne "mathiaslipko"

identite = nom + ' ' + prenom #retourne "mathias lipko"

integerValue = 342 #retourne 342
stringIntegerValue = str(342) #retourne "342"

#Exercice 1
#Faire une fonction qui concatene 2 chaines de caractère, les séparant par une virgule
def concatene(str1, str2):
    if str1=="":
        return str2
    return str1 + ", " + str2

#Exercide 2
#Faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractère avec l'ensemble de l'occurance d'un chiffre e.g.:
#Pour tableau = [0, 1, 1, 1, 0, 1, 1, 0, 1]
#La fonction(tableau, 0) doit renvoyer "0, 4, 7" n'hésitez pas à utiliser la première fonction
def showAllIndexes(tbl, nb):
    string = ""
    for i in range(len(tbl)):
        if tbl[i]==nb:
            string=concatene(string, str(i))
    return string

#exercice 3
#Renvoyer/afficher un message
def show(*args):
    print(*args)

show(concatene("Hello", "World"))
show(showAllIndexes([0, 1, 1, 1, 0, 1, 1, 0, 1], 0))

#FIN 
