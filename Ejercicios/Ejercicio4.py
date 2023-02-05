def count(file):
    # NO FUNCIONA BIEN
    f = open(file, "r")
    txt = f.read()
    num_chr = len(txt)
    f.seek(0)
    lines = f.readlines()
    f.close()
    num_lines = len(lines)
    num_wrd = 0
    for line in lines:
        num_wrd += len(line.split(" "))
    print("Numero de lineas:", num_lines)
    print("Numero de caracteres:", num_chr)
    print("Numero de palabras:", num_wrd)

count("Arch1.txt")