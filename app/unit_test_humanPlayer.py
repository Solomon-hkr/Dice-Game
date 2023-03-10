
import unittest
from unittest.mock import patch
from main import HumanPlayer

class TestHumanPlayer(unittest.TestCase):
    def setUp(self):
        self.player = HumanPlayer("Solomon")

    def test_name(self):
        self.assertEqual(self.player.name, "Solomon")

    @patch('builtins.input', side_effect=[''])
    def test_play_turn_roll(self, mock_input):
        result = self.player.play_turn("Human")
        self.assertTrue(isinstance(result, bool))

    @patch('builtins.input', side_effect=['h'])
    def test_play_turn_hold(self, mock_input):
        self.player.roll_dice = lambda: 3
        self.player.play_turn("Human")
        self.assertEqual(self.player.total_score, 3)

    def test_play_turn_total_score(self):
        self.player.roll_dice = lambda: 4
        self.player.play_turn("Human")
        self.assertEqual(self.player.total_score, 4)

    def test_play_turn_total_score2(self):
        self.player.roll_dice = lambda: 6
        self.player.play_turn("Human")
        self.assertEqual(self.player.total_score, 6)

    def test_is_winner_false(self):
        self.assertFalse(self.player.is_winner())

    def test_is_winner_true(self):
        self.player.total_score = 50
        self.assertTrue(self.player.is_winner())

    def test_hold_score_turn_score(self):
        self.player.turn_score = 10
        self.player.hold_score()
        self.assertEqual(self.player.turn_score, 0)

    def test_hold_score_roll_score(self):
        self.player.roll_score = 5
        self.player.hold_score()
        self.assertEqual(self.player.roll_score, 0)

    def test_hold_score_total_score(self):
        self.player.total_score = 10
        self.player.hold_score()
        self.assertEqual(self.player.total_score, 10)



if __name__ == '__main__':
    unittest.main()