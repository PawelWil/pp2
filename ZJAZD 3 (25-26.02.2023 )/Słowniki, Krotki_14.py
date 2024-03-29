# lista l = [1, 2, 3] - list -- lista charaktyryzuje się, że do elementów odwujemy sie za pomocą indeksów, jest mutowalna
# krotka t = (1,2,3) (ang. tuple) - tuple -- także charaktyryzuje się, że do elementów odwujemy sie za pomocą indeksów, ale nie jest mutowalna
# słownik d = {"a":1, "b":2} - dictionary -- słownik nie jest sekwencją, czyli nie możemy po nim przejść pętlą. Elementy są uporządkowane.
# ciąg znaków s = "asas" - string -- trochę podobny do krotki, mozna po nim iterować, ale jest niemutowalny


# KROTKI ------------------------------------------------
# krotki są niemutowalne = niezmienne-----w przeciwieństwie do list --
# czyli nie można w nich nic podmieniać, co najwyżej je kopiowac w całości lub wycinkach
# nie mozemy tez usunąc jakichs elelmentow krotki-------
# Są w nawiasach okrągłych, w przeciwienstwie do list, które są w nawiasach kwadratowych

#             0  1  2
# numbers = ( 1, 2, 3) # ta zmienna numbers, to jest krotka, nieedytowalna, w nawiasach okrągłych
#            -3 -2 -1

# numbers = 1, 2, 3 # mozna tez krotkę zapisac bez nawiasów - to jest prostszy sposób
# numbers = () # to jest pusta krotka

# numbers = (1, ) # pokazuje konkretną krotkę - ale trzeba podać przecinek - i tak będzie to pokazywane, z przecinkiem
# print (numbers) # pokazuje wszystkie krotki

# wyswietlanie wybranych elementów poprzez indeksy:
# print (numbers[0])
# print (numbers[-1])

# -- prosty przykład krotki:

# a, b = (1, 2) # krotka a, b o wartościach 1 i 2
# print(a)
# print(b)


# -- iteracja krotki----
# numbers = ( 1, 2, 3)

# for i in numbers:
#     print (i)


# #------- pokazywanie wycinków krotki / kopii jakiegoś elementu krotki + całej krotki
# numbers = ( 1, 2, 3)
# print(numbers[1:2]) # tu mamy wycinek o wartości 2, = to jest kopia tego wycinka
# print (numbers[:])# można również zrobić kopię calej krotki, poprzez znak ':'

# ----wygerenowanie krotki za pomocą generatora wyrażenia 'tuple' i pętli for - od od 0 do 9
# generator krotki, za pomocą generatora wyrażenia--------wygerenowanie krotki za pomocą generatora wyrażenia 'tuple'
# numbers = tuple(x for x in range (10)) # x dla x, który zawiera się w petli, gdzie iterujemy od 0 do 9
# print(numbers)

# krotki są niemutowalne = niezmienne-----czyli nie można w nich nic podmieniać, co najwyżej je kopiowac w całości lub wycinkach
# numbers = tuple(x for x in range (10))
# print(numbers)

# - jak widać poniżej nie można w nich nic podmieniać
# numbers = (1, 2, 3, 4)
# numbers[0] = 9999# jak widać podmiana nie działa w krotkach, czyli krotki po prostu są niezmienialne=niemutowalne
# print (numbers)# - mamy błąd "TypeError:

# nie mozemy tez usunąc jakichs elelmentow krotki-------

# numbers = tuple(x for x in range (10))

# print(numbers)
#
# del numbers[0] # nie da się usunąć elemntów krotki
# del numbers # ale da się usunąć całą krotkę

# jakie opercaje":
# 1. ile krotka ma elementów
# numbers = tuple(x for x in range (10))
# print(len(numbers))

# #2. Mnozenie, dodawanie Krotek:
# numbers = tuple(x for x in range (10))

# print(numbers * 2) # teraz mamy dwie krotki
# print (numbers + numbers)# teraz też mamy dwie krotki

# konwersja listy na krotke---------
# numbers = [1,2,3]
# numbers = tuple (numbers) # konwersja listy na krotke, za pomocą polecenia 'tuple'

# print(numbers)

# lub

