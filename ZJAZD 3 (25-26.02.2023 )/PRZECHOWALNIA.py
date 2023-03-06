# Lab 11 - Zad 1

# Napisz skrypt symulujący grę losową:
# • użytkownik obstawia 6 liczb z 49,
# • program losuje 6 liczb z 49,
# • użytkownik dostaje informacje o ilości trafień.


# SPOSÓB Pana Marcina

import random # ten moduł generuje liczby pseudolosowe

user_numbers=[] # liczby od uzytkownika
random_numbers = []#miejsce do zapisu wylosowynch liczb przez komputer
hit_total = 0 # teraz chcmey mieć całkowitą liczbę trafien

# 1 podpunkt - pobranie liczb od uzytkownika i zapisanie - użytkownik obstawia 6 liczb z 49,
# ma być pobrane 6 liczb
for i in range(6): # pętla która będzie przechoidzła 6 razy - oczywiscie to robi 'for'
    # user_numbers.append(int(input("Podaj liczbę (od 1 do 49): ")))
    user_numbers.append(int(input("Podaj" + str(i+1) + "liczbę (od 1 do 49): "))) # tu poprzez konkatecja ładniej bedzie wyglądać

    # 2 podpunkt: program losuje 6 liczb z 49,

    random_numbers = random.sample(range(1,50), 6) # ta funkcja sample wylosuje daną liczbę ze zbioru 1,50 + 6 liczb


# 3 podpunkt: użytkownik dostaje informacje o ilości trafień.

for number in user_numbers:
    if number in random_numbers:
        hit_total +=1

# sortowanie:
user_numbers.sort()
random_numbers.sort()

print("Wylosowane liczby:", random_numbers)
print("Obstawione liczby użytkowników,", user_numbers)
print("Trafiono:", hit_total, "liczb")




# Mój SPOSÓB
# import random
#
# random_numbers = [] # tu umieszczamy te liczby, w tej liście
#
# for i in range (6):  # teraz iterujemy tyle razy ile razy mamy wylosowac liczb - w tym przypadku 6 - to jest na sztywno 3 losowanie , ale to jest zle, musi bec petla while ze zmienna counter
#     counter = 6
#
# while counter:
#     number = random.randint (0, 49)
#     if  number not in random_numbers:
#         random_numbers.append(number)  # tu nam losuje liczbe ze zbioru od 1 do 10
#         counter -= 1 # counter = counter - 1
# random_numbers.sort() # teraz po losowaniu jeszcze musimy posrtować + sprawdzenie czy jest już w naszym zbiorzez, jesli tak, to musimy losować jeszcze raz
#
#
# print (random_numbers)


# ------------------
# Lab 11 - zadanie 2
#
# Napisz skrypt pobierający od użytkownika serię liczb całkowitych, a
# następnie wyświetl je w kolejności malejącej pozbywając się wcześniej
# duplikatów.

# SPOSÓB PANA MARCINA:

# ile liczb w serii będzie się podawać
# pobieram od uzytkownika liczby + zapisywał je do list
numbers = [] # nawza listy
numbers_total = int(input("Podaj liczbe elemntów zbioru: "))# ile tyvch libz uzytkownik bedzie podawał

# teraz uruchamaiamy pętle, jak już mamy info od uzytkowniko ile liczb
for i in range (numbers_total):
    number = int(input("Podaj" + str(i+1) + "elemnt zbioru:")) # teraz pobieramy jakąs liczbę, któą oczywisvie zamieniamy na calkowitą, czyli int
    numbers.append(number) # dopisujemy liczbę, za pomocą append



# teraz mamy je klejności malejącej:

numbers.sort(reverse=True) # sortowanie male
# POZBYWANIE sie duplikatów - poprzez nową liste bez duplikatów
numbers_without_duplicates = []
# a teraz w  petli for robim:
for number in numbers:
    if number not in numbers_without_duplicates:
        numbers_without_duplicates.append(number)


print(numbers_without_duplicates)


