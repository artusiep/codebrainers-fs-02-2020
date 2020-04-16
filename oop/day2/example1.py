# print(list(range(0,30)))

squares = []

for x in range(0, 30):
    if x % 2 == 0:
        squares.append(x ** 2)

print(squares)
print(len(squares))

#### List Comprehension

squares2 = [
    x ** 2
        for x in range(0, 30)
        if x % 2 == 0
]
print(squares2)

squares2 = (
    x ** 2
        for x in range(0, 30)
        if x % 2 == 0
)
print(squares2)

