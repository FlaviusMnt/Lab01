import random
from giocatore import Giocatore
from domanda import Domanda
from game import Game


def main():
    file = Game.leggiFile("domande.txt")
    domande = Game.creaDomande(file)
    Game.ordinaDomande(domande)
    for domanda in domande:
        print(domanda)
    zeb = Game.livelloMax(domande)
    print("*******")
    print(zeb)
    print("*******")

    Game.proponiDomanda(domande)
    Game.ordinaFilePunti("punti.txt")


main()

if __name__ == "__main__":
    pass




