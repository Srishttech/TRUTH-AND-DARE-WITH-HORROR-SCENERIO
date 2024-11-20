import random

def print_board(board):
    print("-----------")
    for i in range(3):
        
        print(f" | {board[i * 3]} | {board[i * 3 + 1]} | {board[i * 3 + 2]} |")
        
    print("-----------")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_board_full(board):
    return all(spot != ' ' for spot in board)

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                return move
            else:
                print("The spot is already taken, try again.")
        except (ValueError, IndexError):
            print("Invalid input, please enter a number between 1 and 9.")

def computer_move(board):
    available_moves = [i for i, spot in enumerate(board) if spot == ' ']
    return random.choice(available_moves)

def play_game():
    board = [' '] * 9
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    current_player = 'X'
    
    while True:
        if current_player == 'X':
            move = player_move(board)
        else:
            print("Computer is making a move...")
            move = computer_move(board)
        
        board[move] = current_player
        print_board(board)
        
        if check_winner(board, current_player):
            if current_player == 'X':
                print("Congratulations! You win!")
            else:
                print("Computer wins! Better luck next time.")
            break
        
        if is_board_full(board):
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
