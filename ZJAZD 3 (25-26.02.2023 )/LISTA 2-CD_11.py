# # zamiana wartości dwóch zmiennych
# a = 1 #1 zmienna
# b = 4 # 2 zmienna
#
# print("a =", a, "b=", b)
# --i Teraz zamiana wartości, chcemy żeby a=4, zaś b=1
# -1 sposób, po prostu dajemy zmienną tymczasową tmp=a, którą potem podstawiamy pod b, która jest równa a, zaś a przyrównujemy do b, i a staje się b
# tmp = a
# a = b
# b = tmp

# print("a =", a, "b=", b)
# -2 sposób, ten docelowy i najłatwiejszy: po prostu w jednej linii umieszczamy a, b, i po =, podmieniamy kolejność!
# lub
# a, b = b, a # to można zamiana kolejnościa uzyskać zamiane
# print("a =", a, "b=", b)

# 2.  zamiana 2 lub więcej elementów w liście

# numbers = [1, 2, 3]  # przykładowa lista
# #zamiana dwoch pierwszych elemntów, podobnie jak powyżej, po prostu zamieniamy kolejnością po znaku '='
# numbers[0], numbers[1] = numbers[1], numbers[0]

# print (numbers)


# 3. Bubble sort - sortowanie bąbelkowe -

# numbers = [4, 5, 2, 1] # lista, która ma 4 elementy nieposortowane
# teraz najpierw sparwdzenie czy 4>5, potem czy 5 wieksze od 2 (czyli trezba te dwa elemnty odwrocic), czy 5>1 - tak(więc znów trza bedzie to odwrocic)
# ale to wszystsko trzeba zrobić przechodząc pętle zamianna step by step, tylko ze to jest mało wydajne....
# numbers = [4, 2, 1, 5] - 1 etap
# numbers = [2, 1, 4, 5] - 2 etap
# numbers = [1, 2, 4, 5] - 3 etap


# numbers = [4, 5, 2, 1] # tą liste chcemy posortowac za pomocą metody bąbelkowej, czy pętli, która przeskakuje pomiędzy liczbamy i krok po kroku je sortuje.
# z tym, że ta metoda jest długa i niepraktyczna - warto ją po prostu znać

# swapped = True #wprowadzamy zmeinną pocniczą, czy zostało zamieniiene, czy była zamiana. Pętla się bedzie wykonywała dopóki zmienna swapped bedzie true
# Pętla się będzie wyoknywała dopóki zmienna swapped będzie true
# while swapped: # robimy to w petli while, dlatego ze nie wiemy ile razy bedziemy iterowac po tyhch elem,entach, az do momnetu gdy osigniemy efekt. Tu swapped dajemy na False, zeby wyrózniła się od true
#     swapped = False #teraz rozmyslnie dajemy swaped na false, zeby móc wyjść z pętli
#     for i in range (len(numbers) - 1): #funkcja len słuzy do oblicznie alosci elemntów i odejmujemy od tego wszytskiegpo 1
#         if numbers[i] > numbers [i+1]: # jesli bedzie wieszka musimy te pierwsze dwa elemnty czyli 4, 5 zamienic
#             numbers[i], numbers[i+1] = numbers [i+1], numbers[i]
#             swapped = True

# print(numbers)


# To samo, ale dla bardziej skomplikowane listy

# numbers = [4, 5, 2, 1, 3, 333333, 3, 456] # tą lsite chcemy posortowac

# swapped = True #wprowadzamy zmeinną pocniczą, czy zostało zamieniiene. Pętla się bedzie wykonywała dopóki zmienna swapped bedzie true

# while swapped: # robimy to w petli while, dlatego ze nie wiemy ile razy bedziemy iterowac po tyhch elem,entach, az do momnetu gdy osigniemy efekt. Tu swapped dajemy na False, zeby wyrózniła się od true
#     swapped = False
#     for i in range (len(numbers) - 1): #funkcja len słuzy do oblicznie alosci elemntów i odejmuje od tego wszytskiegpo 1
#         if numbers[i] > numbers [i+1]: # jesli bedzie wieszka musimy te pierwsze dwa elemnty czyli 4, 5 zamienic
#             numbers[i], numbers[i+1] = numbers [i+1], numbers[i]
#             swapped = True

# print(numbers)

# 4. Bardziej optymalna metopda sortowania - metoda SORT - od największej do najmniejszej - # --praktyczne i szybkie sortowanie, za pomocą metody 'sort'
# numbers = [4, 5, 2, 1, 3, 333333, 3, 456]
# numbers.sort()
# print(numbers)

