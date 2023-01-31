def copyF(file):
    f = open(file, "r")
    txt = f.read()
    f_name = f.name
    f.close()

    f_name = f_name[:-4] + "_copy.txt"

    f = open(f_name, "w+")
    f.write(txt)
    f.seek(0)
    print(f.read())
    f.close()

copyF("Arch1.txt")