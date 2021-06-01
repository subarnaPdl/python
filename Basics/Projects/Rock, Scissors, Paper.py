import os
import random


def game():
    # Computers choice
    rand = random.randint(1, 3)
    if rand == 1:
        comp = "r"
    elif rand == 2:
        comp = "s"
    else:
        comp = "p"

    # Users choice
    user = input("\nEnter rock(r) / scissors(s) / paper(p): ")

    # Win Checker
    if user != comp:
        if user == "r":
            if comp == "s":
                print("Rock over scissors. You won the game.")
            else:
                print("Paper over rock. Computer won the game.")

        elif user == "s":
            if comp == "p":
                print("Scissors over paper. You won the game.")
            else:
                print("Rock over scissors. Computer won the game.")

        else:
            if comp == "r":
                print("Paper over rock. You won the game.")
            else:
                print("Scissors over paper. Computer won the game.")

    else:
        if user == "r":
            print("Rock over rock. Its a draw.")
        elif user == "s":
            print("Scissors over scissors. Its a draw.")
        else:
            print("Paper over paper. Its a draw.")

    restart = (input("\nPress y to restart the game: ")).lower()
    if restart == "y":
        os.system("cls")
        game()


# Starting the game
game()
