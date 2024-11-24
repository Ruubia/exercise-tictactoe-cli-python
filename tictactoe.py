# Function to print the board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# Function to check for a winner
def check_for_winner(board):
    winning_combinations = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Center column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal 1
        [2, 4, 6]   # Diagonal 2
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
            return board[combo[0]]  # Return the winner (X or O)
    
    if " " not in board:  # No spaces left means the game is a draw
        return "Draw"
    
    return None  # No winner yet

# Function to play a move
def play(board, position, player):
    if board[position] == " ":
        board[position] = player
        return True
    return False

# Function to start a new game
def new_game():
    return [" "] * 9  # Reset the board to empty spaces

def main():
    board = new_game()  # Initialize the game
    current_player = "X"
    
    while True:
        print_board(board)
        position = input(f"Player {current_player}, enter your move (1-9) or 'exit' to quit: ").strip().lower()

        if position == "exit":
            print("Exiting the game. Goodbye!")
            break
        
        if position == "reset":
            board = new_game()  # Reset the game
            print("The game has been reset!")
            continue

        try:
            position = int(position) - 1  # Convert to 0-indexed
            if position < 0 or position >= 9:
                print("Invalid position. Please enter a number between 1 and 9.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9, or 'exit' to quit.")
            continue

        # Try to play the move
        if not play(board, position, current_player):
            print(f"Position {position+1} is already taken. Try again.")
            continue

        # Check if someone won or if it's a draw
        winner = check_for_winner(board)
        if winner:
            print_board(board)
            if winner == "Draw":
                print("It's a draw!")
            else:
                print(f"Player {winner} wins!")
            restart = input("Do you want to play again? (y/n): ").strip().lower()
            if restart == "y":
                board = new_game()  # Reset for a new game
                current_player = "X"  # X always starts first
            else:
                print("Exiting the game. Goodbye!")
                break
        else:
            # Switch player
            current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
