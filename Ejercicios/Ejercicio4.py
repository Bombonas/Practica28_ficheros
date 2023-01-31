def count(file):
    # NO FUNCIONA BIEN
    f = open(file, "r")
    txt = f.read()
    num_chr = len(txt)
    num_lines = f.readlines()
    print(num_lines)
    f.close()
    num_wrd = len(txt.split(" "))
    print("Numero de lineas:", num_lines)
    print("Numero de caracteres:", num_chr)
    print("Numero de palabras:", num_wrd)

count("Arch1.txt")