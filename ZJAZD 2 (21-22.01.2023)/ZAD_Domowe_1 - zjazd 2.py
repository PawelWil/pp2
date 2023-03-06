# 1. Napisz program sumujący pobrane liczby od użytkownika wg wytycznych:
# • program powinien pobierać od użytkownika liczby całkowite (+),
# • niepodanie liczby powinno zakończyć wprowadzanie danych (???),
# • program powinien podać sumę liczb parzystych oraz sumę liczb nieparzystych (+).

while True:

    numbers = []
    while True:
        try:
            num = input("Podaj liczbę całkowitą: ")
            numbers.append(int(num))
        except ValueError:
            print("Nie podano liczby całkowitej. Wykonywanie obliczeń:")
            break

    print("Wpisano liczby:", numbers)
    even = []
    odd = []
    for i in numbers:
        if (i % 2) == 0:
            even.append(i)
        else:
            odd.append(i)
    print("Liczby parzyste:", even)
    print("Liczby nieparzyste:", odd)
    evenSum = 0
    oddSum = 0
    for j in even:
        evenSum += j
    for k in odd:
        oddSum += k

    print("Suma liczb parzystych:", evenSum)
    print("Suma liczb nieparzystych:", oddSum)
    print("KONIEC Pętli, bo nie podałeś liczby..sorry")
    break
