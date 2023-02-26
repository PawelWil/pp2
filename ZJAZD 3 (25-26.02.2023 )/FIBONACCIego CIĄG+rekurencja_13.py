# co to jest CIĄG FIBONACCIEGO: poniżej
# dwa piewrwsze elenty są równe 1, są stale, a potem kolejny elelnt jest tworzony na podtsaiwe poprzedzających - jest to suma, czyli 1, 1, 2(1+1), 3 (2+1), 5 (3+2), 8 (5+3), 13 (8+5), 21 (13+8), 34 (21+13) ....

# ZADANIE 1------- poakzanie 100 elelntu ciagu fibonacciego
# def fib(n): # n będzie nam wskazywal numer tego ciągu
#     if n < 1 :
#         return None # czyli jesli n < 1 zwracamy None, ale nie wyswietlamy :) - od razu wyswietla print
#     if n < 3: # to mozemy tez uzyc 'elif' zamiast 'if'
#         return 1
#
#     el1 = el2 = 1 # elemnt pierwszy i element drugi, wynoszą jeden. Mozna to w taki sposób zapisać
#     sum = 0
#     for i in range(3, n+1):# b tu od 3 zaczynamy wyliczać Ciąg Fibonacciego
#         sum = el1 + el2
#         el1, el2 = el2, sum # zamieniamy wartości elemntów, poprzez podmanike kolejności
#     return sum
#
# # print(fib(5)) # element 5 to pięc - ok - to tylko test
# # print(fib(8)) # to ejst elelmnt 8 - ok - to tylko test
#
# for n in range (1, 101): # to poakzuyje to 100 elelntu ciagu fibonacciego
#     print(n, "->", fib(n))




# ZADANIE 2-------tu zrobimy z uzyciem rekurencji

# przyklad 1 - funkcji rekurencji----
# def recursion(number): # to niej bedziemy podstwiac number
#     if number == 20: # taki usawiamy próg
#         return # to wyjdz z tej funkcji, zebysmy się mogli zatrzymac, bo inaczej by to szlo w nieskonconsoc
#     print (number) # wydrukuj tą liczbę
#     number += 1 #podnieś tą liczbę o 1
#     recursion(number) #wywyłaj tą liczbę rekurencyjną
#
# recursion(10)

# Teraz poakzanie 100 elelntu ciagu fibonacciego, ale z uzyciem rekurencji:-----------
# 1, 1, 2(1+1), 3 (2+1), 5 (3+2), 8 (5+3), 13 (8+5), 21 (13+8), 34 (21+13) ...
def fib(n): # n będzie nam wskazywal numer tego ciągu
    if n < 1 :
        return None # czyli jesli n < 1 zwracamy None, ale nie wyswietlamy :) - od razu wyswietla print
    if n < 3: # to mozemy tez uzyc 'elif' zamiast 'if'
        return 1

    return fib(n - 1) + fib(n-2) # suma tych elelmtów

for n in range (1, 10): # to poakzuyje to 100 elelntu ciagu fibonacciego
    print(n, "->", fib(n))

# DEBUGGER (czyli ten robak u góry) to jest opcja sledzenia krok po kroku programu, pokazuje jakie wartosci są przypisawene itd.