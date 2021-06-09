class Point:
    z = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def cm(cls):
        return cls(3, 4)

    # By using classmethod we can directly change the attributes of the class.
    def change_z(cls, z):
        cls.z = z

    def draw(self):
        print(f"Point ({self.x}, {self.y}, {self.z})")


point = Point(1, 2)
point.draw()

another = Point.cm()
another.change_z(5)
another.draw()
