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


#333 ---- Pobieranie liczb

# def get_number(number_no):  # tu definiujemy funkcję
#     print("Podaj liczbę: ", number_no, "liczbe", end=" ")
#     return int(input())
# a = get_number(1)
# b = get_number(2)
# c = get_number(3)
# print ("Pobrano liczby: ", a, b, c)


#4444
# def get_number(number_no):  # tu definiujemy funkcję
#
#     return int(input("Podaj liczbę: " + str(number_no) + "liczbe"))
# a = get_number(1)
# b = get_number(2)
# c = get_number(3)
# print ("Pobrano liczby: ", a, b, c)

#5555
# def get_number(number_no):  # tu definiujemy funkcję
#
#     return int(input("Podaj liczbę: " + str(number_no) + "liczbe"))
#
# print ("Pobrano liczby: ",get_number(1), get_number(2), get_number(3))

#66767

# def my_fun():
#     pass # to jest zaslepka, nie wiemy jak
#     # return None
# if my_fun() == None:
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
# introduce("Kowalski", "Jan") # jak widać jest wazna kolejność przekazywanych argumentów

#przekazywanie argumentow słow kluczowych
# def introduce (first_name, last_name):
#     print("czesc jestem", first_name, last_name)
# introduce(first_name="Jan", last_name="Kowalski") # i tu już zawsze bedzie ok, nawet jak te zmienne obrocimy
# introduce(last_name="Kowalski", first_name="Jan")

# # miksowanie
# def introduce (first_name, last_name):
#     print("czesc jestem", first_name, last_name)
# introduce(first_name="Jan", last_name="Kowalski")

# KOLEJNE
# def introduce (first_name="Jan", last_name="Kowalski"): # to są wartości domyślne, ale tylko się wyswietlą, wtedy gdy nie podamy wartości w introduce
#     print("czesc jestem", first_name, last_name)
# introduce() # jak tak jest to są wartiości domyslene  z góry
# introduce("Marcin", "Nowak") # jak tak to wartości domyslke są zastepowane tymi waartoscami obok
# introduce(last_name="Nowak") #tu mozemy miksowac

#KOLEJNE - return
# def introduce (first_name="Jan", last_name="Kowalski"): # to są wartości domyślne, ale tylko się wyswietlą, wtedy gdy nie podamy wartości w introduce
#     print("czesc jestem", first_name, last_name)
#     return 12
# print(introduce()) # introduce to jest ta funkcja, żeby była jasność!!!!!!!!!!!!


#SPOsoby wykorzystania:
# def count_down(wishes = True):# funkcja ktora sluzy do odliczania, czy checmu zyczenia. Program bedzie wyswietlał 3,2 ,1, 0
#     print("Trzy...")
#     print("Dwa...")
#     print("Jeden...")
#
#     if not wishes:# jesli nie chcemy to przepyszcamu
#         return
#
#     print ("Szczesliwego nowergo roku:")
#         # jesli nie checm,y to:
#
# # count_down(wishes=True) # tu dostajemy wszystko z szcesl wboweg roku
# count_down(wishes=False) # tu dostajemy tylko 1,2 ,3
#
# print (type(count_down(wishes=False))) # to pokazuje nam jaki to typ funkcji


##KOLEJNEEE:
# def sum(a, b):
#     return a + b # to nam zwraca tą wartość
# result = sum (1, 6)
#
# print (result)

# KOlejne
# def sum(a, b):
#     return a + b # to nam zwraca tą wartość
# result = sum () #  nie mozemy tak zrobić, bo muszą byc dwa warunki jqak powyzej, jak jest tak to jest błąd
#
# print (result)

