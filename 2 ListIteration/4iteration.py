# 迭代方法

# 判断是否迭代对象
from collections import Iterable
print(isinstance('abc', Iterable))  # str是否可迭代

print(isinstance([1,2,3], Iterable))  # list是否可迭代

print(isinstance(123, Iterable))  # 整数是否可迭代


# dict
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k, v in d.items():
    print(k, '-->', v)

# Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 字符串可迭代对象
for ch in 'ABC':
    print(ch)

# 列表可迭代对象
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)