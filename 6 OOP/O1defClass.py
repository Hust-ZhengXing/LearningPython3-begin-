# define a class

# class后面紧接着是类名，即Student，类名通常是大写开头的单词，
# 紧接着是(object)，表示该类是从哪个类继承下来的
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。


class Students(object):

    def __init__(self, name, score):  # 特殊方法“__init__”前后分别有两个下划线
        # _init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
        # 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
        # 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
        self.name = name  # 类属性
        self.score = score

    def print_rank(self):  # 类方法
        if self.score >= 90:
            rank = 'excellent'
        elif self.score >= 80:
            rank = 'good'
        elif self.score >= 60:
            rank = 'passed'
        else:
            rank = 'failed'
        print(self.name, ',', rank)






# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
tom = Students('Tom Jackson', 85)
lily = Students('Lily James', 62)
# 面向对象编程的一个重要特点就是数据封装。在Students类中，每个实例就拥有各自的name和score这些数据。可以通过函数来访问这些数据
print(tom.name, ',', tom.score)
# 但是，既然Students实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，
# 可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了
# 这些封装数据的函数是和Students类本身是关联起来的，称之为类的方法
# 这样一来，我们从外部看Student类，就只需要知道，创建实例需要给出name和score，
# 而如何打印，都是在Student类的内部定义的，这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节
tom.print_rank()
lily.print_rank()

# 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
#  方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
#  通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
#  和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
tom.age = 15
print(tom.age)
# print(lily.age)  # lily 没有年龄属性会报错

# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，
# 这样，就隐藏了内部的复杂逻辑。但是，从前面Students类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性
tom.score = 58
tom.print_rank()
