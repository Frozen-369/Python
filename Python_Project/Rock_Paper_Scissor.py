import random
while True:
    choices = ["R", "P", "S"]
    player_1 = None
    computer_0 = random.choice(choices)
    while player_1 not in choices:
        player_1 = input("Player 1 Turn : Choose from R/P/S ").upper()
    print("Computer Turn : ", computer_0)
    print("Player 1 : ", player_1)
    print("Computer : ", computer_0)

    def game(player, computer):
        if player == computer:
            return None
        if player == "R":
            if computer == "P":
                return False
            if computer == "S":
                return True

        if player == "P":
            if computer == "S":
                print("Computer Wins.")
            if computer == "R":
                return True

        if player == "S":
            if computer == "R":
                return False
            if computer == "P":
                return True

    win_lose = game(player_1, computer_0)

    if win_lose == True:
        print("Player 1 Wins.")

    elif win_lose == False:
        print("Computer Wins.")

    else:
        print("Game is a Tie!")

    game = input("Do you want to play again(y/n) ").lower()

    if game != "y":
        break
print("Thanks For Playing.")
