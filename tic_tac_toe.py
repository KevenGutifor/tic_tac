# A two-player game where players take turns marking a 3x3 grid

import pandas as pd
import os

# Initialize the game board
board = [" " for _ in range(10)]
desk = []

# Function to print the current state of the board
def print_board():
    print("\n")
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print(" | ".join(row))
        print("-" * 9)

# Function to check for a win or tie
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full
def is_board_full():
    return " " not in board

# Main function to handle the game loop
def play_game():
    current_player = "X"
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if move < 0 or move >= 9 or board[move] != " ":
                print("Invalid move! Please choose an empty position between 1 and 9.")
                continue

            board[move] = current_player
            print_board()

            if check_winner(current_player):
                print(f"Player {current_player} wins!")
                break

            if is_board_full():
                print("It's a tie!")
                break

            current_player = "O" if current_player == "X" else "X"
        
        except ValueError:
            print("Please enter a valid number between 1 and 9.")

# Start the game when the script is executed
if __name__ == "__main__":
    play_game()