# -------------------
# Lab 11 - zadanie 3
#
# Napisz skrypt symulujący rozgrywkę gry w szachy, w tym celu:
# • stwórz wirtualną szachownicę,
# • na wirtualnej szachownicy rozmieść losowo 2. dowolne figury szachowe i 3. piony,
# • zaprezentuj użytkownikowi stan wirtualnej szachownicy.


import random

# Definiujemy zbiory na początek:
#1. Okreslamy puste pole szachowe:
BLANK_SQUARE = "--"

#.2 LIsat figur ktore beded chcial rozmiscic losowwo:
pieces = ("WP", "BP", "BP", "BT", "WQ" )
# teraz te 5 elelmntów losowo rozmieszczamy na szacxhownicy ( 3piony, wieza, damka)

#nasza szachownica + macierz
chessboard = [[BLANK_SQUARE for i in range (8)] for i in range(8)] # tu robimy wyrazenie zagniezdzaone, dla 8 elementów --> GENERALNIE mamy: to są elementy w wierszu, któe powtarzamu 8 razy

# teraz robimy losowanie
counter = 0 #dajemy do losowanie zmienną counter

# zebyy nie było teraz nadpisywania
while counter <5: # dlatego 5, bo przecie zmamy 5 elelntów --do momnetu jak counrter będzie mniejszy od 5 - do tej pory ta pętla się bedzie kręcicc
    row = random.randint (0, 7) # losujemy wiersz od 0 włacznie do 7 włacznie
    column = random.randint(0,7) # teraz losujemy kolumny
    if chessboard [row][column] == BLANK_SQUARE:# teraz sprawdzamy czy na naszej planszy nie ma czasem w row , czy kolumnie - czy to czasem nie jest puste po[le
        chessboard[row][column] = pieces[counter]
        counter += 1


# teraz zostaje wyswietlanie nam tej szachownicyu: tu pętla w pętli

for row in range (len(chessboard)): # obracoam tą pętlą jaki jest rozmiar mojej szachownicy
    if row ==0:
        print(" ", "A ", "B ", "C ", "D ", "E ", "F ", "G ", "H ", sep=" ")
    print (row +1, end = " ")
    for column in range (len(chessboard[row])):
        print(chessboard[row][column], end=" ") # teraz wyswiatlamy plansze szachwową, któa skalaada si e zwiersza i kolumn i oczywiscie argi,et end na ostep
    print()


# COŚ MI NIE DZIAŁA - FILM nr 3... :(

# ------------------
# LAB. 12, ZAD.1
#
# Napisz funkcję, której zadaniem będzie wyświetlić na ekranie dowolny znak, dowolną
# ilość razy, w poziomie lub w pionie

# Rozwiązanie Pana Marcina:

def print_char(character="*", rep=10, vert=False): # na pewno potrzebujemy funkcj - te zmienne obok, to śa nasze zmienne , wewnetrzne, nie systemowe - tylko dla funkcji. Nie można ich uzywa c na zewnątrrz, tylko sa w obrebie funkci 'char'
# pass # robimy zaslepke na sam początek
    for i in range (rep):
        if vert:
            print (character)
        else:
            print(character + " ", end = "")
    if not vert:
        print()
    print()

print_char()
print_char("+", 5, True)
print_char("^", 7, False)


# -------------------
# LAB 12, ZAD.2

# Napisz skrypt obliczający obwód, pole powierzchni i długość przekątnej dla
# prostokątów o następujących długościach boków:
# • 4 i 5,
# • 2678 i 5678,
# • 344555 i 788998


# tworzymy kilka funcji

# 1 funkcja - liczy obwód prostokąta:

def perimiter(a, b):
    return 2 * a + 2 * b #dodajemy liczenie obwodu

# 2 funkcja - liczy pole pow prostokąta:

def surface_area(a, b):
    return a * b

# 3 funkcja - dług przekatnej prostokąta_z tw. Pitagorasa:
def diaganol_length(a, b):
    return (a **2 + b**2) ** .5
    # lub tak
    # return (a ** 2 + b ** 2) ** (1/2)

