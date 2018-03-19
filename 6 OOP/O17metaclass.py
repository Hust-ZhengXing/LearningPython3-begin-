# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。

#  metaclass，直译为元类，简单的解释就是：
#
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
#
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
#
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
#
# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
#
# metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。
# metaclass是创建类，所以必须从`type`类型派生：


class ListMetaclass(type):  # 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass
    # 这个metaclass可以给我们自定义的MyList增加一个add方法
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# # 当我们传入关键字参数metaclass时，魔术就生效了，
# 它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
# 在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

# __new__()方法接收到的参数依次是：
#
#     当前准备创建的类的对象；
#
#     类的名字；
#
#     类继承的父类集合；
#
#     类的方法集合。


# 指示使用ListMetaclass来定制类，动态修改
class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
L.add(2)
L.add(3)
L.add('END')
print(L)

# 普通的list没有add方法
L2 = list()
# AttributeError: 'list' object has no attribute 'add'
# L2.add(1)

