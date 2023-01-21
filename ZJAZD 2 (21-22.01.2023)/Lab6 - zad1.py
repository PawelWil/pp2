#Napisz skrypt rysujący na ekranie prostokąt
# zbudowany ze znaku jak i wymiarów określonych
# przez użytkownika, np..:

#WERSJA PANA MARCINA:
# nazwa skryptu: drwa_rectangle
char = input ("Podaj znak: ")
columns = int(input("Podaj liczbę kolumn: "))
rows = int (input("Podaj liczbę wierszy: " ))

print()  # to jest tylko efekty estetyczny, czyli pusta linia

print((char * columns + "\n") * rows) # \n daje dodanie nowej linii, czyli złamanie





# MOJA WERSJA
# a = input("podaj znak: ") # tu mamy string bo to znak
# b = int(input ("podaj liczbe kolumn: ")) # tu musimy podać liczbę, więc string musimy zintigerować
# c = int(input ("podaj liczbe wierszy: ")) # tu musimy podać liczbę, więc string musimy zintigerować

# print ((a * c) * 3 )
# print ((a + " " * b + a + "\n") * b, end="")
# print ((a * c) * 3)
# print (str(podaj_znak + str(podaj_liczbe_kolumn) ))


# print ("Jak masz na imię?")
# name = input () #

# print ("+" + 10 * "_" + "+") # linia górna_pozioma
# print (("|" + " " * 10 + "|" + "\n") * 5, end="" ) # linie boczne_pionowe
# print ("+" + 10 * "_" + "+") # linia dolna_pozioma