# teraz pokazujemy rezulataty za pomocą jednej funkcji:

def show_result (a, b):# z niej wywolujemy inne funkcje
    print ("prost o bokach ", a, "i", b)
    print("Owbod:", perimiter(a, b))
    print("Pole pow", surface_area(a, b))
    print("Dlug przek", diaganol_length(a, b))
    print()

show_result(4, 5)
show_result(2678, 5678)
show_result(344555, 788998)

# --------------
# LAB 12, ZAD.3

# Napisz program obliczającej wskaźnik BMI (Body Mass Index), w tym celu:
# • zapytaj użytkownika o wzrost i wagę,
# • stwórz funkcję obliczającą wskaźnik BMI na podstawie podanych przez użytkownika danych,
# • stwórz funkcję wyznaczającą odpowiednią kategorię (niedowaga, waga prawidłowa, nadwaga,
# otyłość) na podstawie wskaźnika BMI,
# • zaprezentuj wyniki korzystając z wcześniej przygotowanych funkcji.


# jak się liczy wskaźnik BMI - najlepiej sprawdzić w google
# BMI = masa / (wzrost)**2

# 1. zapytaj użytkownika o wzrost i wagę,

print ("Obliczanie wskaźnika BMI")
weight_in_kg = float (input("podaj swoją wagę w kg:")) # to dajemy liczbe zmiennprzecinkową, bo moze byc np 55,5 kg
height_in_cm = float (input("podaj swoj wzrost w cm:"))

# print(weight_in_kg, height_in_cm)  # to jest print testowy

# 2. stwórz funkcję obliczającą wskaźnik BMI na podstawie podanych przez użytkownika danych
def calculate_bmi(weight_in_kg, height_in_m):
    return weight_in_kg / height_in_m ** 2

print(calculate_bmi(weight_in_kg, height_in_cm * 0.01)) # height_in_cm * 0.01 - to jest przeliczenie na metry


# 3.  stwórz funkcję wyznaczającą odpowiednią kategorię (niedowaga, waga prawidłowa, nadwaga,
# # otyłość) na podstawie wskaźnika BMI,

def determine_bmi_category(bmi):
    if bmi < 18.5:
        return "niedowaga" # zwracamy, coś podobnego co print
    elif bmi < 25:
        return "waga prawidlowa"
    elif bmi <30:
        return "nadwaga"
    else:
        return "otylosc"

# 4. • zaprezentuj wyniki korzystając z wcześniej przygotowanych funkcji.

bmi = calculate_bmi(weight_in_kg, height_in_cm * 0.01)
category = determine_bmi_category(bmi)

print ("Wskaznik BMI: ", bmi)
print ("Kategoria: ", category)



# -------------------

# Lab 13 - Zad.1
# Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskazanej listy.

#Rozwiązanie Pana Marcina:

# 1 sposób rozwiązania:
# def pow (numbers, exponent): # funkcja pow=power_numbers=podnoszenie do potęgi, będzie przyjmowała dwa argumenty. Numbers=potęga
#     for i in range (len(numbers)):
#         numbers[i] = numbers[i] ** exponent
#     return numbers
#
# print(pow([1,2,3], 2))
#
# print(pow([2, 7, 33], 5))


# # 2 sposób rozwiązania:
#
# def pow (numbers, exponent): # funkcja pow=power_numbers=podnoszenie do potęgi, będzie przyjmowała dwa argumenty. Numbers=potęga
#     for i in range (len(numbers)):
#         numbers[i] = numbers[i] ** exponent
#     return numbers
#
# def pow2(numbers, exponent):
#     result = []
#     for n in numbers:
#         result.append(n ** exponent)
#     return result
#
# print(pow([1,2,3], 2))
# print(pow2([1,2,3], 2))
#
# print(pow([2, 7, 33], 5))
# print(pow2([2, 7, 33], 5))

# 3 sposób rozwiązania:

def pow (numbers, exponent): # funkcja pow=power_numbers=podnoszenie do potęgi, będzie przyjmowała dwa argumenty. Numbers=potęga
    for i in range (len(numbers)):
        numbers[i] = numbers[i] ** exponent
    return numbers

