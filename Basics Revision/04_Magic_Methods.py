# Here __init__ and __str__ are the examples of the magic method.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point ({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
# Try printing out the following code by removing the __str__ method.
print(point)
