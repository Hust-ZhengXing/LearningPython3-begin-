# 偏函数
# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
# 返回一个新的函数，调用这个新函数会更简单
import functools
print(int('2018'))
print(int('2017', base=8))
print(int('2018', 16))

int2 = functools.partial(int, base=2)
int8 = functools.partial(int, base=8)
print(int2('1000000'))
print(int8('1000000'))


def add(x, y):
    return x + y
add10 = functools.partial(add, 10)
print(add10(12))
