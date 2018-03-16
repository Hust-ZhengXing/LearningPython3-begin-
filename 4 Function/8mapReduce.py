# map与reduce 方法在函数中的使用
# map 同时将函数作用在列表的每一个元素上，输出结果列表
# reduce把一个函数作用在一个序列这个函数必须接收两个参数
# reduce把结果继续和序列的下一个元素做累积计算

from functools import reduce


def add(x, y):
    return x + y

print(reduce(add, [1, 3, 5, 7, 9]))
print()


def fn(x, y):
    return 10*x+y

print(reduce(fn, [1, 3, 5, 7, 9]))
print()


def f(x):
    return x*x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(r))
print()
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
print()

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
print()

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
print()





