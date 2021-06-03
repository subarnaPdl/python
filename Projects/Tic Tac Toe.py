# pos_text = ['1', ' 2', '3', '4', '5', '6', '7', '8', '9']
pos_text = [str(i+1) for i in range(9)]
win_condition = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8],
                 [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8]]
current_turn = 'X'


def gameIntro():
    # Game Introduction
    print("\n")
    print("   How to Play")
    print("---------------------\n")
    print("Board design looks like:\n")
    newTable()
    print("\nEnter the position(in number) where you want to place X or O. For example enter 1 for first place.")
    print("Start the game by entering the players name.")

    # Players name input section
    global player1, player2
    player1 = input("Player 1 name (X character): ")
    player2 = input("Player 2 name (O character): ")
    # Play Zone
    playZone()


def playZone():
    global current_turn
    # Input the position from the user
    current_pos = int(
        input(f"\n{player1 if current_turn=='X' else player2} enter the position ({current_turn} character): "))
    # As the index for user starts from 1, we subtract here by 1
    current_pos -= 1
    # Checks whether the user inputs used or wrong index or not
    if current_pos < 9 and pos_text[current_pos] != 'X' and pos_text[current_pos] != 'O':
        pos_text[current_pos] = current_turn
        current_turn = 'X' if current_turn == 'O' else 'O'
        newTable()  # Creates a new table
        winCheck()  # Checks for winner

    else:
        print("\nWrong Value\n")
        playZone()


# Creates a table format
def newTable():
    print(f"{pos_text[0]} | {pos_text[1]} | {pos_text[2]}")
    print("----------")
    print(f"{pos_text[3]} | {pos_text[4]} | {pos_text[5]}")
    print("----------")
    print(f"{pos_text[6]} | {pos_text[7]} | {pos_text[8]}")


# Checks for the winner
def winCheck():
    draw_count = 1
    # Checking for winner
    for i in range(8):
        a = pos_text[win_condition[i][0]]
        b = pos_text[win_condition[i][1]]
        c = pos_text[win_condition[i][2]]
        if a == b and b == c:
            if a == 'X':
                print(f"\n{player1} won the game.\n",)

            elif a == 'O':
                print(f"\n{player2} won the game.\n", )

            return

         # Draw checker function
        elif pos_text[i] == 'X' or pos_text[i] == 'O':
            draw_count += 1

    # Checking for draw
    if draw_count == 9:
        print("\nDraw\n")
        return

    # Continuing the function
    playZone()


# Starting the game
gameIntro()
