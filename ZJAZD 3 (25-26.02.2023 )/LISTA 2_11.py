# # zamiana wartości dwóch zmiennych
# a = 1
# b = 4
#
# # print("a =", a, "b=", b)
#
# # tmp = a
# # a = b
# # b = tmp
#
# # print("a =", a, "b=", b)
#
# lub
# a, b = b, a # to można zamiana kolejnościa uzyskać zamiane
# print("a =", a, "b=", b)

# 2.  zmaiana elemntów cciąg dalszy

# numbers = [1, 2 ,3]
# #zamiana dw och pierwszych elemntów
# numbers[0], numbers[1] = numbers[1], numbers[0]
#
# print (numbers)


# 3. Bubble sort - sortowanie bąbelkowe

# numbers = [4, 5, 2, 1] # to są elemnty nieposortowane
#teraz najeirw sparwdzenie czy 4>5, potem czy 5 wieksze od 2, czy
# ale to wszystsko trzeba zrobić przechodząc pętle zamianna step by step, tylko ze to jest mało wydajne
# numbers = [4, 2, 1, 5] - 1 etap
# numbers = [2, 1, 4, 5] - 2 etap
# numbers = [1, 2, 4, 5] - 3 etap

# numbers = [4, 5, 2, 1] # tą lsite chcemy posortowac
#
# swapped = True #wprowadzamy zmeinną pocniczą, czy zostało zamieniiene. Pętla się bedzie wykonywała dopóki zmienna swapped bedzie true
#
# while swapped: # robimy to w petli while, dlatego ze nie wiemy ile razy bedziemy iterowac po tyhch elem,entach, az do momnetu gdy osigniemy efekt. Tu swapped dajemy na False, zeby wyrózniła się od true
#     swapped = False
#     for i in range (len(numbers) - 1): #funkcja len słuzy do oblicznie alosci elemntów i odejmuje od tego wszytskiegpo 1
#         if numbers[i] > numbers [i+1]: # jesli bedzie wieszka musimy te pierwsze dwa elemnty czyli 4, 5 zamienic
#             numbers[i], numbers[i+1] = numbers [i+1], numbers[i]
#             swapped = True
#
# print(numbers)


# To samo, ale dla bardziej skomplikowane listy

# numbers = [4, 5, 2, 1, 3, 333333, 3, 456] # tą lsite chcemy posortowac
# #
# swapped = True #wprowadzamy zmeinną pocniczą, czy zostało zamieniiene. Pętla się bedzie wykonywała dopóki zmienna swapped bedzie true
# #
# while swapped: # robimy to w petli while, dlatego ze nie wiemy ile razy bedziemy iterowac po tyhch elem,entach, az do momnetu gdy osigniemy efekt. Tu swapped dajemy na False, zeby wyrózniła się od true
#     swapped = False
#     for i in range (len(numbers) - 1): #funkcja len słuzy do oblicznie alosci elemntów i odejmuje od tego wszytskiegpo 1
#         if numbers[i] > numbers [i+1]: # jesli bedzie wieszka musimy te pierwsze dwa elemnty czyli 4, 5 zamienic
#             numbers[i], numbers[i+1] = numbers [i+1], numbers[i]
#             swapped = True
#
# print(numbers)

# 4. Bardziej optymalna metopda sortowania - metoda SORT - od największej do najmniejszej

# numbers.sort()
# print(numbers)

# 5. Bardziej optymalna metopda sortowania - metoda SORT - od  najmniejszej do największej

# numbers.sort(reverse=True)
# # print(numbers)


# 6. Sortowanie nie liczb, ale innych elemntów, np. stringów
# letters = ["A", "C", " ", "B"]
# letters.sort()
# print(letters)

# lub sortowanie odwrocone
# letters = ["A", "C", " ", "B"]
# letters.sort(reverse = True)
# print(letters)


# 7. ORD mówi nam jakie mają wartości poszczególne elemnty w kodzie Ascii - dla duzego A i duzego C
# letters = ["A", "C", " ", "B"]
# print(ord("A"), ord("C"))
# letters.sort()
# print(letters)

# 8. ORD mówi nam jakie mają wartości poszczególne elemnty w kodzie Ascii - dla małego a i małegoo C
# letters = ["a", "a", " ", "b"]
# print(ord("a"), ord("b"))
# letters.sort(reverse = True)
# print(letters)

# 9. Lista jako typ referencyjny, czyli na podkreslienie /na większa uważność gdy bedziemy operowac na tych listach

