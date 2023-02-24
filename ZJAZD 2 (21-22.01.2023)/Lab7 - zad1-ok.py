# ZAD 1
# Napisz skrypt sprawdzający czy pierwiastek kwadratowy z liczby całkowitej
# pobranej od użytkownika jest także liczbą całkowitą.


# I sposób:
# number  = int(input("Podaj liczbę: "))

# if (number ** .5) % 1 == 0: # jesli modulo 1 zwroci nam zero to na pewno jest liczba całkowita
#     str1 = "Tak"
#     str2 = ""
# else:
#     str1 = "nie"
#     str2 = "nie"

# print (str1 + ", pierwiastek kwadratowy z liczby " + str(number) + " " + str2 + " jest liczbą calkowitą ")



# II sposób:
number = int(input("Podaj liczbę: "))

if (number ** .5) % 1 == 0:
    print ("Pierwiastek kwadratowy z liczby 'number' jest liczbą calkowitą" )
else:
    print("nie jest liczbą całkowitą")

