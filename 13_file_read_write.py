# Writing in the file
f = open("13_text.txt", "w")
f.write("Hello! My name is Subarna Poudel. ")
f.close()

# Reading from the file     Method 1
m1 = open("13_text.txt", "r")
print(m1.read())
m1.close()

# Appending to the file
appen = open("13_text.txt", "a")
appen.write("I'm 18 years old.")
appen.close()

# Reading from the file     Method 2
with open("13_text.txt") as m2:
    print(m2.read())
    # No need to close in this method
