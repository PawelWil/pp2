# # LAB 18 - zad 1
#
# 1. Wyświetl polski alfabet (tylko małe litery, także litery ze znakami diakrytycznymi)
# wraz z punktami kodowymi dla każdej litery.


polish_letters = ("ą", "ę", "ó", "ź", "ż")
alphabet = "" + str(polish_letters)
for i in range (ord("a"), ord("z") + 1 ):
    alphabet += chr(i)

print(alphabet)