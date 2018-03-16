# 函数实例：输出杨辉三角某行的各个元素

def tri(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        l = [1]*n
        for i in range(1, n-1):
            l[i] = tri(n-1)[i-1]+tri(n-1)[i]
        return l

r = map(tri, [1, 2, 3, 4, 5, 6, 7, 8])
print(list(r))
