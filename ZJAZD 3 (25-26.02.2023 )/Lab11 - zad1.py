# Lab 11 - Zad 1

# Napisz skrypt symulujący grę losową:
# • użytkownik obstawia 6 liczb z 49,
# • program losuje 6 liczb z 49,
# • użytkownik dostaje informacje o ilości trafień.


# SPOSÓB Pana Marcina

import random # ten moduł generuje liczby pseudolosowe

user_numbers=[] # liczby od uzytkownika
random_numbers = []#miejsce do zapisu wylosowynch liczb przez komputer
hit_total = 0 # teraz chcmey mieć całkowitą liczbę trafien

# 1 podpunkt - pobranie liczb od uzytkownika i zapisanie - użytkownik obstawia 6 liczb z 49,
# ma być pobrane 6 liczb
for i in range(6): # pętla która będzie przechoidzła 6 razy - oczywiscie to robi 'for'
    # user_numbers.append(int(input("Podaj liczbę (od 1 do 49): ")))
    user_numbers.append(int(input("Podaj" + str(i+1) + "liczbę (od 1 do 49): "))) # tu poprzez konkatecja ładniej bedzie wyglądać

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




# Mój SPOSÓB
# import random
#
# random_numbers = [] # tu umieszczamy te liczby, w tej liście
#
# for i in range (6):  # teraz iterujemy tyle razy ile razy mamy wylosowac liczb - w tym przypadku 6 - to jest na sztywno 3 losowanie , ale to jest zle, musi bec petla while ze zmienna counter
#     counter = 6
#
# while counter:
#     number = random.randint (0, 49)
#     if  number not in random_numbers:
#         random_numbers.append(number)  # tu nam losuje liczbe ze zbioru od 1 do 10
#         counter -= 1 # counter = counter - 1
# random_numbers.sort() # teraz po losowaniu jeszcze musimy posrtować + sprawdzenie czy jest już w naszym zbiorzez, jesli tak, to musimy losować jeszcze raz
#
#
# print (random_numbers)