# Python内建的filter()函数用于过滤序列。
# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。


def is_odd(n):
    return n % 2 == 1

l1 = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(l1)


def not_empty(s):
    return s and s.strip()

l2 = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(l2)



