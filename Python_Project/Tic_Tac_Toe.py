# initializing the board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# winner variable for checking if any player have won
Winner = None

# runtime variable for checking game has ended or not
game_run = True

# player who is currently playing
Current_Player = "X"

# calculates the moves
total_play = 0


# displays the board in terminal
def display_board():
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i + 1] + " | " + board[i + 2])


# for flipping the turn for player
def flip_turn():
    global Current_Player

    if Current_Player == "X":
        Current_Player = "O"

    elif Current_Player == "O":
        Current_Player = "X"

    return


# Giving player to choose value turn by turn
def play_game():

    while game_run:

        display_board()

        prompt()

        if total_play >= 5:
            check_win()

        flip_turn()

    display_board()
    if Winner:
        print(f"\nPlayer \"{Winner}\" won")
    else:
        print("Game has been tied")


# prompting and re-prompting for user
def prompt():
    global total_play
    print(f"{Current_Player}'s turn.")

    while True:
        try:
            position = int(input("Enter the position from 1 - 9: "))

            if position in range(1, 10):
                position = position - 1

                if board[position] == "-":
                    board[position] = Current_Player
                    total_play += 1
                    break
                else:
                    print("Position is occupied. Please choose again.")
            else:
                print("Choose the value only from 1 - 9.")

        except ValueError:
            print("Only integer value is accepted.")


# checks if the player have won the match or not
def check_win():
    global Winner, game_run
    if check_row() or check_column() or check_diagonal():
        Winner = Current_Player
        game_run = False

    elif check_tie():
        Winner = None
        game_run = False


def check_row():
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        return True

    return False


def check_column():
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        return True

    return False


def check_diagonal():
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        return True

    return False


def check_tie():
    if "-" not in board:
        return True

    return False

# for resetting all to beginning
def reset():
    global Winner, game_run, total_play, Current_Player, board

    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]

    Winner = None
    Current_Player = "X"
    game_run = True
    total_play = 0


def main():

    while True:
        reset()
        play_game()

        again = (input("\nDo you wish to play again? ").strip()).lower()

        if again != "y" or again != "yes":
            break



if __name__ == "__main__":
    main()
