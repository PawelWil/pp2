#Napisz skrypt rysujący na ekranie prostokąt
# zbudowany ze znaku jak i wymiarów określonych
# przez użytkownika.


sign = input ("Podaj znak: ")
columns = int(input("Podaj liczbę kolumn: "))
rows = int (input("Podaj liczbę wierszy: " ))

print()  # to jest tylko efekty estetyczny, czyli pusta linia

print((sign * columns + "\n") * rows) # \n daje dodanie nowej linii, czyli złamanie
