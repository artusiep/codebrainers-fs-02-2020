x = list(range(0, 31))


def make_square(elem):
    return elem ** 2


x_squared = list(map(lambda elem: elem ** 2, x))
print(x_squared)

x_squared2 = list(map(make_square, x))
print(x_squared2)
