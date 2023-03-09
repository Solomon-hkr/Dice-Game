
import random
import time
import os


class Player:
    def __init__(self, name=None):
        if name is None:
            name = input("Enter your name")
        self.name = name
        self.max_score = 50
        self.roll_score = 0
        self.turn_score = 0
        self.total_score = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def play_turn(self, player_type):
        print()

        if player_type == "Human":
            input("Press enter to roll the die...")
            print()

        roll = self.roll_dice()
        print(f"{self.name} rolled: {roll}")
        if roll == 1:
            print("Pigged out!")
            self.total_score -= self.turn_score
            self.turn_score = 0
            self.roll_score = 0            
            print(f"Turn score is: {self.turn_score}")
            print(f"Total score is: {self.total_score}")
            print()
            return False

        else:
            self.roll_score = roll
            self.turn_score += roll
            self.total_score += self.roll_score
            print(f"Current turn score: {self.turn_score}")
            print(f"Total score: {self.total_score}")
            return True

    def hold_score(self):

        self.roll_score = 0
        self.turn_score = 0
        print(f"\nThe current player chose to hold the score: \nTotal score: {self.total_score}")
        print()

    def is_winner(self):
        return self.total_score >= self.max_score


class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def set_name(self, new_name):
        self.name = new_name



class ComputerPlayer(Player):
    def __init__(self):
        super().__init__("Computer")



class Game:
    def __init__(self, human_name=None):
        self.human_player = HumanPlayer(human_name)
        self.computer_player = ComputerPlayer()
        self.state = "human_turn"

    def play_game(self):
        while True:
            if self.human_player.is_winner():
                print(f"\n{self.human_player.name} wins with a total score of {self.human_player.total_score}!")
                self.record_result(self.human_player.name, self.human_player.total_score)

                play_or_not = input("\nDo you want to continue playing the game? Enter 'y': To stop the game press any key: ").lower()
                print()
                if play_or_not == 'y':                    
                    self.human_player.turn_score = 0
                    self.human_player.total_score = 0
                    self.computer_player.turn_score = 0
                    self.computer_player.total_score = 0
                    self.state = "human_turn"
                else:
                    raise SystemExit()

            elif self.computer_player.is_winner():
                print(f"\n{self.computer_player.name} wins with a total score of {self.computer_player.total_score}!")
                self.record_result(self.computer_player.name, self.computer_player.total_score)

                play_or_not = input("\nDo you want to continue playing the game? Enter 'y': To stop the game press any key: ").lower()
                print()
                if play_or_not == 'y':                    
                    self.human_player.turn_score = 0
                    self.human_player.total_score = 0                   
                    self.computer_player.turn_score = 0
                    self.computer_player.total_score = 0
                    self.state = "human_turn"
                else:
                    raise SystemExit()

            if self.state == "human_turn":
                self.human_turn()

            elif self.state == "human_continue_or_hold":
                self.human_continue_or_hold()

            elif self.state == "computer_turn":
                self.computer_turn()

            elif self.state == "computer_continue_or_hold":
                self.computer_continue_or_hold()


    def human_turn(self):
        print(f"{self.human_player.name}'s turn")
        return_value = self.human_player.play_turn("Human")

        if return_value:
            self.state = "human_continue_or_hold"

        else:
            self.state = "computer_turn"

    def human_continue_or_hold(self):
        continue_or_hold = input("\nTo stop playing press 's'. To see list of winners press 'l'. To change your name press 'c' \n" +
                                 "To win faster press'w'. To hold the current total score press 'h'. To continue playing press enter: ").lower()
        print()                

        if continue_or_hold == "":
            self.state = "human_turn"

        elif continue_or_hold == 'w':
            self.human_player.total_score = 48
            self.state = "human_turn"

        elif continue_or_hold == "h":
            self.human_player.hold_score()
            self.state = "computer_turn"

        elif continue_or_hold == "l":
            self.print_winners()
            self.state = "human_continue_or_hold"

        elif continue_or_hold == "c":
            new_name = input("Enter your new name: ")
            self.human_player.set_name(new_name)
            print(f"\nYour name has been changed to '{new_name}'")
        
        elif continue_or_hold == "s":
            print("Goodbye!")
            print()
            raise SystemExit()


    def computer_turn(self):
        print("Computer's turn")
        time.sleep(2)

        if self.computer_player.play_turn("Computer"):
            self.state = "computer_continue_or_hold"

        else:
            self.state = "human_turn"


    def computer_continue_or_hold(self):
        if self.computer_player.turn_score >= 15:
            self.computer_player.hold_score()
            self.state = "human_turn"

        else:
            self.state = "computer_turn"


    def record_result(self, name, total_score):
        # Check if the file exists
        if not os.path.exists('winners.txt'):
            # If it does not exist, create it with this contents
            with open('winners.txt', 'w') as f:
                f.write("         List of Winners \n")

        # Open the file and read the current list of winners
        with open('winners.txt', 'r') as f:
            winners = f.readlines()

        # Add the new winner with their score to the beginning of the list
        winners.insert(1, name + ' : ' + str(total_score) + '\n')
        
        # Remove the last winner if there are more than 10 winners
        if len(winners) > 11:
            winners.pop()

        # Write the updated list of winners to the file
        with open('winners.txt', 'w') as f:
            f.writelines(winners)

    def print_winners(self):
        with open("winners.txt", "r") as file:
            print(file.read())



class PlayerMain:
    def __init__(self):
        self.player_name = ""

    def get_player_name(self):
        max_attempts = 5
        attempts = 0
        print("\n            Welcome to the game!")
        while attempts < max_attempts:
            new_player = input("\nEnter your name to play: ")
            print()
            if new_player.replace(" ", "").isalpha():
                self.player_name = new_player
                return
            else:
                attempts += 1
                remaining_attempts = max_attempts - attempts
                if remaining_attempts > 0:
                    print(f"Name should be only alphabets. Please try again. {remaining_attempts} attempts remaining.")
                else:
                    print(f"You have exceeded the maximum number of attempts ({max_attempts}). Please start over again.")
                    raise SystemExit()

    def main(self):
        self.get_player_name()
        my_game = Game(self.player_name)
        my_game.play_game()



if __name__ == "__main__":
    player_game = PlayerMain()
    player_game.main()