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


# ------------------------------------------------------------------------------------
# LABORATORIUM 9 - ZAD 1

# Wyświetl tylko liczby podzielne przez 3, 5 lub 7, ze zbioru liczb z zakresu
# określonego przez użytkownika.

# Rozwiązanie Pana Marcina:

# I WERSJA - minimalistyczna
print ("Proszę podać poniżej zakres liczb, w których znajdziemy liczby podzielne przez 3 lub 5 lub 7 ")
range_from = int(input("Zakres zaczyna się od: "))
range_to = int(input("zakres kończy się na: "))

print("Liczby podzielne przez 3 lub 5 lub 7, to: ")
for number in range (range_from, range_to + 1):
    if number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        print(number)

# II WERSJA - full wersja
# print("Podaj zakres liczb")
# range_from = int(input("od: "))
# range_to = int(input("do: "))
#
# print("Liczby z zakresu od", range_from, "do", range_to, "podzielne przez 3 lub 5 lub 7 to: ", end=" ") # zeby wypisać te liczby potrzebujemy end
#
# is_first = True # dodatkowa zmienna
# for number in range (range_from, range_to + 1):
#     if number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
#         if not is_first:
#             print(", ", end="")
#         print(number, end="")
#         is_first = False
# print (".")

# Moje rozwiązanie:
# a = int(input("Podaj liczbę dolną zbioru: "))
# b = int(input("Podaj liczbę górną zbioru: "))
#
# for i in range(a, b+1):
#     if i % 3 == 0:
#         print("liczby podzielne przez 3, to: ", i)
#     elif i % 5 == 0:
#         print("liczby podzielne przez 5, to: ", i)
#     elif i % 7 == 0:
#         print("liczby podzielne przez 7, to: ", i)
# else:
#     print("te liczby są niepodzielne")

# for i in range(10):



# ------------------------------------------------------------------------------------
# LABORATORIUM 9 - ZAD 2

# # ZAD. 2
# Udowodnij, że w zbiorze liczb z zakresu 1-100, jest 11 liczb, które są
# parzyste i jednocześnie większe od 90, a gdy są nieparzyste, to
# przynajmniej dzielą się przez 9.


# Rozwiązanie Pana Marcina:

# zawsze powinnismy to podzielić na mniejsze rowziązania, a potem dopiero to łączyć - bo czasami za duzo na raz tego jest!

counter = 0
for i in range (1, 101):# potrzebujemy liczby od 1 do 100, wiec robimy pętle for
    if i % 2 == 0 and i > 90 or ( i % 2 != 0 and i % 9 == 0): # to jest pierwszy warunek=sprawdzamy parzystsc i wieksze od 90 (i % 2 == 0 and i > 90), a teraz drugi warunek:( i % 2 != 0 and i % 9 == 0)
        counter += 1  # teraz checmy te zmienne zliczyć, wiec dajemy zmienną counter


print("Tak to prawda, w zbiorze liczb z zakresu 1-100, jest " + str(counter) + " liczb, które są parzyste i jednocześnie większe od 90, a gdy są nieparzyste, to przynajmniej dzielą się przez 9.  "  + ".")



# ------------------------------------------------------------------------------------
# LABORATORIUM 9 - ZAD 3

# # ZAD. 3
# Napisz program wyznaczający wartość n-tego bitu dla dowolnej liczby
# całkowitej. Bity liczymy od 0, od najmniej znaczącego bitu.

#tu mamy sytuacje, że podajemy liczbę całkowitą, która ma swoje rozłożenie bitowe, np. dla liczby 1, mamy 0001, czyli jeśli podam liczbę 1 + bit 0 to wtedy dostanę , że bit na pozycji 0 (tu mamy 1) dla liczby 1(tu mamy bit na pozycji 0) i teraz 1 z 1 na tej samej poycji się nakładają, wieć mamy 1, WYNOSI 1. Zaś gdybym podał na innej pozycji, gdzie dla jedynki było nie jeden, a zeero, to wtedy byłoby 0, bo 1 i 0 daje zero.

number = int (input("Podaj liczbę: "))  #podanie liczby całkowitej, dla której jest wyznaczana wartość n-tego bitu, podanego poniżej
n = int(input("Podaj nr bitu: ")) # numery bitów

# 01001 - przykładowa liczba - i tu się posilkujemy maską
# 00001 - to jest moja  maska
# &      -->za pomocą AND(koniunkcji)=& wyłuskamy te bity
# 00001 - to jest wynik, który

mask = 1 << n #potrzebujemy maskę wiec dodajemy taką zmienną
result = number & mask

bit = int(bool(result)) # wyłuskanie bity, czy to jest jeden, czy zero
print("Bit na pozycji", n, "dla liczby", number, "wynosi", bit)


# SPRAWDZENIE (to jest opcjonalne)
print("{:08b}",format(number))
print("{:08b}",format(mask))
print("-" * 8)
print("{:08b}",format(result))



