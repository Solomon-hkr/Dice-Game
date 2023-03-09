
import unittest
import io
from unittest import TestCase
from unittest.mock import patch
from main import Player, HumanPlayer, ComputerPlayer, Game


class TestGame(TestCase):
    @patch('random.randint')
    def test_human_turn_roll_score_1(self, mock_randint):
        mock_randint.return_value = 1
        game = Game(human_name="Test Player")
        game.human_turn()
        self.assertEqual(game.human_player.roll_score, 0)
        self.assertEqual(game.human_player.turn_score, 0)
        self.assertEqual(game.human_player.total_score, 0)
        self.assertEqual(game.state, "computer_turn")
    
    @patch('random.randint')
    def test_human_turn_roll_score_2(self, mock_randint):
        mock_randint.return_value = 2
        game = Game(human_name="Test Player")
        game.human_turn()
        self.assertEqual(game.human_player.roll_score, 2)
        self.assertEqual(game.human_player.turn_score, 2)
        self.assertEqual(game.state, "human_continue_or_hold")

    @patch('random.randint')
    def test_human_turn_roll_score_6(self, mock_randint):
        mock_randint.return_value = 6
        game = Game(human_name="Test Player")
        game.human_turn()
        self.assertEqual(game.human_player.roll_score, 6)
        self.assertEqual(game.human_player.turn_score, 6)
        self.assertEqual(game.state, "human_continue_or_hold")

    @patch('random.randint')
    def test_human_turn_is_winner(self, mock_randint):
        mock_randint.return_value = 6
        game = Game(human_name="Test Player")
        game.human_player.total_score = 49
        game.human_turn()
        self.assertEqual(game.human_player.total_score, 55)
        self.assertEqual(game.human_player.is_winner(), True)


    @patch('random.randint')
    def test_human_continue_or_hold_h(self, mock_randint):
        game = Game(human_name="Test Player")
        game.human_player.total_score = 5
        game.state = "human_continue_or_hold"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            with patch('builtins.input', side_effect=["h"]):
                game.human_continue_or_hold()
                self.assertEqual(fake_stdout.getvalue().strip(), "The current player chose to hold the score: \nTotal score: 5")
        self.assertEqual(game.human_player.roll_score, 0)
        self.assertEqual(game.human_player.turn_score, 0)
        self.assertEqual(game.human_player.total_score, 5)
        self.assertEqual(game.state, "computer_turn")

    @patch('random.randint')
    def test_human_continue_or_hold_w(self, mock_randint):
        game = Game(human_name="Test Player")
        game.state = "human_continue_or_hold"
        with patch('builtins.input', side_effect=["w"]):
            game.human_continue_or_hold()
        self.assertEqual(game.human_player.total_score, 48)
        self.assertEqual(game.state, "human_turn")

    @patch('random.randint')
    def test_human_continue_or_hold_s(self, mock_randint):
        game = Game(human_name="Test Player")
        game.state = "human_continue_or_hold"
        with patch('builtins.input', side_effect=["s"]):
            with self.assertRaises(SystemExit):
                game.human_continue_or_hold()

    def test_human_player_name(self):
        human_player = HumanPlayer("Solomon")
        self.assertEqual(human_player.name, "Solomon")

    def test_computer_player_name(self):
        computer_player = ComputerPlayer()
        self.assertEqual(computer_player.name, "Computer")

    def test_roll_dice(self):
        player = Player("Test")
        roll = player.roll_dice()
        self.assertTrue(roll >= 1 and roll <= 6)

    @patch("builtins.input", side_effect=["", "s"])
    def test_human_player_hold_score(self, mock_input):
        human_player = HumanPlayer("Solomon")
        human_player.total_score = 20
        human_player.turn_score = 10
        human_player.hold_score()
        self.assertEqual(human_player.total_score, 20)
        self.assertEqual(human_player.turn_score, 0)

    def test_computer_player_play_turn(self):
        computer_player = ComputerPlayer()
        computer_player.total_score = 0
        computer_player.play_turn("Computer")
        self.assertTrue(computer_player.turn_score >= 0 and computer_player.turn_score <= 6)
        self.assertTrue(computer_player.total_score >= 0 and computer_player.total_score <= 6)

    def test_is_winner(self):
        player = Player("Test")
        player.total_score = 51
        self.assertTrue(player.is_winner())

    def test_not_is_winner(self):
        player = Player("Test")
        player.total_score = 49
        self.assertFalse(player.is_winner())


if __name__ == "__main__":
    unittest.main()
