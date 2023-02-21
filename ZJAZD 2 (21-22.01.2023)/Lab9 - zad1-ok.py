# LABORATORIUM 9 - ZAD 1

# Wyświetl tylko liczby podzielne przez 3, 5 lub 7, ze zbioru liczb z zakresu
# określonego przez użytkownika.

# Rozwiązanie Pana Marcina:

# I WERSJA - minimalistyczna
# print ("Proszę podać poniżej zakres liczb, w których znajdziemy liczby podzielne przez 3 lub 5 lub 7 ")
# range_from = int(input("Zakres zaczyna się od: "))
# range_to = int(input("zakres kończy się na: "))
#
# print("Liczby podzielne przez 3 lub 5 lub 7, to: ")
# for number in range (range_from, range_to + 1):
#     if number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
#         print(number)

# II WERSJA - full wersja
# print("Podaj zakres liczb")
# range_from = int(input("od: "))
# range_to = int(input("do: "))
#
# print("Liczby z zakresu od", range_from, "do", range_to, "podzielne przez 3 lub 5 lub 7 to: ", end=" ") # zeby wypisać te liczby potrzebujemy end
#
# is_first = True # dodatkowa zmienna
# for number in range (range_from, range_to + 1):
#     if number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
#         if not is_first:
#             print(", ", end="")
#         print(number, end="")
#         is_first = False
# print (".")

# Moje rozwiązanie:
# a = int(input("Podaj liczbę dolną zbioru: "))
# b = int(input("Podaj liczbę górną zbioru: "))

# for i in range(a, b+1):
#     if i % 3 == 0:
#         print("liczby podzielne przez 3, to: ", i)
#     elif i % 5 == 0:
#         print("liczby podzielne przez 5, to: ", i)
#     elif i % 7 == 0:
#         print("liczby podzielne przez 7, to: ", i)
# else:
#     print("te liczby są niepodzielne")

# for i in range(10):
