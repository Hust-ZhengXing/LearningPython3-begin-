# Fact
print('This module is for counting fact')
s = 'Huazhong University of Science and Technology'
num = 1037


def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)