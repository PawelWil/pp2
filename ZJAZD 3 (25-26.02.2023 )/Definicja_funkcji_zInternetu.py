#
#     # https://pl.wikipedia.org/wiki/Funkcja
#
# # Definicja i wywołanie funkcji
#
# # Funkcja to wydzielona część programu wykonująca pewne operacje.
# Nazwa funkcji ma istotne znaczenie, określa ona czynność, którą dana funkcja wykonuje.
# Poprzez użycie odpowiedniej nazwy można wywołać konkretną funkcję, czyli wykonać kod w niej zapisany.
#
# # Dobrze napisana funkcja wykonuje tylko jedną czynność.
#
# Tworzenie funkcji w języku Python rozpoczynamy od słowa kluczowego def.
# Zaraz po nim następuje nazwa funkcji, nawiasy okrągłe oraz dwukropek.
# Przypomnijmy: dwukropek na końcu linii oznacza, że w kolejnej linii następuje odpowiednio wcięty blok kodu złożony
# z co najmniej jednej linii.
#
# def czesc():
#     print("Czesc!")
# czesc() #to musi być żeby tą funkcję wywołać
#

# Każdy blok kodu powinien zawierać dokładnie cztery spacje.
# Jest to wymaganie określone w dokumencie PEP 8, do którego zaleceń stosują się programiści Pythona.


# Przekazywanie argumentów
#
# Parametry funkcji umieszczane są w nawiasach okrągłych umieszczonych za nazwą funkcji.
# Argumenty przekazujemy w nawiasach okrągłych podczas wywoływania funkcji.
#
# def czesc(imie):
#     print("Czesc" + imie + "!")
# czesc("Janusz")
#
# Podczas przekazywania argumentu możemy również podać nazwę parametru.
#
# def czesc(imie):
#     print("Czesc " + imie + "!")
# czesc(imie="Janusz")
#

# Pytanie
# Załóżmy, że mamy funkcję przyjmującą dwa parametry: imie oraz miasto.
# Czy korzystając z nazw parametrów możemy zmienić kolejność ich występowania?
#
# def czesc(imie, miasto):
#     print("Czesc " + imie + "!")
#     print("Widze, ze jestes z miasta", miasto)
# czesc(miasto="Wroclaw", imie="Janusz")
# Odpowiedź: Tak.
#

# Pytanie
# Załóżmy, że mamy funkcję przyjmującą dwa parametry:: imie oraz miasto.
# Czy program zadziała dobrze, gdy przekażemy argumenty ze zmienioną kolejnością nie podając nazw parametrów?
#
# def czesc(imie, miasto):
#     print("Czesc " + imie + "!")
#     print("Widze, ze jestes z miasta", miasto)
# czesc("Wroclaw", "Janusz")
# Odpowiedź: Nie.


# Przekazywanie argumentów - Argumenty domyślne
#
# Dla parametrów funkcji można ustanowić pewne konkretne wartości, nazywamy je argumentami domyślnymi.
#
# Argumenty domyślne pozwalają wywołać funkcję bez podawania jednego lub większej liczby argumentów.
#
# def czesc(imie, miasto, komunikat="Czesc"):
#     print(komunikat, imie + "!")
#     print("Widze, ze jestes z miasta", miasto)
# czesc("Janusz", "Wroclaw")
# czesc("Alicja", "Kraków", "Milego dnia")
#

# Pytanie
# Czy argument domyślny możemy przypisać do parametru miasto?
# Innymi słowy, czy dowolny parametr bez podanego argumentu domyślnego może znajdować się za parametrami z argumentami
# domyślnymi?
#
# def czesc(imie, miasto="Wroclaw", komunikat):
#     print(komunikat, imie + "!")
#     print("Widze, ze jestes z miasta", miasto)
# czesc("Alicja", "Milego dnia")
# Odpowiedź: Nie.


# Zwracanie wartości
# Z czasem stopień skomplikowania naszych funkcji rośnie, ich zadaniem będzie wykonanie pewnych obliczeń i zwrócenie wyniku.
#
# Wartości z funkcji zwracane są przy pomocy słowa kluczowego return.
#
# def dodawanie(a, b):
#     z = a + b
#     return z
# wynik = dodawanie(2, 3)
# print("Wynik:", wynik)


# Pytanie
#
# Co to znaczy zwrócić wartość z funkcji?
# Odpowiedź: Bardzo ogólnie możemy powiedzieć, że zwrócenie wartości oznacza podstawienie obliczonego wyniku
# (wartości wskazanej słowem return) w miejsce wywołania funkcji.
#
# Wartości zwracane z funkcji nie muszą być tylko liczbami. Funkcje mogą zwracać dowolne obiekty
# (np. listy, krotki, słowniki).

#

# Przekazywanie argumentów
#
# Funkcje w języku Python mogą przyjmować dowolnie wiele argumentów. W tym celu został opracowany specjalny parametr
# *args przechowujący dodatkowe nienazwane argumenty przekazane do funkcji.
#
# Nazwa args jest umowna.
#
def czesc(imie, *args):
    print("Czesc " + imie + "!")
    for s in args:
        print("Czesc " + s + "! (args)")
czesc("Janusz", "Maciej", "Mateusz")
#
# Dostępny jest także parametr **kwargs przechowujący dodatkowe nazwane argumenty przekazane do funkcji.
# kwargs jest słownikiem, gdzie kluczem jest nazwa parametru, a wartością przekazany argument.
#
# Nazwa kwargs jest umowna.
#
# def czesc(imie, **kwargs):
#     nazwa = imie
#     if "nazwisko" in kwargs:
#         nazwa = nazwa + " " + kwargs["nazwisko"]
#     print("Czesc " + nazwa + "!")
#
# czesc("Janusz")
# czesc("Anna", nazwisko='Nowak')
#
