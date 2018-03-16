class Students(object):

    def __init__(self, name, score):  # 特殊方法“__init__”前后分别有两个下划线
        self.__name = name  # 类属性-->类私有属性
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    # 又要允许外部代码修改score怎么办？可以再给Students类增加set_score方法
    # 方法中，可以对参数做检查，避免传入无效的参数
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

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

# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Students__name来访问__name变量
# 但是强烈建议不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名
print(tom._Students__name)