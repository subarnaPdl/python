class Point:
    default_color = "Red"  # Class Variable

    def __init__(self, x, y):
        self.x = x  # Instance Variable
        self.y = y

    def draw(self):  # Instance Method
        print(f"Point ({self.x}, {self.y})")


print(Point.default_color)
point = Point(1, 2)
point.default_color = "Yellow"
print(point.default_color)
print(Point.default_color)

another = Point(3, 4)
another.draw()