def pow2(numbers, exponent):
    result = []
    for n in numbers:
        result.append(n ** exponent)
    return result

def pow3(numbers, exponent):
    return [x ** exponent for x in numbers]



print(pow([1,2,3], 2))
print(pow2([1,2,3], 2))
print(pow3([1,2,3], 2))

print(pow([2, 7, 33], 5))
print(pow2([2, 7, 33], 5))
print(pow3([2, 7, 33], 5))




#MOJA PRÓBA :)
# def potega_numbers(numbers): # to co jest w nawiasie to są parametry tej fukcji, tutja to zmienna 'numbers'
#     potega = 4
#     for element in numbers: #teraz korzystamy z petli, ktora to zmienna dostanie kolejne lelemty, któr bedzizemy iteroiwac, dla nas to lista, czyli dopisz/dodaj ten elemnt
#         result = (element ** potega)
#         # element = str(numbers) + str(1)
#     return result
#
# numbers = [1, 3] # to jest zmienna globalna 'numbers'
# result = potega_numbers(numbers)
# print (result)


# -------------------
# Lab 13 - Zad.2
# Korzystając z rekurencji wypisz na ekranie tabliczkę mnożenie do 100.

# krok pierwszy -
def show_operation(a, b): # bedzie miala parametry a i b, czyli mnożymy coś przez coś
    print(a, "x", b, "=", a * b )
    if a == 10 and b==10: # to jest mnozenie do 100, dlatego ttrzeba się na tym zatrzymac
        return
    elif a == 10:
        show_operation(1, b+1)
    else:
        show_operation(a + 1, b)


show_operation(1, 1) # tu mnożymy liczby od 1 do 100 zaczynając od 1
# show_operation(1, 2) # tu mnożymy liczby od 1 do 100 zaczynając od 2



# ------------------
# # Lab 13 - Zad.3
# Napisz skrypt symulujący uproszczone działanie gry losowej "jednoręki bandyta",
# w tym celu:
# • za każdym "pociągnięciem" losuj 3 litery ze zbioru od A do E,
# • kontynuuj losowania do momentu wystąpienia 3 takich samych liter np. A A A,
# • wyświetl informację o wynikach poszczególnych losowań oraz numer próby,
# • przemyśl jak dużo zmian trzeba wprowadzić w skrypcie, aby losować z większego zbioru liter, a także
# większą liczbę liter.


# 1 krok - zaczynamy od losowania -  za każdym "pociągnięciem" losuj 3 litery ze zbioru od A do E,

import random

# print(ord("A")) # funkcja ord zwraca nam numerek który jest reprezentowany przez dany znak

# print(chr(65)) # chr ta funckja przezchdzi z liczby na Ascii, czyli z 65 na "A" w kodzie ascii

# def draw_letter():# losujemy jedną literkę
#     return chr(random.randint(ord("A"), ord("E"))) # zwroc litere, w zakresie od "A" do "E"
#
# def draw_row():
#     return [draw_letter() for i in range (3)]
#
# # 2 krok - kontynuuj losowania do momentu wystąpienia 3 takich samych liter np. A A A,
# def check(row):
#      if row[0] == row[1] and row[1] == row[2]:
#          return True
#      else:
#          return False
#
# # print (check(["A", "B", "C"])) # False
# #
# # print (check(["A", "A", "A"])) # True
#
#
# # krok 3 - # • wyświetl informację o wynikach poszczególnych losowań oraz numer próby,
# counter = 1
# while True:
#     row = draw_row()
#     print(row, counter)
#     if check(row):
#         break
#     counter += 1


# krok 4 - przemyśl jak dużo zmian trzeba wprowadzić w skrypcie, aby losować z większego zbioru liter, a także
# # większą liczbę liter.

import random

FIRST_SYMBOL = "A"
LAST_SYMBOL = "H"
NUMBER_OF_LETTERS = 5

