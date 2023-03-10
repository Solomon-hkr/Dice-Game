
from main import PlayerMain, Game
import unittest
from unittest.mock import patch


class TestPlayerMain(unittest.TestCase):
    def setUp(self):
        self.player = PlayerMain()

    def test_init(self):
        self.assertEqual(self.player.player_name, "")

    def test_valid_name(self):
        with patch('builtins.input', return_value='Solomon'):
            self.player.get_player_name()
            self.assertEqual(self.player.player_name, 'Solomon')

    def test_valid_name_more_words(self):
        with patch('builtins.input', return_value='Solomon Kash'):
            self.player.get_player_name()
            self.assertEqual(self.player.player_name, 'Solomon Kash')

    def test_invalid_name(self):
        with patch('builtins.input', side_effect=['123', 'So$e', 'Solomon1', 'Solomon'],) as mock_input:
            self.player.get_player_name()
            self.assertEqual(mock_input.call_count, 4)
            self.assertEqual(self.player.player_name, 'Solomon')

    def test_empty_input(self):
        with patch('builtins.input', side_effect=['', 'Solomon'],) as mock_input:
            self.player.get_player_name()
            self.assertEqual(mock_input.call_count, 2)
            self.assertEqual(self.player.player_name, 'Solomon')

    def test_whitespace_input(self):
        with patch('builtins.input', side_effect=['   ', 'Solomon'],) as mock_input:
            self.player.get_player_name()
            self.assertEqual(mock_input.call_count, 2)
            self.assertEqual(self.player.player_name, 'Solomon')

    def test_special_character_input(self):
        with patch('builtins.input', side_effect=['Solomon@', 'Solomon'],) as mock_input:
            self.player.get_player_name()
            self.assertEqual(mock_input.call_count, 2)
            self.assertEqual(self.player.player_name, 'Solomon')

    def test_number_input(self):
        with patch('builtins.input', side_effect=['Solomon123', 'Solomon'],) as mock_input:
            self.player.get_player_name()
            self.assertEqual(mock_input.call_count, 2)
            self.assertEqual(self.player.player_name, 'Solomon')

    def test_sign_input(self):
        with patch('builtins.input', side_effect=['=', 'Solomon'],) as mock_input:
            self.player.get_player_name()
            self.assertEqual(mock_input.call_count, 2)
            self.assertEqual(self.player.player_name, 'Solomon')

    def test_unicode_input(self):
        with patch('builtins.input', side_effect=['Solomon✨', 'Solomon'],) as mock_input:
            self.player.get_player_name()
            self.assertEqual(mock_input.call_count, 2)
            self.assertEqual(self.player.player_name, 'Solomon')

    def test_PlayerMain(self):
        game = Game(human_name="test_human_player")
        game.human_player.total_score = 45
        game.human_player.roll_dice = lambda: 1
        game.computer_player.roll_dice = lambda: 5
        game.state = "human_continue_or_hold"

        game.human_continue_or_hold()
        assert game.human_player.total_score == 45
        assert game.human_player.turn_score == 0
        assert game.computer_player.total_score == 0
        assert game.computer_player.turn_score == 0
        assert game.human_player.name == "test_human_player"




if __name__ == '__main__':
    unittest.main()
