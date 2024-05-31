# Initialize the game board as a 3x3 matrix filled with empty spaces
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def display_board(board):
    """
    Display the game board with labeled columns and rows.
    """
    print("   1   2   3")
    for i, row in enumerate(board, start=1):
        print(f"{chr(64+i)}  {' | '.join(row)} ")
        if i < 3:
            print("  -----------")

def check_win(board, player):
    """
    Check if a player has won the game.
    Returns True if the player has won, False otherwise.
    """
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def make_move(board, player, row, col):
    """
    Make a move on the game board.
    Returns True if the move is valid and made successfully, False otherwise.
    """
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else:
        return False

def play_game():
    """
    Main function to play the Tic-Tac-Toe game.
    """
    players = ['X', 'O']
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")
    display_board(board)

    while True:
        player = players[current_player]
        move = input(f"Player {player}, enter your move (e.g., A1): ").upper()
        row = ord(move[0]) - 65
        col = int(move[1]) - 1

        if 0 <= row < 3 and 0 <= col < 3:
            if make_move(board, player, row, col):
                display_board(board)
                if check_win(board, player):
                    print(f"Player {player} wins!")
                    break
                elif all(cell != ' ' for row in board for cell in row):
                    print("It's a draw!")
                    break
                current_player = (current_player + 1) % 2
            else:
                print("Invalid move. That cell is already occupied. Try again.")
        else:
            print("Invalid move. Enter a valid cell (e.g., A1, B2, C3).")

    play_again = input("Do you want to play again? (Y/N): ").upper()
    if play_again == 'Y':
        # Reset the board for a new game
        for row in board:
            for col in range(3):
                row[col] = ' '
        play_game()
    else:
        print("Thanks for playing!")

# Run the game when the script is executed directly
if __name__ == "__main__":
    play_game()  # Start the game by calling the play_game function