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



# ------------------------------------------------------------------------------------
# LABORATORIUM 8 - ZAD 1
# Wyświetl liczby od 1 do 100 z pominięciem liczb podzielnych przez 3

# ROZWIĄZANIE PANA MARCINA:
for i in range (1, 101):
    if i  % 3 != 0: # tu dajemy modulo 3, żeby wyłapać podzielność przez 3  #--> ważna informacja: jakbym dał == to bym wyświetlił wsystkie liczby podzielne przez 3, a nam zależało żeby wyświetlic liczby które sa niepodzielne przez 3, dlatego daliśmy !=
        print(i) # ważne, że musi być wcięcie - bez tego jest błąd!!!!!


# MOJE ROZWIĄZANIE:
print("Liczby od 1 do 100, niepodzielne przez 3, to: " )
for i in range (1, 101):
    if i  % 3 != 0:
        print(i)



# ------------------------------------------------------------------------------------
# LABORATORIUM 8 - ZAD 2
# Napisz skrypt wyświetlający na ekranie macierz. Rozmiar macierzy oraz
# znak z jakiej będzie zbudowana powinien określić użytkownik

# ROZWIĄZANIE PANA MARCINA:

number = int(input("Podaj rozmiar: "))
char = input ("Podaj znak:") # to jest zmienna o nazwie 'czar'

# teraz potrzebujemy mechanimz do wygenerowania macierzy
for i in range(number):
    for j in range(number): # zmieniam nazwę zmiennej iteracyjenj
        print(char, end=" ")
    print()




# ------------------------------------------------------------------------------------
# LABORATORIUM 8 - ZAD 3
# Załóżmy, że na pierwsze pole szachownicy kładziemy 1 ziarno zboża, na
# drugie 2 ziarna, na trzecie 4 ziarna i na każde następne pole dwa razy
# więcej ziaren niż na pole poprzednie. Napisz program, który zasymuluje
# taką sytuację i zliczy sumę wszystkich ziaren na szachownicy.

# ROZWIĄZANIE PANA MARCINA:

# Szachownica ma 64 pola
 # tu bedziemy milei od 0 do 63, ale będą 64 iteracje, czyli przeszło 64 razy, tyle ile jest wymagane
 #    r = 2 ** i # ilość ziarenek, które musimy kłaść: 1 2 4 8 16 ... 2 ** i (mowa o 2 do potęgi i-tej) --> a to się równa:  0 1 2 3 4
 #    print(r)
 #    if r > 63:
 #        break

sum = 0
for i in range (64):
    sum += 2 ** i
print ("suma wszystkich ziaren zboża na szachownicy: " + str(sum))

#  LICZYMY TERAZ ILE TO BĘDZIE TON
# 1 ziarno to: 0,4 mg (mili to jedna tysięczna grama)
# 1 ziarno to: 0,0004 g
# 1 kg = 1000g
#1t = 1000kg
tons = int
tons = int(sum * 0.0004 / 1000 / 1000) # to jest przeliczenie ziarenek po kolei z mg na g(dzielimy przez 1000), a potem na tony(dzielimy przez 1000)
print(tons)

# TERAZ LICZE ILE LAT POTZREBUJE ŻEBY TE ILOSCI zebrać
# Na bazie powyższego mamy daną, że produkcja pszenicy na świecie to ok. 782 mln ton
# years = int(tons / 782_000_000) # tu mamy 782 miliny ton) - tej linii nie używamy
years = round(tons / 782_000_000, 2) # tu mam z zaokragleniem do dwóch miejsc po przecinku - i to trzeba użyć
# years = round(tons / 782e6, 2) # można też tak tą dużą liczbe przedstawić - ta liczba e opisana w zjezdzie numer 1

print (years)

# Pociąg może transportować 2200t maksymalnie - czyli tu kalkulujemu ile potzeba pociągów, żeby tę ilość pszenicy przetrasportować
trains = round(tons / 2200, 1)
# lub tak
trains = int (tons / 2200) + 1
print(trains)
