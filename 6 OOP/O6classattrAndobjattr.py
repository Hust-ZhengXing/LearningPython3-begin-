class Students(object):
    name = 'student'  # 直接定义属性，类属性s


# 类属性与实例属性
s = Students()  # 创建实例s

print(s.name)  # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性

print(Students.name)  # 打印类的name属性

s.name = 'Michael'  # 给实例绑定name属性

print(s.name)  # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性