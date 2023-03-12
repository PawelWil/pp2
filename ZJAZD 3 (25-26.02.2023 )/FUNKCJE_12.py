# -- FUNKCJE--------------
# DEBUGGER (czyli ten robak u góry) to jest opcja sledzenia krok po kroku programu, pokazuje jakie wartosci są przypisawene itd.

#--- Funkcje były stosowane gdy chcieliśmu pobrac dane od uzytowniak - tworzyliśmy zmienną + za pomocą funkcji input, któr mogła być uruchomiona
# z tym argumentem, podanym przez użytkownika.
# Print, to też jest funkcja, która przekazuje argumenty, które są w nią wpisane.
# name = input("Jak masz na imie:") # Funkcja input
# print(("Witaj " + name + "!")* 100) # Funkcja print


# --- Funkcja związana z pobraniem i wyswietleniem liczb (get and show numbers) -

# Standardowy sposób:

# pobieramy od uzytkownika 3 liczby i je wyświetlimy:

# print("Podaj liczbę: ")
# a = int (input()) # tą liczbe za pomoca int rzutujemy do liczby calkowitej i wrzucamy do fukcji input!

# print("Podaj liczbę: ")
# b = int (input())

# print("Podaj liczbę: ")
# c = int (input())

# print ("Pobrano liczby: ", a, b, c)


#2 - tu to samo co powyzej, ale juz za pomocą fuckji 'def'
# def show_message():  # tu definiujemy nową funkcję, do której wrzucimy funkcję print
#     print("Podaj liczbę: ", end=" ")

# pobieramy od uzytkownika 3 liczby
# show_message()
# a = int (input()) # Prosimy o podanie za pomocą zmiennej 'a' i funkcji 'input' liczby,
# która to będzie powiązana z poleceniem pochodzącym z funkcji 'show message'="Podaj liczbę" - za nią się wyświetli wartość zmiennej 'a'
# + tą liczbe za pomoca int rzutujemy do liczby calkowitej!

# show_message()
# b = int (input())

# show_message()
# c = int (input())

# print ("Pobrano liczby: ", a, b, c)


#--- jaki atuty funkcji, np. chcemy dodać w funkcji słowo "proszę", to teraz wystarczy że w funkcji print dopisuje to słowo
# i ono się już wyświetla, we wszystkich zapytaniach, nie trzeba z osobna tego słowa 'proszę' wprowadzać. Oczywiście można również
# dodawać inne znaki, które już będą widoczne w pozostalych zapytaniach


# --- PARAMETRYZOWAnIE FUnKCJI:
# def show_asteriks(how_many): # to jest parametryzowanie funkcji - nasz parametr = how_many + podajemy wartość tego parametru
                                # podczas wywołania funkcji(poniżej),czyli np. (10), (1212) itd. i dzięki temu parametrowi wyświetlamy *
                                # tą zadaną ilość razy
    # print("*" * how_many)

# show_asteriks(10)
# show_asteriks(1212)


# --- ulepszenie programu 1
# def show_message():
#     print("Proszę podaj liczbę: ", end=" ") # tu dodajemy to słowo 'proszę' i jak widzimy na już mamy zapytanie ze słowem 'proszę'

# pobieramy od uzytkownika 3 liczby
# show_message()
# a = int (input()) # wytłumaczenie znaczenia zmiennej a i b i c powyżej!

# show_message()
# b = int (input())

# show_message()
# c = int (input())

# print ("Pobrano liczby: ", a, b, c)


# --- ulepszenie programu 2
# def show_message(number_no):
#     print("Proszę podaj", number_no, "liczbę: ", end=" ") # tu dodajemy to słowo 'proszę' i jak widzimy na już mamy zapytanie ze słowem 'proszę'

# pobieramy od uzytkownika 3 liczby
# show_message(1) # tu teraz do fukcji show_message podajemy argument number_no = 1
# a = int (input()) # wytłumaczenie znaczenia zmiennej a i b i c powyżej!

# show_message(2) # tu teraz do fukcji show_message podajemy argument number_no = 2
# b = int (input())

# show_message(3) # tu teraz do fukcji show_message podajemy argument number_no = 3
# c = int (input())

# print ("Pobrano liczby: ", a, b, c)



#333 ------- Pobieranie liczb

# def get_number(number_no):  # tu definiujemy funkcję, która będzie pobierała od razu ten numer
#     print("Podaj liczbę: ", number_no, "liczbe", end=" ")
#     return int(input())
# a = get_number(1) # funkcja 'get_number' realizuje dwie rzeczy: 1)wyswietla etykiete korzystajac z argumentów które przekazujemy ,
# 2)pobiera ją od uzytkowina i zwraca za pomoca funckji return
# b = get_number(2)
# c = get_number(3)
# print ("Pobrano liczby: ", a, b, c)


