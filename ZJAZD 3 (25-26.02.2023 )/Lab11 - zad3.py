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

#.2 Lista figur ktore beded chcial rozmiscic losowwo:
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

