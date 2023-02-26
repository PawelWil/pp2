# DEBUGGER (czyli ten robak u góry) to jest opcja sledzenia krok po kroku programu, pokazuje jakie wartosci są przypisawene itd.

#1. jak wspoładziaja listy razem z funkcjami-----------
# definiujemy funkcje
def sum_numbers(numbers): # to co jest w nawiasie to są parametry tej fukcji, tutja to zmienna 'numbers'
    sum = 0
    for element in numbers: #teraz korzystamy z petli, ktora to ziinna dostanie kolejne lelemty, któr bedzizemy iteroiwac, dla nas to lista, czyli dopisz/dodaj ten elemnt
        sum += element
    return sum

numbers = [1,2,3]# to jest zmienna globalna 'numbers'
result = sum_numbers(numbers)
print (result)



# 2. Funkcja ktora generuje lsoowo liczby w zakresie od 0 do 99---------

# import random
#
# def generate_numbers(total_numbers):
#     numbers = []# zmienna lokalna
#     for i in range (total_numbers): #  czyli tyle razy bedziemy przez tą pętlę przechodizc
#         numbers.append(random.randint(1, 99))
#     return numbers #zwrcamay nasza listę numbers poprzez return
#
# print (generate_numbers(10)) # wylosuj nam 10 liczb i pokaz na ekranie, i te wszystie liczby są w zakresie od 0 do 99
# print (generate_numbers(100))
# print (generate_numbers(123233))


# 3. Zasieg zmiennych--------
# przyklad 1
# def scope_test (): # ma jedną zmienną lokalką x - to jest x poniżej
#     x = 123
# scope_test() # to jest uruchomienie tej funkcji - dzuiala ale sie nic nie pojawia , bo retiurn zwraca wartosc, a nie pokazjuje jak print
# print(x) # tak nam nie wyswietli bo print jest uznawany jako globalny i tu bedzie error

# przyklad 2---------
# def scope_test (): # ma jedną zmienną lokalką x - to jest x poniżej
#     print(" wsrodku funkji:" + str(x))
#
# x = 99 # zmienna globalna 99
# scope_test() # jak to uruchmimy tą funkcje poprzez scope_test i mamy u gory print, to jak widać te 99 się pokazało

# # przyklad 3-------
# def scope_test (): # ma jedną zmienną lokalką x - to jest x poniżej
#     x=123 # zmienna lokalna
#     print(" wsrodku funkji:" + str(x)) # to wyswietla niezaleznie dla globalnej lokalnej x = 123
#
# x = 99 # zmienna globalna 99
# scope_test() # jak to uruchmimy tą funkcje poprzez scope_test i mamy u gory print, to jak widać te 99 się pokazało
# print(" na zewnatrz: " + str(x)) # to wyswietla niezaleznie dla globalnej zmiennenn x = 99


# przyklad 4 - tu wplywamy na zmienną globalną i znienić ją w ciele funkcji---------
# def scope_test ():
#     global x # zeby to zrobić trezba uzyc instrukcji global, która zacznie traktować zmienną x, nawet lokalnie/wewntarz bedzie traktować jako globalną
#     x=123 # zmienna lokalna
#     print(" wsrodku funkji:" + str(x)) # to wyswietla niezaleznie dla globalnej lokalnej x = 123
#
# x = 99 # zmienna globalna 99
# scope_test() # jak to uruchmimy tą funkcje poprzez scope_test i mamy u gory print, to jak widać te 99 się pokazało
# print(" na zewnatrz: " + str(x)) # po uzyciu instrukcji globalnej jak widać wyswiretla się  x = 123.


### ZDefiniowanie fukcji, ktorej zadaniem jest zmiana wartości---------

# def change_value(n):# do tej funkcji przekazujemy argument n - mowa o wartosciach skalarnych, czyli liczby (int, float) --> tu n = val
#     print ("przed zmiana:", n)
#     n+= 1
#     print("po zmianie", n)
#
# val = 7 # do tej zmiennej globalnej przeakuzjemy wartos c int = 7
# change_value(val) # za pomocą tej change_value mozemy zmienić wartość listy 'val=[1,2] - i następnie program przekazuje do piewrszej linii , tak gdzie funkcja def jest opisana , nawet jak jest n ale tu już jest val i to wchodzi zamiast n
# print(val)


## przekazujemy listę - jakas wartość nieskalarna------------
# def change_value(n):# do tej funkcji przekazujemy argument n - tu nieskalarna, czyli lista --> tu n = val
#     print ("przed zmiana:", n)
#     n = [0,0] # pod n podstawilismy całkeim inny pbiekt, ale lokalnie, który ma pierwszenstow nad globalną, dlatego [1,2], zostało zastąpione [0,0]
#     print("po zmianie", n)
#
# val = [1,2] # do tej zmiennej globalnej przeakuzjemy liste
# change_value(val) # za pomocą tej change_value mozemy zmienić wartość listy 'val=[1,2] - i następnie program przekazuje do piewrszej linii , tak gdzie funkcja def jest opisana , nawet jak jest n ale tu już jest val i to wchodzi zamiast n
# print(val)

## Kolejny przyklad - zmien wartosc listy i podstwa wartos 999--------------
# def change_value(n):# do tej funkcji przekazujemy argument n - tu nieskalarna, czyli lista --> tu n = val
#     print ("przed zmiana:", n)
#     n[0] = 999 # tu bedziemy miec: [999, 2] pod n podstawilismy całkeim inny pbiekt, ale lokalnie, który ma pierwszenstow nad globalną, dlatego [1,2], zostało zastąpione [0,0]
#     print("po zmianie", n)
#
# val = [1,2] # do tej zmiennej globalnej przeakuzjemy liste
# change_value(val) # za pomocą tej change_value mozemy zmienić wartość listy 'val=[1,2] - i następnie program przekazuje do piewrszej linii , tak gdzie funkcja def jest opisana , nawet jak jest n ale tu już jest val i to wchodzi zamiast n
# print(val)


##-----------------
## 1. robie funckje ktora ma zestaw argumetow, ale nie checimy definiowac ile tych argumetow jest--------
# def my_func(*args):
#     for el in args:
#         print(el)
#
# my_func(1,2,3,4,5,6,7,8) # teraz tą funkcje 'my func' sobie wywolujemy!!

# 2. to jest przekazywanie wielu argumetow, jako argumentów przekazywanych przez nazwe, a nie przez pozycję--------
# def my_func(**args):
#     for el in args.items():
#         print(el)
#
# my_func(val1 = "raz", val2 = 999) # teraz tą funkcje 'my func' sobie wywolujemy!!