import fact, str1  # 模块会在首次导入时执行


def main():
    l1 = list(map(fact.fact, [2, 3, 4, 5, 6]))
    print(l1)
    print(fact.s.find('ci'))
    print(str1.str1)


if __name__ == '__main__':
    main()

