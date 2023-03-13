# DEBUGGER (czyli ten robak u góry) to jest opcja sledzenia krok po kroku programu, pokazuje jakie wartosci są przypisawene itd.


# 1. jak wspoładziaja listy razem z funkcjami-----------
# definiujemy funkcje
# def sum_numbers(numbers): # to co jest w nawiasie to są parametry tej fukcji, tutja to zmienna 'numbers'
#     sum = 0
#     for element in numbers: #teraz korzystamy z petli, ktora to ziinna dostanie kolejne lelemty, któr bedzizemy iteroiwac, dla nas to lista, czyli dopisz/dodaj ten elemnt
#         sum += element
#     return sum

# numbers = [1,2,3]# to jest zmienna globalna 'numbers'
# result = sum_numbers(numbers)
# print (result)


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
# --- przykład 0 - pierwszenstwo wyświetlania zmiennej lokalnej, w ciele funkcji, nad zmienną globalną:
# def my_func(): # definiujemy funkcje my_func, z pustym argumentem, pod który poniżej będzie wrzucana wartość zmiennej
#     x = 1 # x=1 - to jest zmienna lokalna, która jest tylko widoczna w ciele funkcji, i w ciele funkcji ona ma pierwszenstwo
    # przed zmienną globalną i ona będzie widoczna a nie zmienna globalna x=3
    # print(x)

# x = 8 # to jest zmienna globalna, czyli zmienna, która dotyczy całego kodu i ona będzie tylko widoczna, gdy damy funkcję
# drukującą print, w obrębie globalnego kodu, a nie w ciele fukcji
# my_func()
# print(x)

# --- przykład 0' - nadpisywanie(czyli zmiana wartości zmiennej globalnej) w ciele funckji, poprzez zawartą instrkcję 'global..'
# w ciele funkcji

# def my_func():
#     global x # poprzez instrukcję global.., nadpisałem zmienną globalną (x=5), zmienną zawartą w ciele funkcji, ale z racji, że przed nią
    # była instrukcja global.., można ją nawet ze jest w ciele funkcji traktować, nie jako zmienną lokalną, ale globalną
    # x=3
# x=5
# my_func()
# print(x) # jak widać zmienna globalna x, przyjmuje wartość nie 5, ale 3, gdzie nadpisanie zostało wykonane w ciele funkcji

# --- przykład 0'' - przekazywanie argumentów do funkcji:
# def pass_value(a):
#     print (a) # jak widać print drukuje nam dwie wartości, które zostały przekazane poniżej, liczbę całkowitą '12' i listę [1,2,3]
# wielkość skalarna, to liczby opisujące miary: waga,siła, prędkość itd. Wielkość wektorowa, to liczby opisujące długość kierunków i zwrotów w przestrzeni wektorowej

# pass_value(12) # tu poprzez wywołanie funkcji pass_value i argumentu 12, przekazuje do funcji (tej górnej części) liczbę 12
# pass_value([1, 2, 3]) # mogę też przekazać listę - tu mowa o liście, która zawiera 3 elementy: 1,2 i 3

# --- przykła 0''' - rekurencja
# rekurencja(rekursja)to odwołanie funkcji do samej siebie
def show_me_recusrion(n):
    if n < 1:
        return
    print ("recursion \n" * n) # jak dam separator \n po słowie, to każdy kolejny będzie się zaczynał od nowej linii
    n =- 1 # tu dajemy n=-1, bo chcemy, żeby to się od 20 razy zmniejszało co 1, 20-1=19, 19-1=18, 18-1-17 itd..
    # aż osiągnie wartość <1, czyli 0, to przestanie się już obniżać od 20 i na podstawie funkcji 'return' zwraca tą wartość,
    # która z kolei dzięki funkcji print(tej powyżej) jest wyświetlana(drukowana). Gdyby nie było print, a samo return, to te wartości
    # by się nie wydrukowały, tylko kod by się wykonał, czyli byłoby: 'Process finished with exit code 0'
    show_me_recusrion(n) # tu mamy znów odwołanie do znów do funkcji show_me_recursion, na zasadzie własnie rekursji,
    # czyli odwołanie tej samej funkcji, do tej samej funkcji (inaczej: odwołanie funkcji, do samej siebie)

show_me_recusrion(20)


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
# my_func(val1 = "raz", val2 = 999) # teraz tą funkcje 'my func' sobie wywolujemy!!;