#333'
# def get_number(number_no):  # tu powyzsze jeszcze skracamy, czyli bez print, od razu w jednej linii z return
    # + na koniec  drukowanie poprzez print

    # return int(input("Podaj liczbę: " + str(number_no) + "liczbe")) #
# a = get_number(1)
# b = get_number(2)
# c = get_number(3)
# print ("Pobrano liczby: ", a, b, c)

# 333''--lub jeszcze większe uproszczenie, jak poniżej:

# def get_number(number_no):  # tu definiujemy funkcję

    # return int(input("Podaj liczbę: " + str(number_no) + "liczbe "))

# print ("Pobrano liczby: ",get_number(1), get_number(2), get_number(3))


#--- Kolejny przyklad na zwracanie funkcji 'NONE'
# def my_fun(): # ta funkcja bedzie zwracała wartosc 'none'
# pass # to jest zaslepka, jak nie wiemy co nasz skrypt bedzie wykonywał
#     return None #1) - albo bedzie spełniony ponizszy warunek 'if', bo mamy przypisaną wartość 'none'
#     return 123 #2) - albo jesli damy zeby coś zwrociła, np 123, a nie nic=none, to wiadomo, że w tym przypadku nic się nie wyswietli,
# bo ten poniższy warunek if nie zostanie spełniony, czyli wyswietli się komunikat: Process finished with exit code 0
# if my_fun() == None: # jesli funkcja zwraca wartosc 'none', czyli nic, to dajemy oczywiscie, ze nic nie zwraca
#     jesli cos damy, to wiadomo, ze nie da komunikatu 'nic nie zwraca'
#     print("Funkcja na razie nic nie zwraca")


# Różnica pomiędzy funkcją 'print', a 'return'

# def my_name():
#     return "Marcin" # ta funkcja zwracca jakas  wartość, ale nie drukuje nic
#
# def show_my_name():
#     print("Marcin") # ta funkcja zwraca jakas  wartość i drukuje coś

#Test z Return
# redefine =  my_name()# jak widać return poprzez funkcje my_name nie zwraca nic
# print (redefine * 10) # zeby zwrocic za pomocą return, trzz go wywolać poprzez print

#Test z Print
# redefine = show_my_name() # tu jak widzimy od razu zwraca wartość


# ZADANIE - robimy asterisks

# definiujemy sobie funkcję
# def show_asterisks(how_many):
#     print("*" * how_many)
#
# show_asterisks(10)
# show_asterisks(50)

# Kolejne zadanie
# def show_message(number_no):
#     print("Proszę podaj", number_no, "lizbe:", end= " ")

# show_message
# show_asterisks(50)

# przekazayanie parametrów pozycyjnych:
# print ("raz", "asD" , "trzy") --cos nie dziala...


#KOlejny przyklad
# def introduce (first_name, last_name):
#     print("czesc jestem", first_name, last_name)
# introduce("Jan", "Kowalski")
# introduce("Kowalski", "Jan") # jak widać jest wazna kolejność przekazywanych argumentów, bo jak je odwrócimy, to
# będą wyświetlane na odwrót

#przekazywanie argumentow słow kluczowych
# def introduce (first_name, last_name):
#     print("czesc jestem", first_name, last_name)
# introduce(first_name="Jan", last_name="Kowalski") # i tu już zawsze bedzie ok, nawet jak te zmienne obrocimy, bo do argumentów na sztywno
# przypisujemy jakąś wartość, czyli do argumentu 'first_name' na sztywno dajemy Jan ', a z racji, ze w funkcji ten argument jest jako pierwszy
# to zawsze będzie wyswietlany, jako pierwszy, nawet gdy zaczniemy od argumentu drugiego 'last_name'=Kowalski
# introduce(last_name="Kowalski", first_name="Jan")

# # --- miksowanie argumentu zafiksowanego na sztywno, oraz wartości bez podanego przypisanie do argumentu:
# def introduce (first_name, last_name):
#     print("czesc jestem", first_name, last_name)
# introduce("Jan", last_name="Kowalski") # i tak to działa, ale WAŻnA rzecz: zawsze na koncu musi być ostatni argument,
# czyli last name, jak będzie przed, to wyskoczy błąd (przykład z błędem poniżej)
# introduce("Kowalski", first_name="Jan") #jest źle-- Typ błędu: introduce() got multiple values for argument 'first_name'
# introduce(last_name="Kowalski", "Jan") # jest źle-- Typ błedu: positional argument follows keyword argument

