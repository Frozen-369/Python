import random

while True:
    guess = random.randrange(0, 100)
    user = None
    guess_count = 0
    while guess != user:
        user = int(input("Guess a number from 1 to 100 : "))
        guess_count += 1

        def game():
            if user > guess:
                return f"The number {user} you have guessed is greater than the number choosed by computer."
            elif user < guess:
                return f"The number {user} you have guessed is smaller than the number choosed by computer."
            else:
                return f"Congo! The number {user} matches the number choosed by computer. You guessed right in {guess_count} turns."
        print(game())

    if guess_count <= 10:
        print(f"Bravo!You are a genius to guess in {guess_count} turns.")
    else:
        print("You're a dumbass.You fool.")

    with open("PG_Highscore.txt", "r") as PG_game:
        high_score = int(PG_game.read())
    if guess_count < high_score:
        print("You have just broken the high score!")
        with open("PG_Highscore.txt", "w") as PG_game:
            PG_game.write(str(guess_count))

    play_again = input("Press y to play again : ").lower()
    if play_again != "y":
        break
