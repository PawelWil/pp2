# ctr alt l = prawidłowe ustawienie kodu!

# FUNKCJA INPUT

#   1.KONKATENACJA  - łaczymy tylko string ze stringiem, nie da się mieszać tyów , np string z intiger. Jak jest int to trza dać przed nim string
# print ("2" + "2") # tu łączę dwa stringi
# print ("2" + str(3)) # tu łącze string z int, ale przed int musze dać 'str(..)'

# 2. Funkcja INPUT
# -----
# print ("Jak masz na imię?")
# name = input () # tu wpropwadzamy imię w oknie poniżej
# print("Witaj " + name + "! Jak Ci minął dzień?")
# jak dam shift F10 (lub ctrl+shift+F10)  to muszę wpisac imię w poniższym oknie run


# -----
# number = int ("2")  # przekonwertowanie do wartości int
   # lub
# number = ("2")  # tu mamy string, czyli liczba '2' wyświetli się 5 razy
# print (number * 5) # tu jako int to mamy mnożenie, bo int to liczba

# number = "2"
# print (number * 5) # tu 2 jako string, to nie jest mnożony, ale ze string to * je powiela

# temp = float ("36.6") # tu poprzez float przed string, konwertuje to na liczbę float i jak widać konwersja sioę odbyła bo mamy 36.6
# temp = float ("36.6") #ale juz tej liczby zmiennoprzecinkowej, typu float nie moge zmienić na string, bo ma przecinek
# print (temp)

# age = 24
# print("Mam", age, "lata.") # tu 3 osobne argumenty
# print("Mam " + str(age) + " lata.") # tu mamy konkatenacje, gdzie trzy argumenty zostały połączone w jeden string, ale wiadmomo ze age jest int, to trza go zamienic na str


#----skomplikowany przykład konkatenacji
# string_number = input ("Podaj liczbę całkowitą: ") #wiadomo, ze w poniszym oknie tą liczbę muszę podać, zeby sie skrypt wykonał
# multiplier = 9
# result = multiplier * int(string_number) # tu zamieniamy na liczbę, żeby mozna otrzyman wynik mnożenia
# print("Gdy liczbę " + string_number + " pomnożymy przez " + str(multiplier) + " to otrzymamy " + str(result) + "." )


#----- Twierdzenie Pitagoarasa z uzyciem funkcji input
# a = float(input ("Wprowadz długość pierwszego boku: ")) # zeby to była wartosc zmiennoprzecinkowa=float, dajemy float żeby ta wartośc na float przekonwertować
# b = float(input ("Wprowadz długość drugiego boku: "))
# result = (a ** 2 + b ** 2) ** .5
# print ("Długość przeciwprostokątnej wynosi: " + str(result))


#-----
# OPERATOR REPLIKACJI - powtarzamy sobie jakis string tyle razy ile sobie życzymy
# print ("Ala" * 3) # tu nie jest mnozenie tylko z relpikowanie - czyli powtorzenie tego coiagu znaków tyle razy ile chcemy
    #lub
# print (3 * "Ala") # tu nie ma znaczenia z której strony damy mnozenie - może być z lewej i zprawej strony
    #lub
# print ("ala" * "ala") # nie da się replikować strin * String - replikacja działa tylko: string * intiger --> czyli w tej linii mam błąd, bo się nie zreplikuej


#-----
# RYSOWANIE prostokąta za pomoca kodów ASCII
# print ("+" + 10 * "_" + "+") # linia górna_pozioma
# print (("|" + " " * 10 + "|" + "\n") * 5, end="" ) # linie boczne_pionowe
# print ("+" + 10 * "_" + "+") # linia dolna_pozioma