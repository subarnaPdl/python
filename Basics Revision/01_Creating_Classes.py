class Point:
    def draw(self):
        print("draw")


point = Point()
print(point)  # Prints module + class name + address in memory
print(id(point))  # Address in memory
print(type(point))  # Prints type of (point)
point.draw()
# Checks whether (point) is the instance of (Point) or not.
print(isinstance(point, Point))
