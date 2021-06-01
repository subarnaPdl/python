class main:
    valueType = "Data type is Personal Info"
    name = gender = "Unidentified"

    def info(self):
        print(f"{self.name} is {self.gender}.")


# By doing this we set percentage as the subset of main.
class percentage(main):
    valueType = "Data type is percentage."

    def marks(self):
        print(f"{self.name} secured {self.percent}%.")


percent = percentage()
# Prints the dataType attribute of percentage class instead of main class.
print(percent.valueType)
# Assigning the values to percentage class assign for the main class too as:
percent.name = "Subarna"
percent.gender = "male"
# Calling the info method of main class from the percentage class.
percent.info()

# Assigning the value for the percentage class.
percent.percent = 90
# Calling the marks method available inside the percentage class.
percent.marks()
