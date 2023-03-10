
import unittest
from unittest.mock import patch
from main import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Solomon")

    def test_roll_dice(self):
        roll = self.player.roll_dice()
        self.assertTrue(1 <= roll <= 6)

    @patch('builtins.input', side_effect=[''])
    def test_play_turn_roll(self, mock_input):
        result = self.player.play_turn("Human")
        self.assertTrue(isinstance(result, bool))


    def test_play_turn_pigged_out(self):
        self.player.roll_dice = lambda: 1
        result = self.player.play_turn("Human")
        self.assertFalse(result)

    def test_hold_score(self):
        self.player.hold_score()
        self.assertEqual(self.player.turn_score, 0)
        self.assertEqual(self.player.roll_score, 0)

    def test_is_winner_false(self):
        self.assertFalse(self.player.is_winner())

    def test_is_winner_true(self):
        self.player.total_score = 50
        self.assertTrue(self.player.is_winner())

    def test_play_turn_roll_score(self):
        self.player.roll_dice = lambda: 4
        self.player.play_turn("Human")
        self.assertEqual(self.player.total_score, 4)

    def test_hold_score_reset_turn_score(self):
        self.player.turn_score = 5
        self.player.hold_score()
        self.assertEqual(self.player.turn_score, 0)

    def test_hold_score_total_score(self):
        self.player.turn_score = 5
        self.player.total_score = 10
        self.player.hold_score()
        self.assertEqual(self.player.total_score, 10)

    def test_max_score_default(self):
        self.assertEqual(self.player.max_score, 50)

    def test_max_score_custom(self):
        self.player.max_score = 100
        self.assertEqual(self.player.max_score, 100)

    def test_max_score_custom(self):
        self.player.max_score = 10
        self.assertEqual(self.player.max_score, 10)

    def test_max_score_min_value1(self):
        self.player.max_score = 1
        self.assertEqual(self.player.max_score, 1)

    def test_max_score_min_value2(self):
        self.player.max_score = 5
        self.assertEqual(self.player.max_score, 5)

    def test_max_score_max_value(self):
        self.player.max_score = 1000
        self.assertEqual(self.player.max_score, 1000)

    def test_turn_score(self):
        self.assertEqual(self.player.turn_score, 0)

    def test_roll_score(self):
        self.assertEqual(self.player.roll_score, 0)




if __name__ == '__main__':
    unittest.main()
