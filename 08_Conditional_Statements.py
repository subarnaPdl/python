a = input("Enter a number: ")
a = int(a)

# Condittion Checker
if (a < 0):
    print(a, "is less than zero.")

elif (a == 0):
    print(a, "is equal to zero.")

else:
    print(a, "is greater than zero.")

# Check whether the inputed number is present in num list or not.
nums = [1, 2, -3, -1]
print("The presence of", a, "in list", nums, "is", a in nums, ".")