#---- KOLEJNE - tu już do funkcji intrduce, do jej argumentów, od razu można podać wartości domyślne, nie dodawać ich później,
# mowa o wartości 'Jan' i 'Kowalsi', jako wartości domyślne
# def introduce (first_name="Jan", last_name="Kowalski"): # to są wartości domyślne, ale tylko się wyswietlą, wtedy gdy nie podamy wartości w introduce
#     print("czesc jestem", first_name, last_name)
# introduce() # 1 sposób wyświetlania: wtedy jak mamy te wartości domyślne, to samo puste wywołanie funkcji 'intrduce'
# pokazuje nam wartiości domyslne  wpisane z góry

# introduce("Marcin", "Nowak") #  2 sposób: ale nie stoi nic na przeszkodzie, żeby te wartości domyslke mogły być zastepowane
# innymi wartościami, mimo tego, że są na sztywno wprowadzone - w naszym przypadku: 'Jan' zastąpiony przez 'Marcin' + 'Kowalski' przez 'NOWAK'

# introduce(last_name="Nowak") # 3 sposób: tu mozemy miksowac, poprzez podanie zafiksowanego argumentu, np. last_name="Nowak", bez podania
# 'first_name', gdzie wiadomo, że first name zostało zafiksowane jako Jan, więc w sumie będzie Jan Nowak



#KOLEJNE ----- ZWRACAnIE WARTOŚCI przez funkcję: "return"
# def introduce (first_name="Jan", last_name="Kowalski"): # to są wartości domyślne, ale tylko się wyswietlą, wtedy gdy nie podamy wartości w introduce
#     print("czesc jestem", first_name, last_name)
    # return 12
    # return  None
    # poprzez funkcję zwracania 'return', która w naszym przypadku jest przypisana do funcji'introduce', nasz faunkcja 'introduce'
    # poprzez funkcje 'return' będzie zwracała '12' lub "NONE', ale będzie zwracała dopiero, jak się wywoła funkcję drukującą,
    # czyli funkcję 'print', która wydrukuje oczywiście: ("czesc jestem", first_name, last_name) + wartość z funkcji return
# print(introduce()) # introduce to jest ta funkcja, żeby była jasność!!!!!!!!!!!!


#SPOsoby wykorzystania: funkcja, która będzie odliczła i pytała, czy chcemy życzenia -- parametr 'wishes'
# def count_down(wishes = True):# funkcja ktora sluzy do odliczania, czy checmu zyczenia. Program bedzie wyswietlał 3,2 ,1, 0
#     print("Trzy...")
#     print("Dwa...")
#     print("Jeden...")

    # if not wishes:# jesli nie chcemy życzeń, to dajemy if not
    #     return

    # print ("Szczesliwego nowergo roku:")

# count_down(wishes=True) # 1 sposób wyswietlenia, gdy wartośc argumemtu jest true: tu dostajemy wiadomo odliczanie, z życzeniami 'szczesliwego nowego roku'wszystko z szcesl wboweg roku
# count_down((True))
# count_down(wishes=False) # 2 sposób wyswietlenia, gdy wartośc argumemtu jest false:  tu dostajemy tylko 1,2 ,3, bez zyczen

# print ((count_down(wishes=False))) # tu za pomocą funkcji drukującej, widzimy, że funkcja 'return' zwraca 'nic'='none'
# + oczywisćie drukuje "trzy", "dwa", "jeden"

# print (type(count_down(wishes=False))) # to pokazuje nam jaki to typ funkcji, czyli klasa/typ - 'none' type


##----KOLEJNEEE: przykład z sumowaniem - bedzie miał funkcje, która będzie sumowała
# def sum(a, b): #bedzie miał funkcje 'sum', która będzie sumowała + będzie przybierała 2 wartości a i b + bedzie zwracała 'a+b' poprzez funkcje return
#     return a + b # poprzez funkcję 'return' będzie nam zwracana wartość a+b, bezposrednio za pomocą zmiennej 'result'
# result = sum (1, 6) # do zmiennj result podtsawimy to co zwrói funkcja sum - czyli sumujemy 2 liczby, a=1 i b=6
# i na koncu wyswietlimy co wyswietlilismy jako suma, w zmiennej result

# print (result)

# --KOlejne - powiązane z powyższym - mowa, że musimy podać wszystkie argumety, jak nie podamy nic albo nawet braknie jednego,
# to wtedy wywali nam błąd
# def sum(a, b):
#     return a + b # to nam zwraca tą wartość
# result = sum () #  nie mozemy tak zrobić, bo muszą byc dwa warunki jak powyzej, jak jest tak to jest błąd
# result = sum (1) # nie mozemy tak zrobić, bo muszą byc dwa warunki jak powyzej, jak jest tak to jest błąd
# print (result)

