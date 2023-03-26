# # LAB 18 - zad 1
#
# 1. Wyświetl polski alfabet (tylko małe litery, także litery ze znakami diakrytycznymi = polskie ogonki)
# wraz z punktami kodowymi dla każdej litery.

alphabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"

for c in alphabet:
    print(c, ord(c))
