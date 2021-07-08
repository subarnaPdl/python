for r in range(6):
    for cl in range(7):
        print('*', end="") if (r == 0 and cl % 3 != 0) or (r == 1 and cl %
                                                           3 == 0) or (r-cl == 2 or r+cl == 8) else print(" ", end="")
    print("")
