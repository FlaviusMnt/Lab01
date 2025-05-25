import random

class Domanda(object):
    def __init__(self, testo = "", difficolta = None , corretta="", opzioni =[]):
        self.testo = testo
        self.difficolta = difficolta
        self.corretta = corretta
        self.opzioni = opzioni


    def opzioni_random(self):
        random.shuffle(self.opzioni)
        return self.opzioni

    def __str__(self):
        return f"DOMANDA:{self.testo:^80s} -- DIFFICOLTA:{self.difficolta:^10d} --CORRETTA:{self.corretta:>30s}"

    def numeroRispostaCorretta(self):
        indiceCorretto = self.opzioni.index(self.corretta) +1
        return indiceCorretto




if __name__ == "__main__":
    listaDomande = []
    domanda1 = Domanda("Capitale dell'Italia?",0,"Roma",["Roma","Milano","Berlino","Parigi"])
    domanda2 = Domanda('Elemento chimico con simbolo "H"?',1,"Idrogeno",["Idrogeno","Ossigeno","Carbonio","Ferro"])
    listaDomande.append(domanda1)
    listaDomande.append(domanda2)
    for d in listaDomande:
        print(d)


    print(domanda1.opzioni)
    domanda1.opzioni_random()
    print(domanda1.opzioni)
    print(domanda1.numeroRispostaCorretta())