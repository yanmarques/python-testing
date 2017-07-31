import string
import re

def crypt(text):
    crypted = []

    words = re.findall('\w+', text)

    for iten in words:
        i = 0
        while i < len(iten):
            index = string.ascii_lowercase.index(iten[i])

            if index == 0:
                crypted.append(string.ascii_lowercase[25])
            else:
                crypted.append(string.ascii_lowercase[index - 1])
            i += 1

    return "".join([e for i, e in enumerate(crypted)])

def decrypt(crypted_text):
    decrypted = []
    i = 0

    while i < len(crypted_text):
        index = string.ascii_lowercase.index(crypted_text[i])

        if index == 25:
            decrypted.append(string.ascii_lowercase[0])
        else:
            decrypted.append(string.ascii_lowercase[index + 1])

        i += 1        

    return "".join([e for i, e in enumerate(decrypted)])
