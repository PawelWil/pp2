# 2. Napisz program, który wylosuje kilka serii liczb całkowitych i wyświetli je
# na ekranie, przy czym:
# • program zapyta użytkownika o zakres minimum oraz maksimum,
# • będzie losował odpowiednie liczby z zakresu podanego przez użytkownika,
# • będzie losował liczbę liczb do wylosowania z zakresu podanego przez użytkownika,
# • będzie losował liczbę serii liczb do wylosowania z zakresu podanego przez
# użytkownika,
# • wyświetli wylosowane serie liczb.


import random
while True:

    min_zakres = int(input("Proszę o podanie zakresu minimum losowania: "))
    max_zakres = int(input("Proszę o podanie zakresu maksimum losowania: "))
    quaNum = random.randint(min_zakres, max_zakres)
    print("Wylosowania ilość losowań wynosi:", quaNum)

    for i in range(quaNum):
        print("Numer losowania " + str(i + 1) + ":")
        lenNum = random.randint(min_zakres, max_zakres)
        print("Wylosowana wielkość zbiorów do losowania:", lenNum)

        numbers = []
        for j in range(lenNum):
            number = random.randint(min_zakres, max_zakres)
            numbers.append(number)

        print("Oto liczby z wybranego zakresu i wylosowanego zbioru:", numbers)
        print()
    break
