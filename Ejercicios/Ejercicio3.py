def separador(file, sep):
    f = open(file, "r")
    txt = f.read()
    f.close()
    lista = txt.split(sep)
    for i in lista:
        print(i)


separador("Arch2.txt", ",")