# 5. Bardziej optymalna metopda sortowania - metoda SORT - od  najmniejszej do największej
# numbers = [4, 5, 2, 1, 3, 333333, 3, 456]
# numbers.sort(reverse=True)
# print(numbers)


# 6. Sortowanie nie liczb, ale innych elementów, np. stringów
# letters = ["A", "C", " ", "B"]  # lista o nazwie 'letter'
# letters.sort()
# print(letters)

# lub sortowanie odwrocone
# letters = ["A", "C", " ", "B"]
# letters.sort(reverse = True)
# print(letters)


# 7. ORD (ordinal = porządkowanie, właściwa kolejnośc) mówi nam jakie mają wartości poszczególne elemnty w kodzie Ascii - dla duzego A i duzego C
# letters = ["A", "C", " ", "B"]
# print(ord("A"), ord("C")) # za pomocą funkcji ord(ordinal), możemy zobaczyć, jaka to jest wartość w kodzie Ascii
# letters.sort()
# print(letters)

# 8. ORD mówi nam jakie mają wartości poszczególne elemnty w kodzie Ascii - dla małego a i małego b i dużego B.
# generalnie małe literki są większe w kodzie Ascii, niż duże litery
# letters = ["a", "a", " ", "B"]
# print(ord("a"), ord("b"))
# letters.sort(reverse = True)
# print(letters)


# ------9. Teraz Lista jako typ referencyjny, czyli na podkreslienie /na większa uważność gdy bedziemy operowac na tych listach

# A. tu mamy dwie nazwy, a lista jedna
# list_1 = [9] # prosta lista, 1-elementowa, jej elementem będzi liczba 9
# list_2 = list_1 # dla tej listy stworzymy kolejną  listę - mamy zmienna lista2, do której podstawiam listę 1.
# Tu można powiedzieć, że mamy jedną listę, której wartość to 9 [9] + ma ona dwie nazwy, które do tel listy [9] prowadzą,
# czyli nazwa=referencja=zmienna list_1 i list_2

# list_2[0] = 13 # dla listy 2 element o indeksie 0, zminieam na 13, czyli zamiast 9 jest 13, ale że list_1=lista_2, to
#wiadomo, że automatycznie ta wartość listy [9], została zmieniona w obu nazwach=referencjach=zmiennych na [13]
# print (list_2) # ale ważne, gdyż obie listy (1 i 2) mają teraz wartość 13, bo referencyjnie lista 1 została przyrównana do listy 2
# print (list_1)


# 10. wycinanie SLising = Robienie kopii
#--- generalnie kopiowanie, nazywane jest jako metoda slicing, czyli wycinanie!

# robienie całościowej kopii:
# list_1 = [9]
# list_2 = list_1 [:]# to robi kopie całej listy, z wszystkimi elementami -czyli w nawiasie kwadratowym, daję dwukropek [:]
# tu dostajemy kopie list_1, zapisaną pod nazwą list_2

#teraz robimy operację z podmianką elementów, dla listy 2, gdzie podtsawimy 13 i finalnie dostaniemy dwie osobne wartości
# dla list_1 = 13, zaś dla list_2=9
# list_2[0] = 13 # elemnt o innkesie 0, zminieam na 13
# print (list_2) # obie listy (1 i 2) mają teraz wartość 13
# print (list_1)
# jak widać dostaliśmy dwie osobne wartości - tu zrobilismy zabieg wycinania listy, który to zabieg tworzy odrębna kopię listy


# ---teraz robimy wycinek, czyli nie pełna kopia, ale jakaś część
# te wycinki=slicing robimy tak:

# ----a. wycinka(slicing), za pomocą indeksów dodatnich
#         0  1  2  3  4  - indeksowanie za pomocą indeksów dodatnich
# numbers=[10, 8, 6, 4, 2] # lista numbers
#       -5  -4 -3 -2 -1  - indeksowanie, za pomocą indeksów ujemnych
# #dla liczby numers chcemy stworzyć nową listę, np. new_numbers, c bedzie wycinkiem , jakąs częscią listy numbers - i teraz mówimy co chcemy wycinać
# new_numbers = numbers[1:3] # chcemy na bazie listy numbers, stworzyć nową listę new_numbers, czyli wycinek jakś cześć listy numbers
# czyli żeby wycinać z listy numbers, wpisujemy numbers(bo z tej losty wycinamy) + w nawiasie kwadratowym, pokazujemy co chcemy wyciąć
# i tu w naszym przykładzie, chcemy wycinać od elementu, który równa się '1', czyli jest to 8 + chcemy jeszcze wyciąć 6, czyli
# dochodzimy do elementu 3(liczba 4), który jest granicą, ale nie jest brany pod uwagę
# robimy to również z użyciem znaku ':', który pokazuje zakres od do
# print(new_numbers) # nowa lista, która jest wynikime numbers
# print(numbers) # one się oczywiście nie zmieniła


