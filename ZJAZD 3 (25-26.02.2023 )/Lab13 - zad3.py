# # Lab 13 - Zad.3
# Napisz skrypt symulujący uproszczone działanie gry losowej "jednoręki bandyta",
# w tym celu:
# • za każdym "pociągnięciem" losuj 3 litery ze zbioru od A do E,
# • kontynuuj losowania do momentu wystąpienia 3 takich samych liter np. A A A,
# • wyświetl informację o wynikach poszczególnych losowań oraz numer próby,
# • przemyśl jak dużo zmian trzeba wprowadzić w skrypcie, aby losować z większego zbioru liter, a także
# większą liczbę liter.


# 1 krok - zaczynamy od losowania -  za każdym "pociągnięciem" losuj 3 litery ze zbioru od A do E,

import random

# print(ord("A")) # funkcja ord zwraca nam numerek który jest reprezentowany przez dany znak

# print(chr(65)) # chr ta funckja przezchdzi z liczby na Ascii, czyli z 65 na "A" w kodzie ascii

# def draw_letter():# losujemy jedną literkę
#     return chr(random.randint(ord("A"), ord("E"))) # zwroc litere, w zakresie od "A" do "E"
#
# def draw_row():
#     return [draw_letter() for i in range (3)]
#
# # 2 krok - kontynuuj losowania do momentu wystąpienia 3 takich samych liter np. A A A,
# def check(row):
#      if row[0] == row[1] and row[1] == row[2]:
#          return True
#      else:
#          return False
#
# # print (check(["A", "B", "C"])) # False
# #
# # print (check(["A", "A", "A"])) # True
#
#
# # krok 3 - # • wyświetl informację o wynikach poszczególnych losowań oraz numer próby,
# counter = 1
# while True:
#     row = draw_row()
#     print(row, counter)
#     if check(row):
#         break
#     counter += 1


# krok 4 - przemyśl jak dużo zmian trzeba wprowadzić w skrypcie, aby losować z większego zbioru liter, a także
# # większą liczbę liter.

import random

FIRST_SYMBOL = "A"
LAST_SYMBOL = "H"
NUMBER_OF_LETTERS = 5

# print(ord("A")) # funkcja ord zwraca nam numerek który jest reprezentowany przez dany znak

# print(chr(65)) # chr ta funckja przezchdzi z liczby na Ascii, czyli z 65 na "A" w kodzie ascii

def draw_letter():# losujemy jedną literkę
    return chr(random.randint(ord(FIRST_SYMBOL), ord(LAST_SYMBOL))) # zwroc litere, w zakresie od "A" do "H" - tu zwikeszamy większy zbior od A do H, a nie jak było od A do E

def draw_row():
    return [draw_letter() for i in range (NUMBER_OF_LETTERS)]

# 2 krok - kontynuuj losowania do momentu wystąpienia 3 takich samych liter np. A A A,
def check(row):
    first_element = row[0]
    for element in row:
        if element != first_element:
            return False
    return True



# print (check(["A", "B", "C"])) # False
#
# print (check(["A", "A", "A"])) # True


# krok 3 - # • wyświetl informację o wynikach poszczególnych losowań oraz numer próby,
counter = 1
while True:
    row = draw_row()
    print(row, counter)
    if check(row):
        break
    counter += 1