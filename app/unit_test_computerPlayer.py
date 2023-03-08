
import unittest
import random
from main import ComputerPlayer, Game


class TestComputerPlayer(unittest.TestCase):

    def setUp(self):
        self.computer_player = ComputerPlayer()

    def test_computer_player_roll_dice(self):
        player = ComputerPlayer()
        rolls = []
        for i in range(10000):
            rolls.append(player.roll_dice())
        assert all(roll >= 1 and roll <= 6 for roll in rolls)

    def test_game_human_turn(self):
        game = Game("Solomon")
        game.human_turn()
        assert game.human_player.total_score >= 0
        assert game.human_player.total_score <= 6
        assert game.human_player.turn_score == game.human_player.roll_score
        assert game.state == "human_continue_or_hold"

    def test_game_computer_turn(self):
        game = Game("Solomon")
        game.state = "computer_turn"
        game.computer_turn()
        assert game.computer_player.total_score >= 0
        assert game.computer_player.total_score <= 6
        assert game.computer_player.turn_score == game.computer_player.roll_score

    def test_roll_dice(self):
        for i in range(100):
            roll = self.computer_player.roll_dice()
            self.assertTrue(1 <= roll <= 6)

    def test_hold_score(self):
        self.computer_player.roll_score = 2
        self.computer_player.turn_score = 10
        self.computer_player.total_score = 20
        self.computer_player.hold_score()
        self.assertEqual(self.computer_player.turn_score, 0)
        self.assertEqual(self.computer_player.roll_score, 0)

    def test_computerplayer_name(self):
        c = ComputerPlayer()
        self.assertEqual(c.name, "Computer")

    def test_computerplayer_play_turn_rolls_one(self):
        c = ComputerPlayer()
        self.assertTrue(c.play_turn("Computer"))

    def test_computerplayer_play_turn_rolls_not_one(self):
        c = ComputerPlayer()
        random.seed(1) # force the dice roll to be 3
        self.assertTrue(c.play_turn("Computer"))

    def test_computerplayer_hold_score(self):
        c = ComputerPlayer()
        c.roll_score = 3
        c.turn_score = 5
        c.hold_score()
        self.assertEqual(c.roll_score, 0)
        self.assertEqual(c.turn_score, 0)

    def test_computerplayer_is_winner_false(self):
        c = ComputerPlayer()
        c.total_score = 49
        self.assertFalse(c.is_winner())

    def test_computerplayer_is_winner_false2(self):
        c = ComputerPlayer()
        c.total_score = 0
        self.assertFalse(c.is_winner())

    def test_computerplayer_is_winner_true(self):
        c = ComputerPlayer()
        c.total_score = 50
        self.assertTrue(c.is_winner())

    def test_computerplayer_is_winner_true_2(self):
        c = ComputerPlayer()
        c.total_score = 55
        self.assertTrue(c.is_winner())

    def test_computerplayer_is_winner_true_3(self):
        c = ComputerPlayer()
        c.total_score = 200
        self.assertTrue(c.is_winner()) 



if __name__ == "__main__":
    unittest.main()
