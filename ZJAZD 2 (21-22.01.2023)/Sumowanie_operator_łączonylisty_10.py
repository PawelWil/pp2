# sumowanie wszystkich elemenmytów listy

# sum = 0
# numbers = [1,2,5,77,85,2,2,2,2,3234, 2323, 23]
#
# for e in numbers:
#     sum += e
#
# print("Suma wszystkich elementów listy", numbers, ",to: ", str(sum) + ".")


# Operatory łączone

# Czasami zachodzi potrzeba, aby zmodyfikować wartość zmiennej na podstawie dotychczasowej wartości w niej przechowywanej.
# Wyobraźmy sobie, że mamy 3 ziemniaki w garnku.
# Teraz chcemy dodać jeszcze 2 nowe ziemniaki do garnka (gdyż właśnie teściowa zapowiedziała nam się na obiad).
# Na podstawie dotychczasowej wiedzy moglibyśmy napisać:

# ziemniaki_w_garnku = 3
# ziemniaki_w_garnku = ziemniaki_w_garnku + 2
# print(ziemniaki_w_garnku)
## 5
# Jednak taki zapis jest dość barokowy, a potrzeba dość częsta, dlatego możemy równie dobrze napisać:

#a teraz poniżej z użyciem operatora łączonego:
# ziemniaki_w_garnku = 3
# ziemniaki_w_garnku += 2 # czyli mamy: ziemniaki_w_garnku = ziemniaki_w_garnku + 2
# print(ziemniaki_w_garnku)
## 5

# Operator += jest operatorem, który modyfikuje zmienną stojącą po lewej stronie,
# dodając do jej dotychczasowej wartości wartość stojącą po prawej stronie. Analogicznie mamy operatory -=, *=, /=, %=.


# def czesc():
#     print("Czesc!")
# czesc()

def czesc(imie, miasto, komunikat="Czesc"):
    print(komunikat, imie + "!")
    print("Widze, ze jestes z miasta", miasto)

czesc("Janusz", "Wroclaw")
czesc("Alicja", "Wroclaw", "Milego dnia")