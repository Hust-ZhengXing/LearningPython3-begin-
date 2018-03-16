# 筛选法判断回数

def reverse(s):  # 字符串反转
    if s == "":
        return s
    else:
        return reverse(s[1:])+s[0]


def is_palindrome(n):  # 判断是否为回数
    str1 = str(n)  # num2str
    str2 = reverse(str1)
    if str1 == str2:  # compare
        return n

l = list(filter(is_palindrome, range(10, 100000)))  # 过滤器过滤
print(l)