# print(ord("A")) # funkcja ord zwraca nam numerek który jest reprezentowany przez dany znak

# print(chr(65)) # chr ta funckja przezchdzi z liczby na Ascii, czyli z 65 na "A" w kodzie ascii

def draw_letter():# losujemy jedną literkę
    return chr(random.randint(ord(FIRST_SYMBOL), ord(LAST_SYMBOL))) # zwroc litere, w zakresie od "A" do "H" - tu zwikeszamy większy zbior od A do H, a nie jak było od A do E

def draw_row():
    return [draw_letter() for i in range (NUMBER_OF_LETTERS)]

# 2 krok - kontynuuj losowania do momentu wystąpienia 3 takich samych liter np. A A A,
def check(row):
    first_element = row[0]
    for element in row:
        if element != first_element:
            return False
    return True



# print (check(["A", "B", "C"])) # False
#
# print (check(["A", "A", "A"])) # True


# krok 3 - # • wyświetl informację o wynikach poszczególnych losowań oraz numer próby,
counter = 1
while True:
    row = draw_row()
    print(row, counter)
    if check(row):
        break
    counter += 1


# --------------------
# # LAB 14 - ZAD.1
#
#  Napisz wyszukiwarkę numerów telefonów:
# • zdefiniuj słownik par imię -> numer telefonu,
# • zapytaj użytkownika o imię,
# • wyświetl użytkownikowi numer telefonu lub informacje o jego braku.


phones = {
    "Adam": 123123123,
    "Karol": 111222333,
    "Mariola": 22233344455,
    "Iza": 2312312312
}

while True:
    name = input ("Podaj imię: ")
    if name == "":
        break
    if name in phones:
        print("Telefon:", phones[name])
    else:
        print("NIe znaleziono telefonu dla imienia", name)


# ------------------
# LAB 14 - ZAD 2
#
# Napisz funkcje zamieniającą 3 listy na 1 krotkę bez powtarzających się elementów.
# Przykład: [1, 2], [1, 1], [4, 4, 4] -> (1, 2, 4)

def merge_list_without_duplicates(source, target): # source = lista zrodlowa, Target=lista wynikowa)
    for e in source:
        if e not in target:
            target.append(e)


# probujemy mergować
def transform_data(list1, list2, list3): #pobierac bedzie 3 listy
    result = [] #pusta lista,
    merge_list_without_duplicates(list1, result)
    merge_list_without_duplicates(list2, result)
    merge_list_without_duplicates(list3, result)
    return tuple(result)

    # pass # to jak dam, to zawiesza działanie linii nad

print(transform_data([1,2], [1,1], [4,4,4]))
print(transform_data([1,2,3], [1,2,3], [4,5,6]))
print(transform_data(["Ala","ma"], ["Ala","ma","kota"], ["mysz"]))

# to zadanie polega na tym, że wszystko się musi zawierac w jednym wierszu, ale bez powtórzeń



# -------------------
# LAB 14 - ZAD 3
#
# Napisz program zliczający punkty w grach (karcianych, planszowych itp.), realizujący:
# • definiowanie liczby oraz imion graczy,
# • definiowanie liczby punktów potrzebnych do wygranej,
# • pobieranie informacji o zdobytych punktach w każdej turze gry,
# • wyświetlanie informacji o zwycięzcy oraz zdobytych punktach poszczególnych graczy.


# 1 krok: definiowanie liczby oraz imion graczy,------
def define_player(player_no):  # pojedynczy gracz
    player_points = []  # lista
    player_name = input("Podaj imię" + str(player_no) + "gracza:")
    return {player_name: player_points}


def define_players():
    players = {}
    players_total = int(input("Podaj liczbe graczy (1-8): "))  # bedzie tam info ilu graczy tam bedzie
    for i in range(players_total):
        players.update(define_player(i + 1))
    return players


# players = define_players()
# print(players)


# 2 krok: definiowanie liczby punktów potrzebnych do wygranej,-----------

def define_win_points():
    return int(input("Zdefiniuj liczbę punktów wygranej: "))


