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

def divide(x, y):
    return x / y

def modulo (x, y):
    return x % y

def salaireNet(Brut, coefficient):
    return Brut * coefficient/100

def salaireParSeconde(salaireHoraire, HeureParJourOuvré, NbJourOuvréParAn):
    return salaireHoraire*HeureParJourOuvré*NbJourOuvréParAn



#FIN