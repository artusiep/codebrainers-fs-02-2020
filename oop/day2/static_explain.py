class Point:
    # Statatyczne atrybuty
    _counter = 0

    def __init__(self, x, y):
        Point._counter += 1
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punkt: {self.x}, {self.y} z {self._counter}"

    def __del__(self):
        Point._counter -= 1

    @staticmethod
    def description():
        print("This is 2d point. Future work to be done")

    @staticmethod
    def increase_counter():
        Point._counter += 1

first_point = Point(10, 20)

print(first_point)

second_point = Point(10, 30)
third_point = Point(10, 30)


print(Point._counter)
print(first_point._counter)

del first_point
print(Point._counter)

Point.increase_counter()

print(Point._counter)

Point.description()
second_point.description()
