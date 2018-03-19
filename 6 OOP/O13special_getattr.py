# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错
# 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性
class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':  # return attribute
            return 99
        if attr == 'age':
            return lambda: 25  # return function is OK !
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值
s = Student()
print(s.name)
print(s.score)
print(s.age())
# AttributeError: 'Student' object has no attribute 'grade'
# print(s.grade)

# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。

# 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None
