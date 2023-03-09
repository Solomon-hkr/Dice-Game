
📝 Table of Contents

- 📝 Table of Contents
- 🧐 About
- 👨‍💻 Description
- 🏁 Getting Started
  - Installing
  - Usage
- ⛏️ Built Using


🧐 About

The project is a simple dice game. It is built for as an assignment for the course 'Methods of Sustainable Programming’.

👨‍💻 Description 

This is a pig dice game played between a computer and a human. 

🏁 Getting Started
 
The game can be played on cmd or any other terminal, such as Git Bash or VSC terminal. 

    Installing

Install the PIP packages that are dependencies to the project and/or the development environment. The dependencies are documented in the requirements.txt.
DO not forget toc check that you have an active venv.

    Usage

The game is played between two players. A computer and human.

The game has only one die to be rolled and six possibilities; i.e., the die has from 1 to 6 numbers. 

A player who first the maximum scored of 50 or more points will win the game.

There are three ways of counting the point on the game, the roll score, turn score, and total score. If a player pigs out he/she loses the turn score but keeps the total score that he/she has collected from the previous turn. 

The turn starts by human player by asking and registering a name. The computer will take its turn automatically if the human player is pigged out or wishes to hold turn score.

A human player can win the game faster/cheat if he/she wishes, by entering the 'w' key on the keyboard. In this case, the human will get more than 45 points immediately and run the game to fill the rest point.

If a player rolled 1, then he/she will be pigged out and his turn score will be zero. And the play turn will pass to the other player.

If a player wants to hold his turn point, he/she can hold it and pass the turn to the other player by entering 'h' key on the keyboard.

If the player wants to change name while playing, he/she can do so any time by entering the 'c' on the key board.

If the player wants to see list of the previous winners while playing, he/she can do so by entering the 'l' key on the keyboard.

If the player wants to quite the game and exit, he can enter the 's' key on the keyboard.

The computer player uses some intelligence wile playing the game. For example, it rolls it die every two seconds so that the human can follow along what the computer is doing. To see this functionality, the game has to be played on VSC terminal or on the command line(cmd) but on the Git Bash terminal this functionality might not be seen.

The computer also uses additional intelligence while playing the game. It holds its score each turn if it reaches 15 or more points. So that it avoids the risk of being pigged out and losing the whole turn score.

⛏️ Built Using

The game is built by using Python programming language on Visual Studio Code.




