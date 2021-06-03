import string
import random

hangman_words = ["Mouse", "Snake", "Leopard", "Lion", "Tiger", "Monkey"]
word = (random.choice(hangman_words)).upper()

alphabets = set(string.ascii_uppercase)
answer_letters = set(word)
# All the used letters. Contains both right and wrong letters.
used_letters = set()
# Used letters. Contains only right letters.
used_correct_letters = set()

tries = 0

while tries < 6:

    # Print the hangman letters
    wordlist = [
        letter if letter in used_correct_letters else '-' for letter in word]
    print(f"\n{' '.join(wordlist)}")

    # Taking input from user
    user_input = (input("Enter a letter: ")).upper()

    # Check for the duplicate input
    if not(user_input in used_letters):
        # Checks whether the user have typed other than alplabets
        if user_input in alphabets:
            # Adds the input letter in the set, both correct and wrong.
            used_letters.add(user_input)
            # Adds the letter in the set if the letter is correct.
            if user_input in answer_letters:
                used_correct_letters.add(user_input)
            else:
                tries += 1
        else:
            print("Please enter a valid letter.\n")
    else:
        print(f"Letter {user_input} is already used.\n")

    # Used Letters
    print(f"Used Letters: {' '.join(used_letters)}")

    #Remaining tries
    print(f"Remaining Tries: {6-tries}")

    # Win checker
    if used_correct_letters == answer_letters:
        print(f"\nAnswer: {' '.join(word)}\nYou win.\n")
        break

else:
    print(f"\nAnswer: {' '.join(word)}\nYou lose.\n")
