# 一个函数就可以接收另一个函数作为参数，这种函数称之为高阶函数。

def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))

print(add([1, 3, 5, 7, 2], [6, 3, 8, 7, 2], max))


def square(x):
    return x*x
print(add(3, 4, square))


def sub(x1, y1, x2, y2, f1):
    return f1(x1, y1) + f1(x2, y2)


def fn(x, y):
    return 10*x+y

print(sub(23, 5, 42, 6, fn))
