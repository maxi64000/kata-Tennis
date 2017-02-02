from Tennis import Player
from Tennis import Tennis
import time
from random import randint
import os

tennis = Tennis()
player1 = Player()
player2 = Player()

def ShowScore():
    print("joueur 1 :     set    jeux    point")
    print("               " + str(player1.set) + "      " + str(player1.jeux) + "       " + player1.point + "")

    print("joueur 2 :     set    jeux    point")
    print("               " + str(player2.set) + "      " + str(player2.jeux) + "       " + player2.point + "")
    print("-----------------------------------")

z = 0
j = 1

while tennis.winner == None:
    os.system('cls')  # For Windows

    if (tennis.sex == 'H'):
        print("-----------------------------------")
        print("Tennis Masculin")
        print("-----------------------------------")
    else:
        print("-----------------------------------")
        print("Tennis Feminin")
        print("-----------------------------------")

    i = randint(1,2)

    if (i == z):
        j = j + 1
    else:
        j = 1

    if i == 1:
        tennis.WinThePoint(player1, player2)
        print("Joueur 1 gagne le point | X" + str(j))
        print("-----------------------------------")
    else:
        tennis.WinThePoint(player2, player1)
        print("Joueur 2 gagne le point | X" + str(j))
        print("-----------------------------------")

    z = i

    ShowScore()

    if (tennis.tieBreakActivated == True):
        print("Tie-Break")
        print("-----------------------------------")
        print("joueur 1 : " + str(player1.tieBreakPoint))

        print("joueur 2 : " + str(player2.tieBreakPoint))
        print("-----------------------------------")

    if (tennis.winner != None and tennis.looser != None):
        if (tennis.winner == player1):
            print("Gagnant :    Joueur 1")
            print("Perdant :    Joueur 2")
            print("-----------------------------------")
        else:
            print("Gagnant :    Joueur 2")
            print("Perdant :    Joueur 1")
            print("-----------------------------------")

    time.sleep(0.25)