# numbers = "Ala"
# numbers = tuple (numbers) # konwersja ciągu znaków na krotke - i mam ('A', 'l', 'a')

# print(numbers)


# SŁOWNIKI = zestaw, klucz, wartosc , wiadomo, że za pomocą klamerek'{}' się robi słowniki ------------------------------------------------

# phones = {"Tomek": 21312321, "Ada": 12341441, "Karol": 99999999} # numery telefonów ludzi. "Tomek"=klucz,
# zaś 21312321 = wartość (tego klucza Tomek)
# print(phones)

# WAŻnE:  klucz musi byc niepowtarzalny, bo jednoznacznie identifikuje wpis w naszym słowniku, np:---

# phones = {"Tomek": 21312321, "Ada": 12341441, "Karol": 99999999, "Tomek": 4444444444444}
# to Tomek z samego poczatku, jest podmienioony z ostatnia wartością
# print(phones)

# typowa struktura zapisu takiego słownika - jest bardziej czytelna niż w jednej linii---
# animals_dict= {
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
# }
# print (animals_dict) # tu nam wyświetla cały słownik
# print (animals_dict["kot"]) # tu wyszukujemy wartość dla konkretnyego klucza, za pomocą metody bezposredniego odwołania
# print (animals_dict.get("kot")) # tu podobnie, też wyszukujemy wartość dla konkretnego klucza, ale za pomocą metody 'get',
# i który to ostatecznie wyświetli tylko jego wartość, w naszym przypadku będzie to 'cat'
# print (animals_dict.get("krowa")) # w tym przypadku klucza 'krowa' nie ma, więc wyświetli nam 'None'
# print (animals_dict.get("krowa", "brak takiego slowa")) # w tym przypadku dzięki funkcji 'get', która ma opcję wyświetlenia czegoś,
# jak nie znajdzie danego elementu. I tak unas wiadomo 'krowy' nie ma, więc dzięki funkcji wyświetli się nam info:'brak takiego słowa'


# weryfikacja, czy istnieje jakiś konkretny klucz w słowniku, pochodzący np. z listy----------- chce dla tych kluczy sprawdzić wartości
# animals_dict = { # przykładowy słownik
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
# }
# words = ["kot", "lew", "chomik"]  # to jest lista, bo kwadratowe nawiasy, której to elementy odwołam do kluczy w słowniku
# for word in words:  # uzywam do tego pętli for- dla słowa word, w liscie 'words'
#     if word in animals_dict:  # jesli jakiś element z listy words jest w słowniku 'animals_dict', to wyświetl to słowo
# żeby ten warunek 'if' zaistniał daje 'in' + gdzie (u nas to słownik animals_dict),
# i jesli jakieś słowo jest ('word')to wyswietli go, gdyż użyłem sprytnego zapisu animals_dict[word]
#         print(word, "->", animals_dict[word])
#     else: # w przeciwnym razie
#         print("nie znaleziono slowa:", word, "w słowniku.") # to 'word' w środku mówi nam jakiego słowa nie znaleziono


# ---------- PRZESZUKIWANie SŁOWnIKA po KLUCZACH = ITEROWAnIE PO KLUCZACH-------
# animals_dict = { # przykładowy słownik
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
# }
# -- 1. za pomocą metody 'keys' wyciągam wszystkie klucze ze słownika
# for key in animals_dict.keys():
#     print(key) # a. teraz wyswietlam tylko same klucze
#     print(key, "->", animals_dict[key]) # b. teraz wyswietlam klucze wraz z ich wartościami, które wiadomo że pochodzą ze słownika
# 'animals_dict' i iterowany jest po słowie 'key' więc jego daję w nawiasie kwadratowym - bo on przechodzi przez słownik

# -- 2. Ale tez istnieje uproszczona metoda, gdzie nie trzeba dawać 'keys', python sam automatycznie to wyszuka
# for key in animals_dict:
#     print(key) # a. teraz wyswietlam tylko same klucze
#     print(key, "->", animals_dict[key]) # b.teraz wyswietlam klucze, z wartościami


# --------------WYCIGAnIE WARTOŚCI ZE SŁOWnIKA - robimy to za pomocą metody 'values'
# animals_dict = { # przykładowy słownik
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
# }
# for val in animals_dict.values(): # tu zamiast key, dajemy val, ale wiadomo, że to słowo może być całkowicie dowolne
#     print(val)


