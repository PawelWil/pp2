# Jak przechowywać wiele wartości, np. 5 liczb całkowitych:
# a = 3
# b = 4
# c = 6
# d = 11
# e = 99

# # print(a,b,c,d,e)# jak wyświrtlic te liczby - ale to jest tylko do małej liczby, przy liscie danych 1000 to już byłby problem, dlatego korzystamy z ponizszego rozwiązania
# numbers = [2, 4, 8, 11, 99, 10, 10]
# print(numbers)
#           0       1           2       3     4  --> to jest rozpisanie, pod jakimi indeksami kryją sie poniższe owoce
# fruits = ["banan", "kiwi", "czereśnia", 99, True] # lista moze przechowaywac rózne typy znaków, string, int, bools(wartość logiczna) itd.
#           -5      -4          -3      -2    -1 --> to jest indfeksowanie ujemne
# print(fruits)
#
# print(fruits[0]) # banan to jest zerowy indeks i indeksy jak powyżej - indeksowanie dodatnie
# print(fruits[-5]) # indeksowanie ujemne


# 1. ----PRZYKŁAD
# przechowywanie pól dolarówek w Denver
# liczba produkcji monet poldolarypwych w latach 2012, 2013, 2014, w Denver i Philadelphi
#w denver było wyprodukowanych 1_700_000, w kolejnym roku 4_600_000, a wkolejnym 2_100_000
#w philadelphi wypodukowanych 1_800_000, w kolejnym roku 5_000_000, a w kolejnym 2_500_000
# denver = [1_700_000, 4_600_00, 2_100_000]
#
# philadelphia = []
# philadelphia.append (1_800_000) # to jest inny sposób takiego zapisu, jak powyzej odnosmnie Denver
# philadelphia.append (5_000_000)
# philadelphia.append (2_500_000)
#
# total = [0, 0, 0]
# total[0] = denver[0] + philadelphia[0]
# total[1] = denver[1] + philadelphia[1]
# total[2] = denver[2] + philadelphia[2]
#
# average = (total[0] + total[1] + total[2]) / len(total) # teraz liczymy średnią
#
# print("Produkcja w roku 2012 wyniosła: ", total[0], "sztuk") # rok 2012 skrywa się w indeksie [0]
# print("{:,d}".format(total[0]).replace(","," ")) # Formatowanie powyższych zapisów (opcjonalne), żeby było ładnie
# print("Produkcja w roku 2013 wyniosła: ", total[1], "sztuk") # rok 2013 skrywa się w indeksie [1]
# print("{:,d}".format(total[1]).replace(","," ")) # Formatowanie powyższych zapisów (opcjonalne), żeby było ładnie
# print("Produkcja w roku 2014 wyniosła: ", total[2], "sztuk") # rok 2014 skrywa się w indeksie [2]
# print("{:,d}".format(total[2]).replace(","," ")) # Formatowanie powyższych zapisów (opcjonalne), żeby było ładnie


# 2. USUWANIE
# fruits = ["banan", "kiwi", "czereśnia", 99, True]
# print(fruits)
# del fruits[-1] # tu nam usuwa indeks [-1]
# del (fruits[-1]) # może być z okrągłymi nawiasami po del -> jest bardziej czytelne, ale nie musi
# print (fruits)
#
# # 3. Rozróżnienie między funkcją - LEN - pokazuje ile elementów jest schowanych w danej liście - w tym przypadku mowa o liście 'fruits'
# l = len(fruits)
# print(l) # albo tak
# print(len(fruits)) #albo tak
#
# # 4. Metoda APPEND + INSERT - dodanie konkretnych elementów
#
# fruits.append("jabłko") # metoda Append dodaje element, zawsze na koniec listy
# print(fruits)

# fruits.insert(0, "gruszka")# mozemy tez dodawać za pomocą INSERT - w tej metodzie trza podać, na które miejsce _pod jaki indeks ma być wrzucony dodatkowy element - w naszym przypdaku to jest indeks 0, czyli peirwszy, na którym będzie dodany element 'gruszka'
# print(fruits)


# ---------- 5. JAK ITEROWAĆ=sprawdzac co mamy, po LISTACH - jak się poruszać

  # I SPOSÓB
# fruits = ["banan", "jabłko", "czereśnia"]
# for i in range(len(fruits)):
    # print(fruits[i]) # to jest iterowanie pionowe, bo nie ma end = ' '
    # print(fruits[i], end=" ") # to jest iterowanie poziiome, bo jes end = ' '

  # II SPOSÓB
# fruits = ["banan", "jabłko", "czereśnia"]
# for f in fruits:
#     print(f)
