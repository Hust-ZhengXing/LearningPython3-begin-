# 排序函数sorted

from operator import itemgetter

# Python内置的sorted()函数可以对list进行排序
print(sorted([36, 5, -12, 9, -21]))

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
print(sorted([36, 5, -12, 9, -21], key=abs))

# 按ASCII值排序字符串
L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))
print(sorted(L, key=str.lower, reverse=True))

# 按名称或分数对学生进行排序
students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))

# 用sorted函数分别按键和值对字典元素排序

dict1 = {'Bob': 75, 'Adam': 92, 'Bart': 66, 'Lisa': 88}
l1 = sorted(dict1.keys())
l2 = sorted(dict1.values())
l3 = sorted(dict1.items(), key=lambda item: item[0])
l4 = sorted(dict1.items(), key=lambda item: item[1])

print(l1)
print(l2)
print(l3)
print(l4)
