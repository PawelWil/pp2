# Wyświetl tylko liczby podzielne przez 3, 5 lub 7, ze zbioru liczb z zakresu
# określonego przez użytkownika.


print ("Proszę podać poniżej zakres liczb, w których znajdziemy liczby podzielne przez 3 lub 5 lub 7 ")
range_from = int(input("Zakres zaczyna się od: "))
range_to = int(input("zakres kończy się na: "))

print("Liczby podzielne przez 3 lub 5 lub 7, to: ")
for number in range (range_from, range_to + 1):
    if number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        print(number)