# ----b. wycinka(slicing), za pomocą indeksów ujemnych
#          -5 -4 -3 -2 -1
# numbers=[10, 8, 6, 4, 2]
#dla liczby numers chcemy stworzyć nową listę, np. new_numbers, c bedzie wycinkiem , jakąs częscią listy numbers - i teraz mówimy co chcemy wycinać
# new_numbers = numbers[-4:-2] # tu chcemy też wyciąć 8 i 6, ale za pomocą indeksowania ujemnego, czyli wiadomo, że zaczynam
# od indeksu '-4', a kończę na indeksie '-2'
# print(new_numbers) # nowa lista, która jest wynikime numbers
# print(numbers) # one się oczywiście nie zmieniła


# ----c. wycinka(slicing), za pomocą indeksów mieszanych, czyli dodatnich i ujemnych
#        -5 -4 -3 -2 -1
# numbers=[10, 8, 6, 4, 2]
#        1  2  3   4  5
# new_numbers = numbers [-4:3]
# print(new_numbers) # nowa lista, która jest wynikime numbers
# print(numbers) # one się oczywiście nie zmieniła

# ----d. jeśli chcemy całość skopiować, to możemy to zrobić na dwa sposoby. Albo z użyciem[:] albo za pomoca funkcji 'len' = length

# # #dla liczby numers chcemy stworzyć nową listę, np. new_numbers, c bedzie wycinkiem , jakąs częscią listy numbers - i teraz mówimy co chcemy wycinać
# numbers=[10, 8, 6, 4, 2]
# new_numbers = numbers [:] # [:] - to nam kopiuję całość = 1 sposób
# albo
# new_numbers = numbers[0:len(numbers)] # tu musimy podać, że zaczynamy od elemntu 0 i za pomocą len, bierzemy całą listę
# print(new_numbers) # nowa lista, która jest wynikime numbers
# print(numbers) # one się oczywiście nie zmieniła
# jak wiemy funkcja 'len' zwraca nam liczbę elementów, które są zawarte w danej liści.  W naszym przypdaku jest to 5 elemntów:
# print(len(numbers))

# 11. Usuwanie wycinków - dzięki instrukcji del (delete)

#          -5 -4 -3 -2 -1
# numbers=[10, 8, 6, 4, 2]
# #        0  1  2   3  4
# del numbers[1:3] # wylatuje 8 i 6 -tu usuwamy konkretne argumenty
# del numbers [:] # to usuwamy całą listę o nazwię ! - wiadomo, że ':' albo kopiuje całą zawartość listy(jej wszystkie elementy) albo usuwa
# del numbers # to nam nie tyle usuwa elemnty, ale usuwa całą listę. Przez to dostaniemy komunikat- NameError: name 'numbers' is not defined
# print(numbers)


# 12. Operatory IN oraz NOT

# numbers=[10, 8, 6, 4, 2]
#
# print (5 in numbers)# sprawdzenie, czy 5 jest w liscie numbers --> wiadomo, ze nie ma, wiec mamy false
# print(7 not in numbers) #to jest sprawdzenie, że 7 nie ma w tej liscie --> no wiadomo, ze nie ma , wiec mamy True


# 13. Wyrażenie listowe - list comprehensions = listy złożone - chodzi np. o tworzenie bardzo rozbudowanych list(1000 elementów)

# numbers=[10, 8, 6, 4, 2]

# A. generacje duzej listy

# definiujemy pustą listę i za pomocą petli for generujemy bardzo dużo elementów listy
# 1 Sposób
# numbers=[] # definiujemy pustą liste, do której wstawimy elemnty
# for i in range (1, 1001):  # dla elementu i, za pomocą funkcji range będziemy ładować 1000 elemntów do listy,
# czyli dajemy zakres od (1, 1001) i do naszej listy za pomocą metody np. append (zapisywanie na koniec listy, kolejnego elemntu)
# będziemy te elementy dodawać  do listy numbers.
#     numbers.append(i)
# print(numbers)

