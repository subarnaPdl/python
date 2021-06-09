class location:
    country = "Nepal"
    city = "Chitwan"
    Municipality = "Ratnanagar"
    num = 12

    # By running following fuction we can directly change the attributes of the class.

    # Method 1: Simple Method
    def changecountry(self):
        location.country = "France"

    # Method 2: Dumble tag method
    def changenum(self, num):
        self.__class__.num = num

    # But we prefer following method over method 2;
    # Method 3:
    @classmethod
    def changecity(cls, city):
        cls.city = city


a = location()

# Method 1
print(a.num)
a.changenum(13)
print(a.num)

# Method 2
print(a.country)
a.changecountry()
print(a.country)

# Method 3
print(a.city)
a.changecity("Kathmandu")
print(a.city)
