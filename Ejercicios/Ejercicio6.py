def load_data(file):
    dic = {}
    f = open(file, "r")
    txt = f.read()
    f.close()
    values = txt.split(" / ")
    for value in values:
        dict_list = value.split(": ")
        dic.update({dict_list[0]: dict_list[1]})
    return dic

def save_data(dic, file):
    txt = ""
    primero = True
    for key in dic:
        if primero:
            primero = False
            txt += key + ": " + dic[key]
        else:
            txt += " / " + key + ": " + dic[key]
    f = open(file, "w")
    f.write(txt)
    f.close()


d = {"Josuke Higashika": "Soft & Wet", "Yoshikage": "KilleQueen", "Yasuho": "Paisley Park"}
save_data(d, "dict_file.txt")

print(load_data("dict_file.txt"))