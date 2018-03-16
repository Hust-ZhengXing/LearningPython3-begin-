# 函数递归，反转字符串
# 一定要有无需递归的基例，否则会无限递归导致内存崩溃


def reverse(s):
    if s == "":
        return s  # 需要有基例，避免无限递归
    else:
        return reverse(s[1:])+s[0]

print(reverse("Hello"))
