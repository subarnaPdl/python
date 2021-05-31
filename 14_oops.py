class Details:

    # Following function works without calling it.
    def __init__(self, id):
        self.id = id
        print(f"{self.id} is created.")

    def info(self):
        print(f"My name is {self.name}.")
        print(f"My age is {self.age}.\n")

    # When @staticmethod is used, we should not pass the "self" parameter.
    @staticmethod
    def greet():
        print("Good Morning!!")


student1 = Details("Student1")
student1.name = "Subarna"
student1.age = 18
student1.info()  # Or, Details.info(student1)

student2 = Details("Student2")
student2.name = "Shreya"
student2.age = 16
Details.info(student2)  # Or, student2.info()

student3 = Details("Student3")
student3.name = "Ritesh"
student3.age = 17
student3.info()

# Calling to a staticmethod
Details.greet()  # Or, Details.info()
