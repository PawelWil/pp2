# Lab 11 - Zad 1

# Napisz skrypt symulujący grę losową:
# • użytkownik obstawia 6 liczb z 49,
# • program losuje 6 liczb z 49,
# • użytkownik dostaje informacje o ilości trafień.


import random # ten moduł generuje liczby pseudolosowe

user_numbers=[] # liczby od uzytkownika
random_numbers = []#miejsce do zapisu wylosowynch liczb przez komputer
hit_total = 0 # teraz chcmey mieć całkowitą liczbę trafien

# 1 podpunkt - pobranie liczb od uzytkownika i zapisanie - użytkownik obstawia 6 liczb z 49,
# ma być pobrane 6 liczb
for i in range(6): # pętla która będzie przechoidzła 6 razy - oczywiscie to robi 'for'
    # user_numbers.append(int(input("Podaj liczbę (od 1 do 49): ")))
    user_numbers.append(int(input("Podaj " + str(i+1) + " liczbę (od 1 do 49): "))) # tu poprzez konkatenacja ładniej bedzie wyglądać


# 2 podpunkt: program losuje 6 liczb z 49,

    random_numbers = random.sample(range(1,50), 6) # ta funkcja sample wylosuje daną liczbę ze zbioru 1,50 + 6 liczb


# 3 podpunkt: użytkownik dostaje informacje o ilości trafień.

for number in user_numbers:
    if number in random_numbers:
        hit_total +=1

# sortowanie:
user_numbers.sort()
random_numbers.sort()

print("Wylosowane liczby:", random_numbers)
print("Obstawione liczby użytkowników,", user_numbers)
print("Trafiono:", hit_total, "liczb")

