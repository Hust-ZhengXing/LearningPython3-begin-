# 文件操作实例：文件COPY

def main():
    # Input file name
    f1 = input("Enter a source infile:").strip()
    f2 = input("Enter a source outfile:").strip()

    # Open file
    infile = open(f1, 'r')
    outfile = open(f2, 'w')

    # Copy contents
    countLines = countChars = 0
    for line in infile:
        countLines += 1
        countChars += len(line)
        outfile.write(line)
    print(countLines, "lines and", countChars, "chars copied")
    infile.close()
    outfile.close()
main()
