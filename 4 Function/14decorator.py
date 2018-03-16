# 装饰器

# 由于函数也是一个对象，而且函数对象也可以被赋值给变量，所以通过变量也能调用该函数


def now():
    print('2018-3-14 白色情人节')
f = now
print(f())

print(now.__name__)
print(f.__name__)

# 假设要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# decorator就是一个返回函数的高阶函数
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2018-3-14 白色情人节')
now()


def logger(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@logger('白色情人节')
def today():
    print('2018-3-14')

today()
print(today.__name__)
