# Lab 11 - zadanie 2

# Napisz skrypt pobierający od użytkownika serię liczb całkowitych, a
# następnie wyświetl je w kolejności malejącej pozbywając się wcześniej
# duplikatów.



# ile liczb w serii będzie się podawać
# pobieram od uzytkownika liczby + zapisywanie je do list
numbers = [] # nawza listy
numbers_total = int(input("Podaj liczbe elementów zbioru: "))# ile tych liczb uzytkownik bedzie podawał

# teraz uruchamaiamy pętle, jak już mamy info od uzytkowniko ile liczb
for i in range (numbers_total):
    number = int(input("Podaj " + str(i+1) + " element zbioru:")) # teraz pobieramy jakąs liczbę, któą oczywisvie zamieniamy na calkowitą, czyli int
    numbers.append(number) # dopisujemy liczbę, za pomocą append



# teraz mamy je w kolejności malejącej:

numbers.sort(reverse=True) # sortowanie malejące
# POZBYWANIE sie duplikatów - poprzez nową liste bez duplikatów
numbers_without_duplicates = []
# a teraz w  petli for robimy:
for number in numbers:
    if number not in numbers_without_duplicates:
        numbers_without_duplicates.append(number)


print(numbers_without_duplicates)

