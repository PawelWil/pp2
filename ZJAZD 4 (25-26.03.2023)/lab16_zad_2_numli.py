## ZADANIE 2 - LAB 16

# Napisz, przetestuj i zastosuj własny moduł do obsługi list liczb całkowitych:
# • stwórz modułu o dowolnej nazwie,
# • dodaj funkcję weryfikującą czy podana lista zawiera wyłącznie liczby całkowite,
# • dodaj funkcję sumującą wszystkie liczby z listy,
# • dodaj funkcję zwracającą iloczyn wszystkich liczb z listy,
# • dodaj testy weryfikujące poprawne działanie napisanych funkcji,
# • zaimportuj utworzony moduł i skorzystaj z jego funkcji.


# • stwórz moduł o dowolnej nazwie
# moduł tworze poprzez utworzenie nowego katalogu. W tym przypadku to jest 'Lab 16 - zad2'

# • dodaj funkcję weryfikującą czy podana lista zawiera wyłącznie liczby całkowite,

def is_list_of_integers(list): # tworzymy funkcje is_list_of integers, ktora zweryfikuje czy podana lista zawiera tylko liczby całkowite
    for i in list: # teraz za pomocą pętli for iterujemy każdy element listy (i), sprawdzamy czy dany element jest typem int
        if not isinstance (i, int):# tu sprawdzamy na bazie, czy nie jest
            return False # i jak nie jest typem int to zwraca nam false. Jesli jest to dochodzimy do 'True'
    return True



# • dodaj funkcję sumującą wszystkie liczby z listy,
def sum_list(list): # nazywamy funkcję sum_list, w której podajemy argument nasz listy 'list'
    sum = 0 # potrzebujemy zmienną lokalną, która na początku będzie równa 0, do której będziemy dodawać wszystkie elementy z listy-
    # jak poniżej
    for i in list:
        sum += i
    return  sum



#• dodaj funkcję zwracającą iloczyn wszystkich liczb z listy - wiadomo, że te liczby musimy przez siebie przemnożyć
def product_list(list):
    product = 1 # nasz iloczyn zaczniemy od zmiennej ustawionej na 1, nie na 0, bo jakbyśmy dali 0, to wiadomo, że każde mnożenie,
    # konczyłoby się wynikiem 0
    for i in  list:# i teraz iterujemy dla wszystkich elementów listy
        product = product * i
    return product # zwracamy sobie wynik iloczynu



# • dodaj testy weryfikujące poprawne działanie napisanych funkcji,
if __name__ == "__main__": # sprawdzamy czy własciwość name jest równa napisowi 'main' - jesli tak tzn. że ktoś uruchamia nas modul
    list = [1,2,3] # teraz dajemy proste dane testowe, żeby pokazać, że wszystko działa dobrze
    print(is_list_of_integers(list) == True) # sparwdzamy, czy ta nassza lista jest listą  liczb całkowitch - jeśli tak to wiadomo true
    print(is_list_of_integers(["a", "b", "c"]) == False) # jeśli będzie string to false
    print(sum_list(list) == 6) #  To wyświetlenie jest do funkcji sumującej 'sum' = jest true bo suma z listy jest równa 6
    print(sum_list(list) != 7) # dla sprawdzenia, czy funkcja działa prawidłowo, sprawdzam, czy suma w liscie 'list' jest różna od 7
    # odpowiedz jest prawidłowa, bo wyświetla nam True.
    print(product_list(list) == 6) # tu sprawdzamy czy ilo liczb w liście 'list' jest równy 6 - jest true - więc ok
    print(product_list(list) != 99) # tu jeszcze weryfikujemy, czy błedny wynik podany jako różnica, też da nam true-dało, więc tez jest ok



