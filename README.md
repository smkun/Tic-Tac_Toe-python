# Tic-Tac-Toe Game

This is a simple command-line implementation of the classic Tic-Tac-Toe game in Python. The game allows two players to take turns marking spaces on a 3x3 grid until one player wins or the game ends in a draw.

## How to Play

1. Run the Python script to start the game.
2. The game board will be displayed with labeled columns (1, 2, 3) and rows (A, B, C).
3. Players take turns entering their moves by specifying the cell they want to mark.
    - To make a move, enter the column letter (A, B, or C) followed by the row number (1, 2, or 3).
    - For example, to mark the cell in the first row and first column, enter "A1".
4. The game will validate each move and update the board accordingly.
5. The game continues until one of the following conditions is met:
    - A player wins by marking three cells in a row, column, or diagonal.
    - All cells are filled, resulting in a draw.
6. After the game ends, players can choose to play again or quit.

## Game Features

-   Player-friendly move input using column letters and row numbers.
-   Input validation to ensure valid moves within the board range.
-   Clear display of the game board after each move.
-   Detection of winning conditions and declaration of the winner.
-   Detection of a draw when all cells are filled without a winner.
-   Option to play multiple rounds or quit after each game.

## Requirements

-   Python 3.x

## How to Run

1. Clone the repository or download the Python script.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the following command:

    ```
    python tic_tac_toe.py
    ```

    Replace `tic_tac_toe.py` with the actual filename if necessary.

4. Follow the on-screen instructions to play the game.

## Code Structure

The code is organized into several functions:

-   `display_board(board)`: Displays the current state of the game board.
-   `check_win(board, player)`: Checks if a player has won the game.
-   `make_move(board, player, row, col)`: Makes a move on the game board.
-   `play_game()`: Main function that orchestrates the gameplay.

The game logic is implemented in the `play_game()` function, which handles player turns, move validation, and game termination conditions. The game board is represented as a 3x3 matrix using a list of lists.

## Acknowledgments

This Tic-Tac-Toe game implementation is a beginner-friendly project inspired by various online tutorials and examples. It serves as a learning resource for those starting with Python programming and game development.

Feel free to modify and enhance the game as per your requirements. Enjoy playing Tic-Tac-Toe!
