import numpy as np
import random

# Define constants for the game
ROWS = 6
COLS = 7
EMPTY = 0
PLAYER_1 = 1  # Human Player
PLAYER_2 = 2  # Computer Player

# Function to create the game board
def create_board():
    board = np.zeros((ROWS, COLS), int)
    return board

# Function to print the current state of the board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join([str(cell) if cell != 0 else "." for cell in row]))
        print("-" * 29)
    print("\n")

# Function to check if a move is valid
def is_valid_move(board, col):
    return board[0][col] == EMPTY

# Function to get the next available row for a given column
def get_next_available_row(board, col):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == EMPTY:
            return row
    return -1

# Function to drop a piece in the given column
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Function to check for a win
def check_win(board, piece):
    # Check horizontal locations
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == piece for i in range(4)):
                return True

    # Check vertical locations
    for row in range(ROWS - 3):
        for col in range(COLS):
            if all(board[row + i][col] == piece for i in range(4)):
                return True

    # Check positively sloped diagonals
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == piece for i in range(4)):
                return True

    # Check negatively sloped diagonals
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == piece for i in range(4)):
                return True

    return False

# Function to handle the computer's move
def computer_move(board):
    available_moves = [col for col in range(COLS) if is_valid_move(board, col)]
    return random.choice(available_moves)

# Main game loop (Human vs Computer)
def play_game():
    board = create_board()
    game_over = False
    turn = 0  # 0 for Player (Human) turn, 1 for Computer turn
    
    while not game_over:
        print_board(board)
        
        if turn == 0:  # Human Player's Turn
            player = PLAYER_1
            print("Player's Turn (X)")
            valid_move = False
            while not valid_move:
                try:
                    col = int(input(f"Choose a column (0-6): "))
                    if col < 0 or col >= COLS:
                        print("Invalid column. Please choose a column between 0 and 6.")
                        continue
                    if is_valid_move(board, col):
                        row = get_next_available_row(board, col)
                        drop_piece(board, row, col, player)
                        valid_move = True
                    else:
                        print("Column is full. Choose a different column.")
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 6.")
        else:  # Computer's Turn (No User Input)
            player = PLAYER_2
            print("Computer's Turn (O)")
            col = computer_move(board)  # The computer selects a column randomly
            row = get_next_available_row(board, col)
            drop_piece(board, row, col, player)
            print(f"Computer chose column {col}.")

        # Check for a win
        if check_win(board, player):
            print_board(board)
            if player == PLAYER_1:
                print("Player wins!")
            else:
                print("Computer wins!")
            game_over = True

        # Switch turns
        turn = (turn + 1) % 2  # Alternate between 0 and 1 (Human vs Computer)

# Start the game
if __name__ == "__main__":
    play_game()


