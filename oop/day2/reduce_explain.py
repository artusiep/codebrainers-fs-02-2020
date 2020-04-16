from functools import reduce

temperatury = [10, 13, 14, 15, 14, 10]

acc = 1
for x in temperatury:
    acc = acc * x
print(acc)


def multiply(elem1, elem2):
    return elem1 * elem2


acc_2 = reduce(lambda elem1, elem2: elem1 * elem2, temperatury[2:])
print(acc_2)


# [10, 13, 14, 15, 14, 10] -> 1 Etap
# [130, 14, 15, 14, 10] -> 2 Etap
# [1820, 15, 14, 10] -> 3 Etap
# [27300, 14, 10] -> 4 Etap
# [382200, 10] -> 5 Etap
# [3822000] -> 6 Etap
# 3822000 -> 7 Etap

def a(arg1, arg2):
    # 'r', 'w', 'a'
    with open(arg1, 'a') as f:
        f.write(arg2)
    return (arg1, arg2)

a("plik.txt", "NASZ PLIK")
a("plik.txt", "NASZ PLIK")
a("plik.txt", "NASZ PLIK")
a("plik.txt", "NASZ PLIK")
