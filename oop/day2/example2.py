import statistics

temperatures = [10, 12, 14, 15, 10, 9, 5]


def if_greater_then_mean(x):
    if x > statistics.mean(temperatures):
        return True
    else:
        return False


# lambda x: x > statistics.mean(temperatures)
temperatures_under_mean = list(filter(if_greater_then_mean, temperatures))

print(temperatures_under_mean)