# 2 sposób, jednolinijokwy - lepszy niż powyższy sposób:
# numbers=[i for i in range (1, 1001)] # mozna to zrobić równiez jedną linijką --> trza się z tym uswoić.
# Upraszcza kod, który staje się przejrzysty.

# print(numbers)

# Kolejny przykład - teraz chcemy, żeby te wartości nie były takie szablonowe:
# numbers=[99 for i in range (1, 1001)] # tu nam daje 1000 razy liczbe 99 - na sztywno dajemy liczbę 99
# print(numbers)

# # kolejny przykład z obliczeniem:
# numbers=[i ** 2 for i in range (1, 101)] # tu możemy te wszystkie wartości podnięść do potęgi, załóżmy dla 100 elementów
# print(numbers)

# kolejny przykład - mowa o instrukcji warunkowej, po pętli użyjemy zapisu if i dodamy jakiś warunkek -
# np wyświetlamy liczby od 1 do, ale mają być liczby parzyste. Oczywiście mogą być różne warunki, np. nieparzyste (%2=!0)
# podzielne przez 7 (% 7 == 0) itd. itp.
# numbers=[i for i in range (1, 101) if i % 2 ==0 ] # tu nam daje liczby do 100, ale tylko liczby parzyste
# print(numbers)


# ZADANIE:
# Chcemy dowiedziec się, ile jest liczb w przedziale od 1 do 300, które dzielą się przez 3 i 7 (jednocześnie), z wykorzystaniem wyrażenia listowego.
# Ma to być jedna linijka kodu.

# -- tu mamy ile liczb
# print(len([i for i in range (1, 301)if i % 3 == 0 and i % 7 == 0])) # funkcja len (length) mówi nam ile liczb w tym przedziale jest
# które jednocześnie dzielą się przez 3 i 7. Czyli ta liczba 14, to pokazuje nam ilość tych liczb.
# !Wyrażenie listowe, to jest to wyrażenie ujęte w nawiasie

# -- tu mamy jakie to są liczby
# numbers=[i for i in range (1, 301) if i % 3 ==0 and i % 7 == 0 ] # to nam mówi, jakie to są liczby
# # #
# print(numbers)

# 14. Listy wielowymiarowe, czyli listy, w listach

# numbers = [1, 2, 3]
# # l2 = numbers # lista druga = l2, która wskaywac bedzie to samo co lista numbers
# # ---PRZYKŁAD: zrobic listę i umiescić tam inna listę, czyli zagniezdzenie listy w liscie
# l2 = [numbers] # to jest widoczne wtedy, gdy mamy podwójny nawias kwadratowy

# print(numbers)
# print (l2)

# B. lista w liscie = matrix = macierz
#            0  1  2  3  4
# numbers = [1, 2, 3, 4, 5]

# matrix = [numbers[:], numbers[:]] #A. dwa razy to samo odwolanie, ale dwa raz to wsadzone jest + ich pełne kopie [:]
# print (matrix)

#B.
#            0  1  2  3  4
# numbers = [1, 2, 3, 4, 5]
# numbers[2] = 99 # tu mamy, że na drugim elemencie pojawi się liczba 99

# MATRIX = [numbers [1:2], numbers[2:3], numbers[0]] # tu jak widać mamy listę w liście, po slicingu, czyli odcięciu pewnych liczb
# oraz pokazuje nam rownież konkretny elemnt położony na 0-ym bicie, czyli w naszym przypadku element '1'.
# print (MATRIX)


# ZADANIE  - zaimplementowanie szachownicy - który zwizulalizje nam prostą sytuacje na planszy do gry w szachy

# 8 x 8 - macierz 8 razy 8

#     A B C D E F G H
#   1 # # # # # # # #
#   2 # # # # # # # #
#   3 # # # # # # # #
#   4 # # # # # # # #
#   5 # # # # # # # #
#   6 # # # # # # # #
#   7 # # # # # # # #
#   8 # # # # # # # #


# chess_row = ["--", "--", "--", "--", "--", "--", "--", "--",]# tworzymy liste(szachowy wiersz), która wiadomo będzie miała 8 elemntów=szachowy wiersz - prosty sposób
# chess_row = ["--" for i in range (8) ] # to jest powielanie szachowego wiersza poprzez pętle for