# A. tu mamy dwie nazwy, a lista jedna
# list_1 = [9]
# list_2 = list_1
#
# list_2[0] = 13 # elemnt o innkesie 0, zminieam na 13
# print (list_2) # obie listy (1 i 2) mają teraz wartość 13
# print (list_1)


# 10. wycinanie SLising + Robienie kopii

# list_1 = [9]
# list_2 = list_1 [:]# to robi kopie całej listy, z dwukropikime
# lub

#
# list_2[0] = 13 # elemnt o innkesie 0, zminieam na 13
# print (list_2) # obie listy (1 i 2) mają teraz wartość 13
# print (list_1)
# jak widać dostaliśmy dwie osobne wartości - tu zrobilismy zabieg wycinania listy, który to zabieg tworzy odrębna kopię listy


# te wycinki=slicing robimy tak:
# numbers=[10, 8, 6, 4, 2]
# #dla liczby numers chcemy stworzyć nową listę, np. new_numbers, c bedzie wycinkiem , jakąs częscią listy numbers - i teraz mówimy co chcemy wycinać
# new_numbers = numbers[1:3]
# print(new_numbers) # nowa lista, która jest wynikime numbers
# print(numbers) # one się oczywiście nie zmieniła


 #       -5 -4 -3 -2 -1
# numbers=[10, 8, 6, 4, 2]
# # #dla liczby numers chcemy stworzyć nową listę, np. new_numbers, c bedzie wycinkiem , jakąs częscią listy numbers - i teraz mówimy co chcemy wycinać
# new_numbers = numbers[-4:-2]
# print(new_numbers) # nowa lista, która jest wynikime numbers
# print(numbers) # one się oczywiście nie zmieniła


#       -5 -4 -3 -2 -1
# numbers=[10, 8, 6, 4, 2]
# #        1  2  3   4  5
# # #dla liczby numers chcemy stworzyć nową listę, np. new_numbers, c bedzie wycinkiem , jakąs częscią listy numbers - i teraz mówimy co chcemy wycinać
# new_numbers = numbers[:len(numbers)] # to kpiuje całą listę lub można [:]
# print(new_numbers) # nowa lista, która jest wynikime numbers
# print(numbers) # one się oczywiście nie zmieniła

# 11. Usuwanie wycinków

#       -5 -4 -3 -2 -1
# numbers=[10, 8, 6, 4, 2]
# #      1  2  3   4  5
# del numbers[1:3] # wylatuje 8 i 6
    # del numbers # to usuwa całą listę!

# print(numbers)



# 12. Operatory IN oraz NOT

# numbers=[10, 8, 6, 4, 2]
#
# print (5 in numbers)# czy 5 jest w liscie numbers. WIadomo, ze nie jest wiec mamy false
# print(7 not in numbers) #st upewenieni się, że 7 nie ma w tej liscie. no wiadomo, ze nie ma , wiec mamy True



# 13. Wyrażenie listowe - list comprehension

# numbers=[10, 8, 6, 4, 2]

# A. generacje duzej listy

#definiujem,e pust ą listę i za pomocą petli for wstawiamy tam rózne elementy
# 1 Sposób
# numbers=[]
# for i in range (1, 1001):  # do 1000
#     numbers.append(i)
#
# print(numbers)

# 2 sposób, ale jednolnijokwy:
# numbers=[i for i in range (1, 1001)] # mozna to zrobić równiez jedną linijką
#
# print(numbers)

# kolejny przykład
# numbers=[99 for i in range (1, 1001)] # tu nam daje 1000 razy liczbe 99
# #
# print(numbers)

# # kolejny przykład
# numbers=[i ** 2 for i in range (1, 101)] # tu nam daje do kwadratu, do 100 elem,ntw
# #
# print(numbers)

# kolejny przykład
# numbers=[i for i in range (1, 101) if i % 2 ==0 ] # tu nam daje liczby do 100, ale tylko liczby parzyste
# #
# print(numbers)


# ZADANIE:
# chcemy dowiedziec się, ile liczb w przedziale od 1 do 300, które dzielą się przez 3 i 7 (jednocześnie)

print(len([i for i in range (1, 301)if i % 3 == 0 and i % 7 == 0])) # to nam mówi ile liczb w tym przedziale jest


numbers=[i for i in range (1, 301) if i % 3 ==0 and i % 7 == 0 ] # to nam mówi, jakie to są liczby
# #
print(numbers)
