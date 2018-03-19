# 形如__xxx__的变量或者函数名在Python中是有特殊用途


class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__  #直接显示变量调用__repr__， __str__返回用户看到的字符串

print(Student('Michael'))