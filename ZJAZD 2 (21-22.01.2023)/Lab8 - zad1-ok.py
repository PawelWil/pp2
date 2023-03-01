# LABORATORIUM 8 - ZAD 1
# Wyświetl liczby od 1 do 100 z pominięciem liczb podzielnych przez 3

# ROZWIĄZANIE PANA MARCINA:
for i in range (1, 101):
    if i  % 3 != 0: # tu dajemy modulo 3, żeby wyłapać podzielność przez 3  #--> ważna informacja: jakbym dał == to bym wyświetlił wsystkie liczby podzielne przez 3, a nam zależało żeby wyświetlic liczby które sa niepodzielne przez 3, dlatego daliśmy !=
        print(i) # ważne, że musi być wcięcie - bez tego jest błąd!!!!!


# MOJE ROZWIĄZANIE:
# print("Liczby od 1 do 100, niepodzielne przez 3, to: " )
# for i in range (1, 101):
#     if i  % 3 == 0:
#         print(i)


