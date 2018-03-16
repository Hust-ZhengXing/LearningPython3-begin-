# 匿名函数
# 在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便

l1 = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(l1)
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

f = lambda x: x * x
print(f)
print(f(51))
# 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数


def build(x, y):  # 也可以把匿名函数作为返回值返回
    return lambda: x * x + y * y
f1 = build(3, 4)
print(f1)
print(f1())


l = list(range(1, 20))
print(list(filter(lambda x: x % 2 == 0, l)))

from functools import reduce
print(reduce(lambda x, y: x + y, l))
