class Army():  # Outer Class
    def __init__(self):
        self.name = "Subarna"
        self.gn = self.Gun()  # Creating inner class object

    def show(self):
        print("Name: ", self.name)

    class Gun():  # Inner Class
        def __init__(self):
            self.name = "AK47"
            self.capacity = 75

        def disp(self):
            print("Gun Name: ", self.name)
            print("Capacity: ", self.capacity)


a = Army()
a.show()
a.gn.disp()
