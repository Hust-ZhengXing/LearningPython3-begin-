#  函数递归，实现阶乘的计算


def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
num = eval(input("Please input a number:(num)"))
print("The fact of", num, "is", fact(num))
