class Player:

    def __init__(self):
        self.point = '0'
        self.jeux = 0
        self.set = 0
        self.tieBreakPoint = 0

class Tennis:

    def __init__(self):
        self.tieBreakActivated = False
        self.sex = 'H'
        self.winner = None
        self.looser = None

    def ActivateTieBreak(self):
        self.tieBreakActivated = True

    def WinTheSet(self, playerWinner, playerLooser):
        playerWinner.set = playerWinner.set + 1
        playerWinner.jeux = 0
        playerLooser.jeux = 0

        if (playerWinner.set == 3 and self.sex == 'H') or (playerWinner.set == 2 and self.sex == 'F'):
            self.winner = playerWinner
            self.looser = playerLooser

    def WinTheJeux(self, playerWinner, playerLooser):
        playerWinner.jeux = playerWinner.jeux + 1
        playerWinner.point = '0'
        playerLooser.point = '0'

        if playerWinner.jeux == 6 and playerLooser.jeux == 6:
            self.ActivateTieBreak()

        if playerWinner.jeux >= 6 and (playerWinner.jeux - playerLooser.jeux) >= 2:
            self.WinTheSet(playerWinner, playerLooser)

    def WinThePoint(self, playerWinner, playerLooser):
        if self.tieBreakActivated == True:
            playerWinner.tieBreakPoint = playerWinner.tieBreakPoint + 1

            if playerWinner.tieBreakPoint >= 7 and (playerWinner.tieBreakPoint - playerLooser.tieBreakPoint) >= 2:
                self.WinTheSet(playerWinner, playerLooser)
                playerWinner.tieBreakPoint = 0
                playerLooser.tieBreakPoint = 0
                self.tieBreakActivated = False
        else:
            if playerWinner.point == 'A' or (playerWinner.point == '40' and playerLooser.point in ('0', '15', '30')):
                self.WinTheJeux(playerWinner, playerLooser)
            else:
                if playerWinner.point == '40' and playerLooser.point == 'A':
                    playerLooser.point = '40'
                else:
                    if playerWinner.point == '40' and playerLooser.point == '40':
                        playerWinner.point = 'A'
                    else:
                        if playerWinner.point == '30':
                            playerWinner.point = '40'
                        else:
                            if playerWinner.point == '0':
                                playerWinner.point = '15'
                            else:
                                playerWinner.point = '30'