# ------------------------------------------------------------------------------------
# LABORATORIUM 10 - ZAD 1

# # ZAD. 1
#
# Napisz skrypt, pobierający od użytkownika zbiór imion, w tym celu:
# • skrypt powinien zapytać użytkownika o liczbę elementów zbioru,
# • pobrać kolejne elementy i zapisać je do listy,
# • wyświetlić w podsumowaniu jakie imiona pobrał od użytkownika.


# ROZWIĄZANIE PANA MARCINA:
names  = [] # to jest zmienna na imiona
name_number = int(input("Podaj liczbę imion: "))

for i in range(1, name_number + 1): #tu to 1 przed zmienną name_number jest po to żeby liczenie nie zaczęło się od bitu liczby 0, a od 1 - gdyby było bez tego, to jakbym podał liczbe imion 3, to by mi naliczyło 4 imiona, bo zaczeło by liczyć od 0, czyli 0=imie 1, 1=imie 2, 2=imie 3, 3=imie 4
    names.append(input("Podaj " + str(i) + " imię: "))

print ("Od użytkowanika pobrano nastepujace imiona: ", names)



# ------------------------------------------------------------------------------------
# LABORATORIUM 10 - ZAD 2

# # ZAD. 2
# Napisz program, który zasymuluje 16 rzutów kostką do gry a następnie
# wyświetli poniższe informacje:
# • zestaw wylosowanych wyników,
# • wyrzucaną wartość za 8 razem,
# • liczbę wyrzuconych szóstek,
# • maksymalną liczbę wyrzuconych tych samych wartości pod rząd.



# ROZWIĄZANIE PANA MARCINA:

import random

dice_rolls_total = 16 #definuijemy stałą, w której będziemy przechowywać ilośc rzutów kostką - ma być 16
rolls = [] # tu przechwujemy listę wylosowanych oczek

for i in range (dice_rolls_total):
    rolls.append(random.randint(1, 6))
print ("Zbior wyników po", dice_rolls_total, "rzutach kostką do gry:", rolls) # to jest podpunkt 1

print ("Za 8 razem wyrzucono wartość", rolls[8 - 1] ) # to jest podpunkt 2 bez kropki po wartosc
print ("Za 8 razem wyrzucono wartość", str(rolls[8 - 1]) + "." ) # to jest podpunkt 2, ale z kropką po 'wartość'

# podpunkt 3
sixes_total = 0 # na początku tą zmienną pomocniczą ustawiamy na 0
for roll in rolls:
    if roll == 6:
        sixes_total += 1 # to jestzwiakszenie za pomoca opreattoar '+=' o 1
print("Wyrzucono", sixes_total, "razy szostke")

# podpunkt 4
in_row_value_tmp = rolls[0] #zmienna pod rząd, ale pomocnicza = tmp=temporary
in_row_total_tmp = 0 # pod rząd total, tez pomocnicza = tmp=temporary

in_row_value = 0 #tu juz nie pomocnicze, tylko koncowe
in_row_total = 0 # tu juz nie pomocnicze, tylko koncowe

for roll in rolls:
    if(roll == in_row_value_tmp):
        in_row_total_tmp += 1 # in_row_total_tmp zwiaksza sie za pomoca opreattoar '+=', o 1
    else:
        in_row_value_tmp = roll
        in_row_total_tmp = 1
    if in_row_total_tmp > in_row_total:
        in_row_total = in_row_total_tmp
        in_row_value = in_row_value_tmp

print ("Pod rząd wyrzucono: ", in_row_total, "razy wartość", in_row_value)
print ("Pod rząd wyrzucono: ", in_row_total, "razy wartość", str(in_row_value) + ".") # to jest to samo co u góry, ale z kropką po "wartość"



# ------------------------------------------------------------------------------------
# LABORATORIUM 10 - ZAD 3

# # ZAD. 3

# Napisz skrypt, który znajdzie najczęściej występującą cyfrę w zbiorze.
# Np. w zbiorze [4, 1, 2, 9, 4, 4] najczęściej występującą cyfrą jest 4,
# występuje 3 razy.

# ROZWIĄZANIE PANA MARCINA:



digits = [1, 2, 4, 6, 6, 2, 6, 6, 9] # zbior naszych cyfr - tu w tym zadaniu podaje z reki zbior tymczasowych elementów
frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]# zmienna pomocnicza, które dotyczy się listy z częstościa wystepowania poszczególnych elemntow -  z reki dajemy liste 10-elemntową

for digit in digits:
    frequency[digit] += 1

print(frequency)

most_common = -1
for i in range (len(frequency)):
    if frequency[i] > most_common:
        most_common = i

print("Najczęściej występującą cyfrą jest " + str(most_common) + ",", "występuje", frequency[most_common], "razy.")