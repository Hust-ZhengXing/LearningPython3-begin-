# An Instance of PYTHON OOP

import shelve


# 步骤1： 创建实例
class Person:
    def __init__(self, name, job=None, pay=0):  # 构造函数，将本地变量赋给实例属性，job和pay是可选参数，pay默认值为0
        # Python 的语法规则：一个函数定义中， 在第一个拥有默认值的参数之后的任何参数， 都必须拥有默认值
        self.name = name
        self.job = job
        self.pay = pay

    # 步骤2： 添加行为方法
    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= 1 + percent

    def __str__(self):  # 步骤3 内置属性重载
        return '[Person:%s,%s]' % (self.name, self.pay)


# 步骤4 通过子类定制行为
class Manager(Person):
    # 定制经理的涨工资方式，
    # 扩展方法：不好的方式，不利于维护
    # def giveRaise(self, percent,bonus):
    #     self.pay *= 1 + percent + bonus
    #
    def __init__(self, name, pay, age):  # 步骤5 定制构造函数
        Person.__init__(self, name, 'mgr', pay)
        self.age = age

    # 扩展方法，好的方式
    def giveRaise(self, percent, bonus=0.10):  # 默认10%的津贴
        Person.giveRaise(self, percent + bonus)

    def __str__(self):  # 子类属性重载
        return '[Manager:%s,%s,%s]' % (self.name, self.pay, self.age)


# 步骤6 类的其它组合方式：嵌入Embedding-based, 聚合其它对象Aggregate embedded objects into a composite
class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showALL(self):
        print('*****Show All Members*****')
        for person in self.members:
            print(person)


if __name__ == '__main__':  # self-test code, 在类导入时就不会运行

    def testManager():
        print('***********testManager*************')

        zx = Person('Xing Zheng')
        qj = Person('Jun Qu', job='Programmer', pay=300000)

        # print(zx.name, zx.pay)
        # print(qj.job, qj.pay)
        print(qj)
        # print(zx.name.split()[-1])
        # qj.pay *= 1.20  # 可修改属性
        # print(qj.pay)
        print(zx.lastName(), qj.lastName())
        qj.giveRaise(0.2)
        print(qj.pay)
        print(qj)

        defu = Manager('Defu Shi', 350000, 23)
        defu.giveRaise(0.10)
        print(defu)

        # 多态的作用
        print('******All Three******')
        for obj in (zx, qj, defu):  # 自动为每个对象选择正确的涨薪方法
            obj.giveRaise(0.2)
            print(obj)


    def testDepartment():
        # Test the class Department
        print('***********testDepartment*************')

        bob = Person('Bob Smith')
        sue = Person('Sue Jones', 'dev', 200000)
        tom = Manager('Tom Jackson', 320000, 25)

        ali = Department(bob, sue)
        ali.addMember(tom)
        ali.giveRaises(0.20)
        ali.showALL()


    # 步骤7 使用内省工具
    def usingBuiltinTools():
        print('***********usingBuiltinTools*************')

        lily = Person('Lily Green')

        print(lily)
        print(lily.__class__)
        print(lily.__class__.__name__)
        print(list(lily.__dict__.items()))
        print(dir(lily))

        for key in lily.__dict__:
            # print(key, "=>", bob.__dict__[key])
            print(key, "=>", getattr(lily, key))


    # 步骤8 把对象存储到数据库中
    # 对象持久化通过三个标准的库模块来实现：pickle 任意Python对象和字符串之间的序列化
    # dbm 实现一个可通过键访问的文件系统，以存储字符串  shelve 使用另两个模块按照键把python对象存储到一个文件中
    def updateDb():
        db = shelve.open('persondb')

        bob = Person('Bob Smith')
        sue = Person('Sue Jones', 'dev', 200000)
        tom = Manager('Tom Jackson', 320000, 25)

        for obj in (bob, sue, tom):
            db[obj.name] = obj

        db.close()


    def loadDb():
        print('***********load database*************')
        database = shelve.open('persondb')
        # print(len(db))
        # print(list(db.keys()))
        # bob1 = db['Bob Smith']
        # print(bob1.lastName)
        for key in sorted(database):
            print(key, "\t=>", database[key])


    testManager()
    testDepartment()
    usingBuiltinTools()
    updateDb()
    loadDb()
