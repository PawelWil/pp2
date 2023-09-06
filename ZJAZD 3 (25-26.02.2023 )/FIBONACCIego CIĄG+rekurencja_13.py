# co to jest CIĄG FIBONACCIEGO: poniżej
# dwa pierwsze elementy są równe 1, które są stale, a potem kolejne elementy są tworzone na podstawie poprzedzających -
# jest to suma, czyli: 1, 1, 2(1+1), 3 (2+1), 5 (3+2), 8 (5+3), 13 (8+5), 21 (13+8), 34 (21+13) ....


# ZADANIE 1------- pokazanie 100 elementów ciagu fibonacciego
def fib(n): # zdefiniujemy funkcje 'fib', podamy w tej funkcji parametr 'n' który będzie nam wskazywal
# numer tego ciągu/wartość danego elementu ciągu fibonacciego
    if n < 1: # jesli ktos poda liczbę mniejszą od 1, to się nic nie uda i zwracane za pomocą if będzie NONE
        return None # czyli jesli n < 1 zwracamy None, ale nie wyswietlamy :) - od razu wyswietla print
    if n < 3: # tu mozemy tez uzyc 'elif' zamiast 'if'# tu mamy mniejsze od 3 - czyli w momencie jezeli ktoś podstawi 1,
#     to jak wiemy jest pierwszy i drugi element ciagu fibonacciego, czyli jest równy 1 i zwrócone będzie 1 (funkcja return poniżej)
#     Jest to ustawienie na sztywno.
        return 1

    el1 = el2 = 1 # elemnt pierwszy i element drugi, wynoszą jeden. Mozna to w taki sposób zapisać. To jest sytuacja startowa
    sum = 0 # zmienna pomocnicza, która wynosi 0
    for i in range(3, n+1):# a teraz w pętli for, w zakresie od 3 do n+1=kolejne element, zgodny z funkcją range-musi się
# zwiększać (bo wiadomo, że nie interesuje nas ani element pierwszy, ani drugi,
#     które na sztywno w ciągu fibonacciego mają 1) dojeśli ktoś poda więcej niż 1 dla elementy od b tu od 3 zaczynamy
#     wyliczać Ciąg Fibonacciego
        sum = el1 + el2 # nasza suma to el1 + el2 -- jak tu zaczynamy od el3 to el1 + el2 da nam ten el 3
        el1, el2 = el2, sum # zamieniamy wartości elemntów, poprzez podmanike kolejności, gdzie po znaku =, el2 wskoczy na pierwszą
#         pozycję, za el1 przejdzie w sum (która się równa el1 + el2)
    return sum # i zwraca sumę, na bazie której dojdziemy do elementu, który nas interesuje

print(fib(5)) # wyświetl element 5 = który jest równy pięc - ok - to tylko test! - na b
print(fib(6)) # to jest element 6, który się równa 8 - ok - to tylko test!

for n in range (1, 101): # teraz pokazujemy wszystkie elemnty fibonacciego od 1 do 100, za pomocą funkcji for
    print(n, "->", fib(n)) # "->" - to jest element graficzny, który przekirowuje do konkretnego elementu ciągu fibonacciego




# ZADANIE 2-------tu zrobimy to co powyżej, ale z uzyciem rekurencji

# 1---- Prosty przyklad funkcji z uzyciem rekurencji----
# def recursion(number): # do tej funkcji 'recursion' bedziemy podstawiac do argumenty 'number' jakąś wartość
#     if number == 20: # taki ustawiamy próg, czyli 20, żeby się zabezpieczyć, że będzie liczyło do 20, czyli to jest próg,
#     po osiągnieciu którego wychodzimy z tego, żeby można było się kiedyś zatrzymac, a nie liczyło w nieskonczoność
#         return # to wyjdz z tej funkcji, zebysmy się mogli zatrzymac, bo inaczej by to szlo w nieskonconsoc
#     print (number) # wydrukuj tą liczbę
#     number += 1 #podnieś tą liczbę o 1 - czyli wchodzimy za kazdym razem do srodka, tak jak matrioszki
#     recursion(number) #wywyłaj tą liczbę rekurencyjnie = dzięki temu mamy rekursje, czyli funkcja w funkcji,
#     czyli tych funkcji rekurencyjnych mamy 20, bo 1 jest 2, 2 w 3, itd.

# recursion(10)

# 2----- Teraz pokazanie 20 elementów ciagu fibonacciego, z uzyciem rekurencji:-----------
# 1, 1, 2(1+1), 3 (2+1), 5 (3+2), 8 (5+3), 13 (8+5), 21 (13+8), 34 (21+13) ...
# def fib(n): # w funkcji 'fib' argument 'n' będzie nam wskazywal numer tego ciągu
#     if n < 1 : # jesli ktos poda liczbę mniejszą od 1, to się nic nie uda i zwracane za pomocą if będzie NONE
#         return None # czyli jesli n < 1 zwracamy None, ale nie wyswietlamy :) - bo wyswietla print, a return zapamietuję tą dana
#     if n < 3: # to mozemy tez uzyc 'elif' zamiast 'if'
#         return 1

    # return fib(n - 1) + fib(n-2) #

# for n in range (1, 20): # to poakzuyje do 10 elementu ciag fibonacciego
#     print(n, "->", fib(n))

# DEBUGGER (czyli ten robak u góry) to jest opcja sledzenia krok po kroku programu, pokazuje jakie wartosci są przypisawene itd.