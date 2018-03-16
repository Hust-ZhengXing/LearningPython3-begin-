# 模拟编写自己的map函数


def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res

# def mymap(func, *seqs):
#     return [func(*args) for args in zip(*seqs)]


def main():
    print(mymap(abs, [-7, 5, -8, 6, 3]))
    print(mymap(pow, [1, 2, 3], [4, 5, 3]))


if __name__ == '__main__':
    main()
