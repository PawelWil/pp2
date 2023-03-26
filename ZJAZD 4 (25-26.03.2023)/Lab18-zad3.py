# LAB 18 - zad 3

#  Rozszyfruj poniższą wiadomość wiedząc, że została ona zaszyfrowana szyfrem
# cezara z parametrem przesunięcia równym 3.
# VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ

delta = 3

# print(ord("A")) # to nie jest potrzebne - tylko testowo, pokazuje zakres
# print(ord("Z")) # to nie jest potrzebne - tylko testowo, pokazuje zakres

# for i in range(ord("A"), ord("Z") + 1):
#     print(chr(i), end="")

print()

for i in range(ord("A") + delta, ord("Z") + 1 + delta):
    if i > ord("Z"):
        i -= ord("Z") - ord("A") + 1
    # print(chr(i), end="")


# funkcja odkodowania szyfr cezara
def decode_letter(letter, delta): # rozkodowanie 1 litery
    if letter < "A" or letter > "Z":
        return letter
    n = ord(letter) - delta
    if n < ord("A"):
        n += ord("Z") - ord("A") + 1
    return  chr(n)

def decode(string, delta):
    decoded = ""
    for char in string:
        decoded += decode_letter(char, delta)
    return decoded

print(decode("VCBIU", delta))

# print()
# print(decode_letter("J", delta) == "G")
# print(decode_letter("J", delta))

