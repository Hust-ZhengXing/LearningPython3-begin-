# 文件操作 文件的读写与遍历

f = open("test.txt", "w")
f.write(" hello\n Python\n hello\n world\n")
f.close()
file = open('test.txt', "r+")
# for line in file.readlines():  # 当读入文件较大，占用很大内存
for line in file:  # 文件遍历
    print(line)
file.close()

