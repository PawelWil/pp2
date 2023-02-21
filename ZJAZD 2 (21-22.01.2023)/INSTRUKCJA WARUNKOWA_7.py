# ctr alt l = prawidłowe ustawienie kodu!

# INSTRUKCJA WARUNKOWA

#  Operatory relacji -------
# • == równości
# • != nierówności
# • > większości
# • < mniejszości
# • >= większości lub równości
# • <= mniejszości lub równości

#  Priorytety operatorów -------
# Podstawy programowania w języku Python - Instrukcja warunkowa 3
# Priorytet Operator
# 1 +, - jednoargumentowe
# 2 **
# 3 *, /, //, %
# 4 +, - dwuargumentowe
# 5 <, <=, >, >=
# 6 ==, !=


# print ( 7 > 11 ) # czy 7 jest większe od 11 - nie jest, czyli dostajemy odpowiedź 'false'
# print ( 7 < 11 ) # tu 7 jest mniejsze od 11, więc 'true'


# a, b = 11, 9 # przypisujemy wartości zmiennych w jednym wierszu, ale jest dużo mniej czytelny. Dużo bardziej czytelnie jest, gdy to robimy w kazdym soobnym wierszu - tu a = 11, zaś b = 9
# print (a >= b) # oczywiscie true

# print (2 == 2)
# print (2 = 2.) # tu w informacji błedu dostaniemy info, że musimy dać operator == --> 'SyntaxError: expression cannot contain assignment, perhaps you meant "=="?'

# number = 2
# if number > 3: # ważny jest dwukropek na koncu linii -- to jest instrukcja warunowa if, gdzie diwe poniższe linie to blok kodu, który wykona się jeśli te warunki zostaną spoełnione
#     print("liczba jest większa niż 3 ") # to jest pisanie blowoe, czyli są wcięcia, ale jest to robione automatycznie
#     print ("Hurra!")
# else:
#     print ("Koniec")

# tu gdy mamy 2, czyli jest mniejsze od 3, czyli jest false i automatycznie przechodzi do linii koniec i zamyka ten blok kodu.
# wciecia musimy stossowac konsekwetnie - wcięcia mozemy robić za pomocą spacji i tabulatora, ale trza wybrać jedną wersję, czy to będzie tab, czy spacja. Ale najlepiej dawać tabulator
# jeśli chcemy spacje do wcięć, to ich ilość zawsze musi być taka sama, inaczej będą błędy, dlatego tabulator jest najlepszy, bo nam zawsze ustawi 4 spacje!

# A. if + else
# number = 0
# if number > 0:
#     print("Liczba większa od zera")
# else: #  przeciwnym razie
#     print("Liczba mniejsza lub równa zero")


# B. if + else + elif
# number = 0
# if number > 0:
#     print("Liczba większa od zera")
# elif number < 0: # jeśli number jest czasami mniejsze od zera. ELifów można stosować wiele
#     print("Liczba mniejsza od zera")
# else:
#     print("Liczba równa zero")


# C. Program, który sprawdza liczbę

# number = int(input("Podaj liczbę: "))
# print ("Liczba jest: ")
     # sprawdzamy czy liczba jest parzysta
# if number % 2 == 0:
#     print ("parzysta")
# else:
#     print ("nieparzysta")

    # teraz czy liczba jest podzielna przez 5
# if number % 5 == 0:
#     print ("podzielna przez 5")
# else:
#     print ("niepodzielna przez 5")

     # teraz czy liczba jest podzielna przez 7
# if number % 7 == 0:
#     print ("podzielna przez 7")
# else:
#     print ("niepodzielna przez 7")


      # C. Pierwsza gra :) - ODGADNIJ LICZBĘ
# import random # to jest ściągnięcie biblioteki, która jest mechanizmem do losowania liczb (jakichs znaków)

# number = random.randint(1, 3) # ona nam losuje liczbę z przedziału jaki jej podamy, czyli w naszym przypadku, z przdziału od 1 do 3
# guess = int(input("Zgadnij jaką liczbę mam na myśli (chodzi o: 1, 2 lub 3) : ")) # zmienna która nam poda jaka liczbę mamy na mysli
# if guess == number:
#     print("brawo! Dokładnie taką liczbę miałem na myśli!")
# else:
#     print("niestety, myślałem o liczbie: " + str(number) + ".")


# ---- POnIŻEJ opcja z podwójną próbą zgadywania  :) -  tu zastosowałem dwa razy instrukcję 'else'

# import random # to jest ściągnięcie biblioteki, która jest mechanizmem do losowania liczb (jakichs znaków)

# number = random.randint(1, 3) # ona nam losuje liczbę z przedziału jaki jej podamy, czyli w naszym przypadku, z przdziału od 1 do 3

# guess = int(input("Zgadnij jaką liczbę mam na myśli (chodzi o: 1, 2 lub 3) : ")) # zmienna która nam poda jaka liczbę mamy na mysli

# if guess == number:
#     print("brawo! Dokładnie taką liczbę miałem na myśli!")
# else:
#     guess = int(input("Zgadnij jaką liczbę mam na myśli (chodzi o: 1, 2 lub 3) : "))
#     if guess == number:
#         print("brawo za drugim razem")
#     else:
#         print ('niestety..')


