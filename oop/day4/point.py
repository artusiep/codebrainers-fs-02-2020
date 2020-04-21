def increase_counter():
    Point._counter += 1


class Point:
    _counter = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.increase_counter()

    def __del__(self):
        self.decrease_counter()

    def distance(self, other_point):
        x_diff = self.x - other_point.x
        y_diff = self.y - other_point.y
        dist = (x_diff ** 2 + y_diff ** 2) ** 0.5
        return dist

    @staticmethod
    def increase_counter():
        Point._counter += 1

    @classmethod
    def decrease_counter(cls):
        cls._counter -= 1

    def __eq__(self, other_point):
        return self.x == other_point.x and self.y == other_point.y

    def __add__(self, other_point):
        x_add = self.x + other_point.x
        y_add = self.y + other_point.y
        return Point(x_add, y_add)

    def __str__(self):
        return f"Point {self.x, self.y}"

    def __sub__(self, other_point):
        x_sub = self.x - other_point.x
        y_sub = self.y - other_point.y
        return Point(x_sub, y_sub)

    def __getitem__(self, index_point):
        if index_point == 0:
            return self.x
        elif index_point == 1:
            return self.y
        else:
            raise IndexError("Wektor ma tylko dwa elementy - nr 0 i 1")


increase_counter()

Point.increase_counter()
Point.do_sth()
print(Point._counter)