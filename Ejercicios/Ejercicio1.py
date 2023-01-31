def printN(file, n):
    f = open(file, "r")
    lines = f.readlines()
    for i in range(n):
        print(lines[i], end="")
    f.close()

printN("Arch1.txt", 3)