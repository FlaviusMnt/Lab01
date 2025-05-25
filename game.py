import random

from domanda import Domanda
from giocatore import Giocatore
class Game:

    @staticmethod
    def leggiFile(inputFile):
        contenitore = []
        with open(inputFile ,"r", encoding="utf-8") as file:
            for riga in file.readlines():
                riga = riga.strip()
                contenitore.append(riga)
        return contenitore

    @staticmethod
    def creaDomande(contenitore):
        domande = []
        i = 0
        while i < len(contenitore):
            if contenitore[i] == "":
                i += 1
                continue

            domanda = contenitore[i]
            difficolta = int(contenitore[i+1])
            corretta = contenitore[i+2]
            sbagliate = contenitore[i+3:i+6]
            opzioni = [corretta] + sbagliate
            domande.append(Domanda(domanda, difficolta, corretta, opzioni))

            i +=7
        return domande

    @staticmethod
    def ordinaDomande(domande):
        domande.sort(key = lambda d: d.difficolta)
        # domande.sort(key=lambda d: d.difficolta, reverse=True)

    @staticmethod
    def livelloMax(domande):
        domande.sort(key = lambda d: d.difficolta, reverse = True)
        return domande[0].difficolta

    @staticmethod
    def proponiDomanda(domande):
        punteggio = 0
        difficoltaProposta = 0
        inGioco = True

        while inGioco:

            domandeLivelloCorrente = []
            for domanda in domande:
                if domanda.difficolta == difficoltaProposta:
                    domandeLivelloCorrente.append(domanda)
            domandaProponente = random.choice(domandeLivelloCorrente)

            print(f"LIVELLO {difficoltaProposta}) {domandaProponente.testo}")
            for (i,elemento) in enumerate(domandaProponente.opzioni_random()):
                print(f"{i+1:>12d} {elemento}")
            rispostaGiocatore = int(input("INSERISCI UNA RISPOSTA: "))
            if rispostaGiocatore == domandaProponente.numeroRispostaCorretta():
                print("Risposta Corretta!")
                punteggio += 1
                difficoltaProposta += 1
                domandeLivelloCorrente.clear()
            else:
                inGioco = False
                print(f"Risposta Errata! La risposta corretta era: {domandaProponente.numeroRispostaCorretta()} \n")
                print(f"HAI TOTALIZZATO {punteggio} PUNTI")
                nomeGiocatore = input("INSERISCI IL TUO NOME: ")
                giocatore = Giocatore(nomeGiocatore,punteggio)
                with open("punti.txt","a", encoding="utf-8") as file:
                    file.write("\n" + giocatore.nome + " " + str(giocatore.punti))

    @staticmethod
    def ordinaFilePunti(infile):
        with open(infile,"r",encoding="utf-8") as file:
            listaPunti = []
            contenitore = file.readlines()

            for riga in contenitore:
                riga = riga.strip()
                nome = riga.split()[0]
                punti = int(riga.split()[1])
                listaPunti.append((nome, punti))

            listaPunti.sort(key = lambda x: x[1], reverse = True)
            with open(infile,"w",encoding="utf-8") as ofile:
                for linea in listaPunti:
                    ofile.write(f"{linea[0]} {linea[1]}\n")