# 3 krok: pobieranie informacji o zdobytych punktach w każdej turze gry,---------

def is_winner(players, win_points):
    for player_name, player_points in players.items():
        sum = 0
        for p in player_points:
            sum += p
        if sum >= win_points:
            return True
    return False


def count_points(players, win_points):
    counter = 1
    while True:
        print("\nTura: ", counter)
        for player_name in players.keys():
            player_points = int(input("Podaj punkty dla gracza" + player_name + ":"))
            players[player_name].append(player_points)
            if is_winner(players, win_points):
                return player_name
        counter += 1


# 4 krok: wyświetlanie informacji o zwycięzcy oraz zdobytych punktach poszczególnych graczy.------------

def show_results(players, winner):
    print("\nWygrał gracz i imieniu: ", winner + ", brawo!\n")
    print("Szczegółowa tabela wyników")
    for player, points in players.items():
        print(player, "->", points)


players = define_players()
win_points = define_win_points()
winner = count_points(players, win_points)
show_results(players, winner)



# ------------------
# # LAB 15 - ZAD 1
#
# Utwórz funkcję o nazwie safe_int(), która pobiera pojedynczy argument arg.
# Jeśli to możliwe, funkcja powinna przekonwertować podany argument na typ int
# i zwrócić go. Jeśli jednak nie jest to możliwe (tj. jeśli wystąpi wyjątek), funkcja
# powinna zwrócić None.

def safe_int(arg):
    try:
        return int(arg)
    except:
        return None

print(safe_int(1))
print(safe_int(7.2))
print(safe_int("jeden"))


# ----------------

# # LAB 15 - ZAD 2
#
# Napisz program pobierający od użytkownika 3 liczby zmiennoprzecinkowe = FLOAT NUMBERS
# Uwzględnij możliwość pomyłki użytkownika.

numbers = [] # w niej zapiszany pozyskane liczby
counter = 1

while True:
    if counter > 3:
        break

    try:
        number = float(input("Podaj " + str(counter) + "liczbę zmiennoprzecinkową"))
        numbers.append(number)# dodajemy ją do pustej listy powyżej za pomocą metody append
        counter += 1
    except:
        print("Podana wart jest niepopr, sprobuj ponownie")
print(numbers)



# --------------
# LAB 15 - ZAD 3
#
# Zabezpiecz program zliczający punkty w grach (moduł 14, lab 3) przed
# wprowadzaniem błędnych danych przez użytkownika.



# Poniszy program jezt z LAB 14, zad3

def fetch_and_validate_int(standard_msg, error_msg="To nie jest liczba"):
    while True:
        try:
            return int(input(standard_msg))
        except:
            print(error_msg)


def define_player(player_no):  # pojedynczy gracz
    player_points = []  # lista
    player_name = input("Podaj imię" + str(player_no) + "gracza:")
    return {player_name: player_points}


def define_players():
    players = {}
    players_total = fetch_and_validate_int("Podaj liczbe graczy (1-8): ")  # bedzie tam info ilu graczy tam bedzie
    for i in range(players_total):
        players.update(define_player(i + 1))
    return players



def define_win_points():
    return fetch_and_validate_int("Zdefiniuj liczbę punktów wygranej: ")



def is_winner(players, win_points):
    for player_name, player_points in players.items():
        sum = 0
        for p in player_points:
            sum += p
        if sum >= win_points:
            return True
    return False


def count_points(players, win_points):
    counter = 1
    while True:
        print("\nTura: ", counter)
        for player_name in players.keys():
            player_points = fetch_and_validate_int("Podaj punkty dla gracza" + player_name + ":")
            players[player_name].append(player_points)
            if is_winner(players, win_points):
                return player_name
        counter += 1



def show_results(players, winner):
    print("\nWygrał gracz i imieniu: ", winner + ", brawo!\n")
    print("Szczegółowa tabela wyników")
    for player, points in players.items():
        print(player, "->", points)


players = define_players()
win_points = define_win_points()
winner = count_points(players, win_points)
show_results(players, winner)




