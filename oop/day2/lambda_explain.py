def sum_digits(a, b):
    return a + b

print(sum_digits(5,10))

sum_digits_lambda = lambda a, b: a+b

print(sum_digits_lambda(5,10))

#      arguments: return value
lambda _, _1, _2:  _ + _2 + _1