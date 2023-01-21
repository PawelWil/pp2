# ZAD.1
# Wyświetl liczby od 1 do 100 z pominięciem liczb podzielnych przez 3

# ROZWIĄZANIE PANA MARCINA:



# MOJE ROZWIĄZANIE:
for i in range (1, 101): #range(2, 101, 1)
    if i % 3 != 0: # to dajemy modulo, na bazie którego wyrzucamy, wszystkie liczby, które są podzielne przez 3, czyli: dajemy % 3(jako modulo podzielności przez 3) + znak różności '!=' co dodatkowo specyfikuje, że nie jest to liczba parzysta
        print(i)