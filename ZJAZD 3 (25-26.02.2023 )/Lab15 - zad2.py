# # LAB 15 - ZAD 2
#
# Napisz program pobierający od użytkownika 3 liczby zmiennoprzecinkowe = FLOAT NUMBERS
# Uwzględnij możliwość pomyłki użytkownika.

numbers = [] # w niej zapiszany pozyskane liczby
counter = 1

while True:
    if counter > 3:
        break

    try:
        number = float(input("Podaj " + str(counter) + " liczbę zmiennoprzecinkową: "))
        numbers.append(number)# dodajemy ją do pustej listy powyżej za pomocą metody append
        counter += 1
    except:
        print("Podana wartość jest niepoprawna, proszę spróbuj ponownie")
print(numbers)
