# ZAD 1
# Napisz skrypt sprawdzający czy pierwiastek kwadratowy z liczby całkowitej
# pobranej od użytkownika jest także liczbą całkowitą.


# Rozwiązanie Pana Marcina

# I sposób:
number  = int(input("Podaj liczbę: "))

if (number ** .5) % 1 == 0: # jesli modulo 1 zwroci nam zero to na pewno jest liczba całkowita
    str1 = "Tak"
    str2 = ""
else:
    str1 = "nie"
    str2 = "nie"

print (str1 + ", pierwiastek kwadratowy z liczby " + str(number) + " " + str2 + " jest liczbą calkowitą ")



#II sposób:
number  = int(input("Podaj liczbę: "))

if (number ** .5) is_integer: # jesli modulo 1 zwroci nam zero to na pewno jest liczba całkowita
    str1 = "Tak"
    str2 = ""
else:
    str1 = "nie"
    str2 = "nie"

print (str1 + ", pierwiastek kwadratowy z liczby " + str(number) + " " + str2 + " jest liczbą calkowitą ")

# MOJE ROZWIĄZANIE:
# number = int(input("Podaj liczbę: "))

# if number ** .5 == 0:
#     print ("Pierwiastek kwadratowy z liczby 'number' jest liczbą calkowitą:" )
# else:
#     print("nie jest liczbą całkowitą")


# print(3%2 ==0)
# if number > 0:
#     print("Liczba większa od zera")
# elif number < 0: # czy naumber nie jest czasami mniejsze od zera. ELifów można stosować wiele
#     print("Liczba mniejsza od zera")
# else:
#     print("Liczba równa zero")