# --------------WYCIGAnIE ELEMEnTÓW ZE SŁOWnIKA w postaci KROTEK- robimy to za pomocą metody 'items'
# * tak gwoli przypomnienia, wiadomo, że krotek nie możemy modyfikować
# animals_dict = {  # przykładowy słownik
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
# }
# for item in animals_dict.items():  # tu za pomocą items, klucze i ich wartości są przedstawiane w postaci Krotek,
# czyli ciągów znaków
#     print(item)

# --------------WYCIGAnIE ELEMEnTÓW polskich i angielskich ZE SŁOWnIKA w postaci KROTEK- robimy to za pomocą metody 'items'# for pl, en
# in animals_dict.items():
# animals_dict = { # przykładowy słownik
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
# }
# for pl, en in animals_dict.items(): # dzięki elementom pl = słowo polskie i en = słowo angielskie, python nam ze słownika dosłownie wyświetli
#     słowa polskie i słowa angielskie
#     print(pl, "->", en) # tu najpierw będzie polskie słowo, potem angielskie
#     print(en, "->", pl) # zaś tu odwrotnie sobie zrobiłem przykład, czyli wpier angielskie,a potem polskie


# ---------------MODYFIKACJA SŁOWnIKA: AKTUALIZACJA(cos chcemy dodać), ZMiana nazwy WARTSCI --------

# --- aktualizacja slownika
# animals_dict= {
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
# }
# animals_dict["swinka"] = "pig" #1. tu dodajemy dodatkowy klucz z wartością, czyli klucz="swinka", a jego wartość="pig"
# animals_dict.update({"kurczak": "chicken"}) # dodanie dodatkowego klucza, można też zrobić za pomocą funcji update
# animals_dict.update({"swinka": "piggy"})# zmiana wartości klucza, na inny - też robimy za pomocą fukcji update

# print(animals_dict) # ten print wyświetla nam cały słownik po różnych modyfikacjach


# --------------------------TWORZEnIE KOPII, za pomocą metody 'copy' ---
# animals_dict= {
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
# }

# dict2 = animals_dict.copy()
# print(dict2) # tu już nam wyświetla kopię słownika 'animals_dict'

# print(animals_dict)

# -------------------------- USUWAnIe, za pomocą metody 'delay', jakiegoś konkretnego klucza---
# animals_dict= {
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
# }
# animals_dict["swinka"] = "pig"
# animals_dict.update({"kurczak": "chicken"})
# animals_dict.update({"swinka": "pigy"})

# dict2 = animals_dict.copy()

# del dict2["swinka"] # 1. tu usuwany konkretny key ze słownika, czyli usuwamy 'swinka'

# print(dict2)

# -------------------------- USUWAnIe, za pomocą metody 'popitem', tylko ostatniego klucza ze słownika---
# animals_dict= {
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
# }
# animals_dict["swinka"] = "pig"
# animals_dict.update({"kurczak": "chicken"})
# animals_dict.update({"swinka": "pigy"})

# dict2 = animals_dict.copy()

# dict2.popitem() # także jako ostatni element to 'chicken', więc on będzie usunięty ze slownika
# dict2.popitem() # jeśli to powielimy, to kolejne ostatnie elementy będziemy usuwać. Teraz usuniemy 'swinka'

# print(dict2)


# -------USUnIĘCIE WSZYSTKICH KLUCZY - czyli wyczyszczenie słownika, ale nie jego usunięcie- za pomocą 'CLEAR'
# animals_dict = {
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
# }
# animals_dict["swinka"] = "pig"
# animals_dict.update({"kurczak": "chicken"})
# animals_dict.update({"swinka": "pigy"})

# dict2 = animals_dict.copy()

# dict2.popitem()  # także jako ostatni element to 'chicken', więc on będzie usunięty ze slownika
# dict2.popitem()  # jeśli to powielimy, to kolejne ostatnie elementy będziemy usuwać. Teraz usuniemy 'swinka'

# dict2.clear() # także wyczyścił caly slownik i dostajemy pusty słownik = {}

# print(dict2)
