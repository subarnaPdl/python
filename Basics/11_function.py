# Defining the function
def greet(name, gre):
    return ("Hello " + gre + " " + name)


# Input Section
name = input("Enter your name: ")
gender = input("Enter your gender: ")

# Condition to check for the greeting Mr or Mrs
if gender.lower() == "male":
    gre = "Mr."
elif gender.lower() == "female":
    gre = "Mrs."
else:
    gre = " "

# Calling the function
print(greet(name, gre))
