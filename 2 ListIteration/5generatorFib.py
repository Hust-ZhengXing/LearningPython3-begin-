# 生成器
# 在Python中，一边循环一边计算的机制，称为生成器：generator。

L = [x * x for x in range(5)]  # List
print(L)

g = (x * x for x in range(5))  # generator
print(g)
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))  # 没有更多的元素时，抛出StopIteration的错误。
# 正确方法 for循环 generator也是可迭代对象
print('for loop')
g1 = (x * x for x in range(5))
for n in g1:
    print(n)

# function


def fib(max1):
    n, a, b = 0, 0, 1
    while n < max1:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib(8))

# generator


def fib1(maxNum):   # generator
    n, a, b = 0, 0, 1
    while n < maxNum:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
# generator和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
# 再次执行时从上次返回的yield语句处继续执行。
print(fib1(8))

for m in fib1(8):
    print(m)


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o = odd()
print(next(o))
print(next(o))
print(next(o))



def tri(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        l = [1]*n
        for i in range(1, n-1):
            l[i] = tri(n-1)[i-1]+tri(n-1)[i]
        return l

r = map(tri, [1, 2, 3, 4, 5, 6, 7, 8])  # map generator
for i in r:
    print(i)