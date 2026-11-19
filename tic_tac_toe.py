
# Tic-Tac-Toe with Simple AI
# CodeOrbit Tech Internship - Task 2

import math

# Create an empty 3x3 board
board = [" " for _ in range(9)]

# Display the game board
def display_board():
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i+3]))
        if i < 6:
            print("---+---+---")
    print()


# Check whether a player has won
def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


# Check whether the board is full
def is_draw():
    return " " not in board


# Minimax algorithm for computer AI
def minimax(is_maximizing):

    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(False)

                board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                score = minimax(True)

                board[i] = " "
                best_score = min(score, best_score)

        return best_score


# Computer chooses the best move
def computer_move():

    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":

            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    if best_move is not None:
        board[best_move] = "O"
        print("Computer selected position:", best_move + 1)


# Main game
def play_game():

    print("WELCOME TO TIC-TAC-TOE!")
    print("You are X and Computer is O.")
    print("Choose a position from 1 to 9.")

    display_board()

    while True:

        # User's turn
        try:
            move = int(input("Enter your position (1-9): ")) - 1

            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid position! Try again.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        board[move] = "X"
        display_board()

        if check_winner("X"):
            print("Congratulations! You Win!")
            break

        if is_draw():
            print("Game Draw!")
            break

        # Computer's turn
        print("Computer is thinking...")
        computer_move()
        display_board()

        if check_winner("O"):
            print("Computer Wins! Better luck next time.")
            break

        if is_draw():
            print("Game Draw!")
            break


# Start the game
play_game()
