# 类似于def， import和from语句是可执行的的语句，而不是编译期间的声明
# 它们可以嵌套在if语句中，出现在def语句体中，到python执行时才会解析


def importf(x):
    if x > 0:
        from m1fact import fact
        l1 = list(map(fact, [2, 3, 4, 5, 6]))
        print(l1)
    else:
        import m3str1
        print(m3str1.str1)


def aver(x,y):
    return (x+y)/2


def main(x, y):
    ave = aver(x**2,y-14)
    importf(ave)

if __name__ == '__main__':
    print(main(2,2))
    print(main(2, 22))