# chessboard = [chess_row [:] for i in range (8)]# teraz  za pomocą zagniezdzonego wyrazenia listowego robie całą szachwonice, za pomoc for robie go 8 razy,
# i tu ważna rzecz, za pomocą [:] zrobiliśmy, ze te wszystkie listy są osobnymi listami

# lub można te powysze ( 2 linie) zrobic za pomoca jednej linii, jak poniżej:
# chessboard = [["--" for i in range (8)] for i in range (8)]
# print (chessboard) # próbne drukowanie, na bazie którego mogę zobaczyć szachownicę - nie jest elemntem całego kodu
#
# # teraz definiujemy elemnty - biały pion + czarny pion
# WHITE_POWN = "WP"
# BLACK_POWN = "BP"
#
# chessboard[0][0] = WHITE_POWN #- w kolumnie 0 i wierszu 0 ustwiamy białego piona - zagnieżdzenie listy w liście
# chessboard[3][5] = BLACK_POWN #- w kolumnie 5 i wierszu 3 ustwiamy białego piona
#
# # teraz wyswietlamy plansze szachową- czyli nic innego jak rysujemy macierz:
# for chess_row in chessboard:
#     for chess_square in chess_row: # tu mamy pętle  w pętli
#         print (chess_square, end = " ")
#     print()


# print (chessboard)


# ZADANIE: losuj trzy liczby ze zbioru od 1 do 10.
# - Ale nie chcemy żeby się powtarzały.
# - Posortuj te liczby, w kolejności rosnącej.

# SPOSÓB I:

import random # moduł do losowania losowego

random_numbers = [] # tu umieszczamy te liczby, w tej liście

# -----TO UŻYCIE PĘTLI 'FOR' jest tylko przykładem losowania na sztywno - poniższa pętla while jest PRAWIDLOWA!!!
# for i in range (3):  # teraz iterujemy tyle razy ile razy mamy wylosowac liczb - w tym przypadku 3
#     random_numbers.append(random.randint(1,10)) ## te liczby, które się pojawią w  liście random_numbers
# wylosujemy poprzez użycie funkcji randint ze zbioru od 1 do 10
# random_numbers.sort()#jak już je wylosujemy i wrzucimy do listy 'random_numbers',
# to jeszcze je w tej liście posortujemy, poprzez funkcję 'sort'
# print (random_numbers)# i teraz zerknijmy, co mamy, poprzez drukowanie za pomocą funkcji 'print'
#-------


#  - for to jest pętla, która ustawia na sztywno ustaloną ilość losowań, ale nie o to nam do konca chodziło, musi bec petla while ze zmienna counter, za pomocą której określamy 3 losowania
# gdzie nie będą się liczby losowane nie powtarzały i potem pętla się kończy

# musi być pętla while, gdzie dodatkowo sprawdzamy, czy już wylosowana liczba jest w naszym zbiorze 'random number, np.[3,3,5] -tu się powtarza liczba 3
# dajemy pętla while = losuj dopóki, i tu dodatkowo jest potrzebna nam zmienna pomocnicza 'couter', która bedzie nam liczbe losowan
# mamy miec 3 wylosowane liczby

counter = 3
while counter:
    number = random.randint (1, 10) # zmienna number będzie przechowuywać liczbę z losowania ze zbioru od 1 do 10
    if  number not in random_numbers: # tu dajemy warunek, który sprawdza, czy wylosowana liczba, sie już w tej liście nie pojawiła, dlatego daje 'not in'
        random_numbers.append(number)  # jeśli się nie pojawiła, to dodaję tą liczbę do zmiennej number
        counter -= 1 # counter = counter - 1 --> czyli jak już losowanie się zakonczyło sukcesem, to muszę zmniejszyć ilość losowań do 2,
        # potem do 1 i na 0 się pętla konczy

random_numbers.sort() # teraz po losowaniu jeszcze musimy posortować

print (random_numbers)


# SPOSÓB II -  na powyższe

# import random
#
# numbers = [ i for i in range (1, 11)]
#
# random_numbers = random.sample (numbers, 3) # tu metode sample - ona losuje elemnty ze zbioru numbers i losuje 3 elemnty
#
# random_numbers = random.sample (numenrs, 3)
#
#
#
# random_numbers.sort() # teraz po losowaniu jeszcze musimy posrtować + sprawdzenie czy jest już w naszym zbiorzez, jesli tak, to musimy losować jeszcze raz
#
#
# print (random_numbers)
