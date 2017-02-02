import unittest
from Tennis import Player
from Tennis import Tennis

class TennisTest(unittest.TestCase):
    tennis = Tennis()

    def test_ShouldReturn_0_0(self):
        player1 = Player();
        player2 = Player();

        self.assertEqual(player1.point, '0')
        self.assertEqual(player2.point, '0')

    def test_ShouldReturn_15_0(self):
        player1 = Player();
        player2 = Player();

        self.tennis.WinThePoint(player1, player2);

        self.assertEqual(player1.point, '15')
        self.assertEqual(player2.point, '0')

    def test_ShouldReturn_30_0(self):
        player1 = Player()
        player2 = Player()

        for i in range(0,2):
            self.tennis.WinThePoint(player1, player2)

        self.assertEqual(player1.point, '30')
        self.assertEqual(player2.point, '0')

    def test_ShouldReturn_40_0(self):
        player1 = Player()
        player2 = Player()

        for i in range(0,3):
            self.tennis.WinThePoint(player1, player2)

        self.assertEqual(player1.point, '40')
        self.assertEqual(player2.point, '0')

    def test_ShouldReturn_A_40(self):
        player1 = Player()
        player2 = Player()

        for i in range(0,3):
            self.tennis.WinThePoint(player1, player2)

        for i in range(0,3):
            self.tennis.WinThePoint(player2, player1)

        self.tennis.WinThePoint(player1, player2)

        self.assertEqual(player1.point, 'A')
        self.assertEqual(player2.point, '40')

    def test_ShouldReturn_40_40_After_A_40(self):
        player1 = Player()
        player2 = Player()

        for i in range(0,3):
            self.tennis.WinThePoint(player1, player2)

        for i in range(0,3):
            self.tennis.WinThePoint(player2, player1)

        self.tennis.WinThePoint(player1, player2)
        self.tennis.WinThePoint(player2, player1)

        self.assertEqual(player1.point, '40')
        self.assertEqual(player2.point, '40')

    def test_ShouldWin_Jeux_after_40_0(self):
        player1 = Player()
        player2 = Player()

        for i in range(0,4):
            self.tennis.WinThePoint(player1, player2)

        self.assertEqual(player1.jeux, 1)
        self.assertEqual(player2.jeux, 0)
        self.assertEqual(player1.point, '0')
        self.assertEqual(player2.point, '0')

    def test_ShouldWin_Jeux_after_A_40(self):
        player1 = Player()
        player2 = Player()

        for i in range(0,3):
            self.tennis.WinThePoint(player1, player2)

        for i in range(0,3):
            self.tennis.WinThePoint(player2, player1)

        for i in range(0,2):
            self.tennis.WinThePoint(player1, player2)

        self.assertEqual(player1.jeux, 1)
        self.assertEqual(player2.jeux, 0)
        self.assertEqual(player1.point, '0')
        self.assertEqual(player2.point, '0')

    def test_ShouldWin_Set_After_6_0(self):
        player1 = Player()
        player2 = Player()

        for i in range (0, 6):
            self.tennis.WinTheJeux(player1, player2)

        self.assertEqual(player1.set, 1)
        self.assertEqual(player2.set, 0)
        self.assertEqual(player1.jeux, 0)
        self.assertEqual(player2.jeux, 0)

    def test_ShouldNotWin_Set_IfAvance_Inferior_2(self):
        player1 = Player()
        player2 = Player()

        for i in range (0, 5):
            self.tennis.WinTheJeux(player1, player2)

        for i in range (0, 5):
            self.tennis.WinTheJeux(player2, player1)

        self.tennis.WinTheJeux(player1, player2)

        self.assertEqual(player1.set, 0)
        self.assertEqual(player2.set, 0)
        self.assertEqual(player1.jeux, 6)
        self.assertEqual(player2.jeux, 5)

    def test_ShouldWin_Set_After_6_0(self):
        player1 = Player()
        player2 = Player()

        for i in range(0, 5):
            self.tennis.WinTheJeux(player1, player2)

        for i in range(0, 5):
            self.tennis.WinTheJeux(player2, player1)

        for i in range(0, 2):
            self.tennis.WinTheJeux(player1, player2)

        self.assertEqual(player1.set, 1)
        self.assertEqual(player2.set, 0)
        self.assertEqual(player1.jeux, 0)
        self.assertEqual(player2.jeux, 0)

    def test_ShouldTieBreak_Activated(self):
        player1 = Player()
        player2 = Player()
        local_Tennis = Tennis()

        for i in range(0, 5):
            local_Tennis.WinTheJeux(player1, player2)

        for i in range(0, 5):
            local_Tennis.WinTheJeux(player2, player1)

        local_Tennis.WinTheJeux(player1, player2)
        local_Tennis.WinTheJeux(player2, player1)

        self.assertEqual(local_Tennis.tieBreakActivated, True)
        self.assertEqual(player1.set, 0)
        self.assertEqual(player2.set, 0)
        self.assertEqual(player1.jeux, 6)
        self.assertEqual(player2.jeux, 6)

    def test_ShouldSetTieBreakPoint_And_NotSetPoint_After_TieBreak_Activated(self):
        player1 = Player()
        player2 = Player()
        local_Tennis = Tennis()

        local_Tennis.ActivateTieBreak()
        local_Tennis.WinThePoint(player1, player2);

        self.assertEqual(player1.tieBreakPoint, 1)
        self.assertEqual(player2.tieBreakPoint, 0)
        self.assertEqual(player1.point, '0')
        self.assertEqual(player2.point, '0')

    def test_ShouldWin_Set_After_7_0_TieBreakPoint(self):
        player1 = Player()
        player2 = Player()
        local_Tennis = Tennis()

        local_Tennis.ActivateTieBreak()

        for i in range(0,7):
            local_Tennis.WinThePoint(player1, player2);

        self.assertEqual(player1.set, 1)
        self.assertEqual(player2.set, 0)
        self.assertEqual(player1.jeux, 0)
        self.assertEqual(player2.jeux, 0)
        self.assertEqual(local_Tennis.tieBreakActivated, False)
        self.assertEqual(player1.tieBreakPoint, 0)
        self.assertEqual(player2.tieBreakPoint, 0)

    def test_ShouldNotWin_Set_IfAvance_Inferior_2(self):
        player1 = Player()
        player2 = Player()
        local_Tennis = Tennis()

        local_Tennis.ActivateTieBreak()

        for i in range(0,6):
            local_Tennis.WinThePoint(player1, player2);

        for i in range(0,6):
            local_Tennis.WinThePoint(player2, player1);

        local_Tennis.WinThePoint(player1, player2);

        self.assertEqual(player1.set, 0)
        self.assertEqual(player2.set, 0)
        self.assertEqual(local_Tennis.tieBreakActivated, True)
        self.assertEqual(player1.tieBreakPoint, 7)
        self.assertEqual(player2.tieBreakPoint, 6)

    def test_ShouldWin_Set_IfAvance_Superior_2(self):
        player1 = Player()
        player2 = Player()
        local_Tennis = Tennis()

        local_Tennis.ActivateTieBreak()

        for i in range(0,6):
            local_Tennis.WinThePoint(player1, player2);

        for i in range(0,6):
            local_Tennis.WinThePoint(player2, player1);

        local_Tennis.WinThePoint(player1, player2);
        local_Tennis.WinThePoint(player1, player2);

        self.assertEqual(player1.set, 1)
        self.assertEqual(player2.set, 0)
        self.assertEqual(local_Tennis.tieBreakActivated, False)
        self.assertEqual(player1.tieBreakPoint, 0)
        self.assertEqual(player2.tieBreakPoint, 0)

    def test_Win_H(self):
        player1 = Player()
        player2 = Player()
        local_Tennis = Tennis()

        for i in range(0,3):
            local_Tennis.WinTheSet(player1, player2)

        self.assertEqual(local_Tennis.winner, player1)
        self.assertEqual(local_Tennis.looser, player2)

    def test_Win_F(self):
        player1 = Player()
        player2 = Player()
        local_Tennis = Tennis()
        local_Tennis.sex = 'F'

        for i in range(0,2):
            local_Tennis.WinTheSet(player1, player2)

        self.assertEqual(local_Tennis.winner, player1)
        self.assertEqual(local_Tennis.looser, player2)

if __name__ == '__main__':
    unittest.main()
