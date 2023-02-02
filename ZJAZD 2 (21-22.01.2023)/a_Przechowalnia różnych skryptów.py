# LABORATORIUM_ 6 -  ZAD 2
# Pobierz od użytkownika dwie liczby całkowite i wykonaj na nich operacje:
# dodawania, odejmowania, mnożenia, dzielenia oraz operację modulo.
# Wyświetl rezultat na ekranie

# Wersja Pana Marcina
# a = int(input("Podaj liczbę całkowitą a: "))
# b = int(input("Podaj liczbę całkowitą b: "))
# print () #rozdzielenie estetyczne
#
# print ("a + b = " + str(a + b))
# print ("a - b = " + str(a - b))
# print ("a * b = " + str(a * b))
# print ("a / b = " + str(a / b))
# print ("a % b = " + str(a % b))

# MOJA WERSJA
a = int(input("podaj pierwszą liczbę całkowitą: "))
b = int(input("podaj drugą liczbę całkowitą: "))

print ("Wynik Dodawania, to: ")
print ( a + b)

print ("Wynik Odejmowania, to: ")
print ( a - b)

print ("Wynik Mnożenia, to: ")
print ( a * b)

print ("Wynik Dzielenia, to:")
print ( a / b)

print ("Wynik Operacji Modulo, to: ")
print ( a % b)

# ----------------------------------------------------------------------------------
# LABORATORIUM 6 - ZAD 3

#ZAD 3
# Za pomocą jednej instrukcji wyświetl na ekranie
# następującą figurę

# print ("+" + "-+" * 9) # na razie linia górna - zaczymay od +, potem 9 x mnożymy znak -+
print ("+" + "-+" * 9, "| " * 10, "+" + "+-" *9, sep="\n") #teraz dajemy separator z nową linią, wazna jest też spacja po "|", bo on nam to rozszerza



# ------------------------------------------------------------------------------------
# LABORATORIUM 7 - ZAD 1
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
# number  = int(input("Podaj liczbę: "))
#
# if (number ** .5) is_integer: # jesli modulo 1 zwroci nam zero to na pewno jest liczba całkowita
#     str1 = "Tak"
#     str2 = ""
# else:
#     str1 = "nie"
#     str2 = "nie"
#
# print (str1 + ", pierwiastek kwadratowy z liczby " + str(number) + " " + str2 + " jest liczbą calkowitą ")

# MOJE ROZWIĄZANIE:
# number = int(input("Podaj liczbę: "))
#
# if number ** .5 % 1 == 0:
#     print ("Pierwiastek kwadratowy z liczby 'number' jest liczbą calkowitą" )
# else:
#     print("nie jest liczbą całkowitą")



# ------------------------------------------------------------------------------------
# LABORATORIUM 7 - ZAD 3
# Rozwiązanie Pana MArcina -- !! sprawdzić ten kod jeszcze z filmikiem, bo coś nie do końca działa!!

import random # to jest ściągnięcie biblioteki, która jest mechanizmem do loswaonia liczb (jakichs znaków)

number = random.randint(1, 10)# ona nam losuje liczbę z przedziału jaki jej podamy, czyli w naszym przypadku, z przdziału od 1 do 3
msg = "Zgadnij jaką liczbę mam na myśli (od 1 do 10) :"  # zmienna, która nam poda nam podpowiedź do odgadnięcia prawdziwej liczby, widocznej pod zmienną 'number'
guess = int(input(msg))
if guess == number:
    print("brawo! Dokładnie taką liczbę miałem na myśli!")
else:
    msg = "Masz kolejną szansę :" # to jest druga szansa
    if number % 2 == 0:# to już jest trzecia szansa, czyli podpowiedz, o parzystości
        msg += " twoja liczba jest parzysta: "
    else:
        msg += " twoja liczba jest nieparzysta: "
    guess = int(input(msg))
    if guess == number:
        print("Brawo! Udało się odgadnąć za drugim razem!")
    else:
        msg = "Masz kolejną szansę :"  # to jest druga szansa
        if number > 5:  # to już jest trzecia szansa, czyli podpowiedz, o parzystości
            msg += "moja liczba jest większa"
        else:
            msg += "moja liczba jest mniejsza lub równa"
        msg += " od liczby 5: "
        guess = int(input(msg))
    if guess == number:
        print("Brawo! A jednak do trzech razy sztuka")
    else:
        msg = "Niestety myślałem o liczbie :" + str(number) + "."
        print(msg)