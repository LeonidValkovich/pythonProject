def func1(a, b):
    def inner_func(x):
        return x * x * x

    return inner_func(a) + inner_func(b)


print(func1(4, 5))


def sum(a, b): return a * b


print(sum(1, 5))
