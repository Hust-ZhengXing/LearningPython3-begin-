# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
# 只有内部可以访问，外部不能访问，所以，把O1模块的Students类改一改


class Students(object):

    def __init__(self, name, score):  # 特殊方法“__init__”前后分别有两个下划线
        self.__name = name  # 类属性-->类私有属性
        self.__score = score

    def print_rank(self):  # 类方法
        if self.__score >= 90:
            rank = 'excellent'
        elif self.__score >= 80:
            rank = 'good'
        elif self.__score >= 60:
            rank = 'passed'
        else:
            rank = 'failed'
        print(self.__name, ',', rank)

tom = Students('Tom Jackson', 85)
lily = Students('Lily James', 62)

tom.print_rank()
lily.print_rank()
# print(tom.__score) # 不能访问
tom.__score = 59  # 不会修改
tom.print_rank()