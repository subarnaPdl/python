import os
import random

print("\nHow To Play?")
print("Computer generates a random number between 1 and 100 and you have to guess it in 5 times.\n")
ans = random.randint(1, 100)
tries = 0


def repeat():
    global ans, tries
    tries += 1
    if tries <= 5:
        guess = int(input("Guess the number: "))
        if not(guess > 100 or guess < 0):
            diff = guess - ans
            if diff > 25:
                print("Your guess is very high.\n")
                repeat()

            elif diff > 10:
                print("Your guess is high.\n")
                repeat()

            elif diff > 0:
                print("Your guess is slightly higher.\n")
                repeat()

            elif diff < -25:
                print("Your guess is very low.\n")
                repeat()

            elif diff < -10:
                print("Your guess is low.\n")
                repeat()

            elif diff < -0:
                print("Your guess is slightly low.\n")
                repeat()

            else:
                print("Congratulations!! You guessed the right answer.\n")
                restart()

        else:
            print("Please enter a valid number.\n")
            repeat()

    else:
        print("Tries limit reached. You were unable to guess the answer.")
        print(f"Correct answer is: {ans}\n")
        restart()


def restart():
    global ans, tries
    restart = (input("Press y to restart the game: ")).lower()
    if restart == "y":
        tries = 0
        ans = random.randint(1, 100)
        os.system('cls')
        repeat()


repeat()
