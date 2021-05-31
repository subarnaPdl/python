class location:
    country = "Nepal"
    city = "Chitwan"
    Municipality = "Ratnanagar"
    num = 12

    # By running following fuction we can directly change the attributes of the class.
    def changenum(self, num):
        self.__class__.num = num

    # But we prefer another method over it which is;
    @classmethod
    def changecity(self, city):
        self.city = city


a = location()

# Method 1
print(a.num)
a.changenum(13)
print(a.num)

# Method 2
print(a.city)
a.changecity("Kathmandu")
print(a.city)
