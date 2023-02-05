def encrypt(line):
    encrypt_line = ""
    for letter in line:
        if 64 < ord(letter) < 91:
            encrypt_line += chr(((ord(letter) - 64 + 13) % 26) + 64)
        elif 96 < ord(letter) < 123:
            encrypt_line += chr(((ord(letter) - 96 + 13) % 26) + 96)
        else:
            encrypt_line += letter
    return encrypt_line


def encrypt_file(file_origin, file_encrypt):
    f = open(file_origin, "r")
    lines = f.readlines()
    f.close()
    txt = ""
    for line in lines:
        txt += encrypt(line)
    f = open(file_encrypt, "w")
    f.write(txt)
    f.close()

encrypt_file("Arch1.txt", "Arch1_encrypt.txt")