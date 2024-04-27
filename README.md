# Python CLI Tic-Tac-Toe

Welcome to the Python CLI Tic-Tac-Toe! This simple command-line version of the classic game allows two players to compete in a turn-based fashion, making moves in a shared 3x3 grid.

## Description

The game is played on a grid that's 3 squares by 3 squares. Players take turns putting their marks (either 'X' or 'O') in empty squares. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner. When all 9 squares are full, if no player has 3 marks in a row, the game is considered a draw.

## Features

- 2-player gameplay on the same machine
- Simple and intuitive text-based interface
- Checks for win or draw conditions after every move
- Alternating turns between players

## How to Play

1. Start the script in a Python environment.
2. The game will prompt `Joueur 1` to enter a number between `1-9`.
3. The input corresponds to the position on the grid:
   - 1 for the top-left corner
   - 9 for the bottom-right corner
4. `Joueur 2` follows with their input.
5. The game continues to alternate between players until a winner is declared or a draw occurs.

## Instructions

1. Clone or download this repository to your local machine.
2. Ensure that you have Python installed. This script is compatible with Python 3.x.
3. Navigate to the directory containing the game file in your terminal or command prompt.
4. Run the script using the command: `python tic_tac_toe.py`
5. Follow the on-screen prompts to play the game.

## Functions

- `draw()`: Prints the current state of the board.
- `check_win()`: Checks for a winning condition on the board.
- `check_draw()`: Checks whether the board is full and the game is a draw.
- Game loop: Facilitates the alternating player turns and checks for game end conditions.

## Sample Game

Joueur 1[1-9]: 1

##### X . .

##### . . .

##### . . .

Joueur 2[1-9]: 5

##### X . .

##### . O .

##### . . .
