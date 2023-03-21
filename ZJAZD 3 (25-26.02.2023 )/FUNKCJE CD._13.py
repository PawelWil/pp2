# DEBUGGER (czyli ten robak u góry) to jest opcja sledzenia krok po kroku programu, pokazuje jakie wartosci są przypisawene itd.


# 1. jak wspoładziaja listy razem z funkcjami-----------
# definiujemy funkcje, która będzie zliczać sumę elementów naszej listy przekazanej do finkcji
# def sum_numbers(numbers): # to co jest w nawiasie to są parametry tej fukcji, tutaj zmienną 'numbers'
#     sum = 0 # tu dajemy zmienną lokalną 'sum'
#     for element in numbers: #teraz korzystamy z petli, ktora to zmienna dostanie kolejne elementy, naszego obiektu, kótrym jest lista
#     która to zaś bedzie iterowana
#         sum += element
#     return sum # zwraca nam naszą sumę

# -- 1 sposób na pokazanie sumy - bezpośredni sposób
# print (sum_numbers([1,2,3]))

# -- 2 sposób na pokazanie sumy - dekomponuemy na mniejsze elemnty: dajemy zmienną 'numbers', gdzie przypiszemy listę
#następnie zmienna 'result' gdzie do funkcji sum_numbers wrzucamy listę + finalnie drukujemy za pomocą print tą zmienną 'result'
#w której zawarta jest lista.
# numbers = [1,2,3]# to jest zmienna globalna 'numbers'
# result = sum_numbers(numbers)
# print (result)



# 2. Funkcja ktora generuje listę z losowymi liczbami w zakresie od 0 do 99---------
# parametrem tej funkcji będzie ile liczb będziemy chcieli wylosować, a funkcja będzie nam tą wartość zwracała

# import random # importujemy moduł 'random' do generowanie liczb pseudolosowych

# def generate_numbers(total_numbers): # parametrem naszej funkcji to ilosc liczb = total numbers
#     numbers = []# zmienna lokalna = pusta lista
#     for i in range (total_numbers): #  w pętli for element i, w zasiegu range = total_numbers (czyli tu
#     będzie info ile razy bedziemy przez tą pętlę przechodzić)
#         numbers.append(random.randint(1, 99)) # do listy 'numbers' dodamy za każdym razem wylsowaną wartość,
#         wylosowaną za pomocą odwołanaia do modułu random + oczywiście skorzystamy z metody randint = za pomocą której
#         będziemy losowac liczby w zakresie miedzy 1 a 99.
#     return numbers # A teraz po losowaniu zrwacamy naszą listę o nazwie 'numbers'

# print (generate_numbers(10)) # używamy naszej funkcji 'generate_numbers' za pomocą ktorej (oczywiście zeby się te liczby wylosowane wyświetliły, musimy uzyć funkcji drukującej 'print')
# w tym przypadku wylosuje nam 10 liczb, z zakresu od 1 do 99 i pokaze na ekranie
# print (generate_numbers(100)) # tu nam wylosuje 100 liczb
# print (generate_numbers(123233)) # a tu nam wylosuje 123233 liczb


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
# def show_me_recusrion(n):
#     if n < 1:
#         return
#     print ("recursion \n" * n) # jak dam separator \n po słowie, to każdy kolejny będzie się zaczynał od nowej linii
#     n =- 1 # tu dajemy n=-1, bo chcemy, żeby to się od 20 razy zmniejszało co 1, 20-1=19, 19-1=18, 18-1-17 itd..
    # aż osiągnie wartość <1, czyli 0, to przestanie się już obniżać od 20 i na podstawie funkcji 'return' zwraca tą wartość,
    # która z kolei dzięki funkcji print(tej powyżej) jest wyświetlana(drukowana). Gdyby nie było print, a samo return, to te wartości
    # by się nie wydrukowały, tylko kod by się wykonał, czyli byłoby: 'Process finished with exit code 0'
    # show_me_recusrion(n) # tu mamy znów odwołanie do znów do funkcji show_me_recursion, na zasadzie własnie rekursji,
    # czyli odwołanie tej samej funkcji, do tej samej funkcji (inaczej: odwołanie funkcji, do samej siebie)

# show_me_recusrion(20)


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

# # przyklad 3------- ZASIĘG ZMIEnnych CD.
def scope_test (): # definujemy funkcje o nazwie scope_test ,  ma on ajedną zmienną lokalką x - to jest x poniżej,
# do której przypiszemy wartość 123
    x=123 # zmienna lokalna
    print(" wsrodku funkji:" + str(x)) # to wyswietla niezaleznie dla globalnej lokalnej x = 123

# x = 99 # zmienna globalna 99
# scope_test() # jak to uruchmimy tą funkcje poprzez scope_test i mamy u gory print, to jak widać te 99 się pokazało
# print(" na zewnatrz: " + str(x)) # to wyswietla niezaleznie dla globalnej zmiennenn x = 99


# przyklad 4 - tu wplywamy na zmienną globalną i znienić ją w ciele funkcji (nadpisujemy zmienną globalną,
# za pomocą zmiennej w lokalnej w ciele funkcji---------
# def scope_test ():
#     global x # zeby moc zamienic zmienną globalną trzeba uzyc instrukcji global, która zacznie traktować zmienną x,
    # nawet lokalnie/wewntarz bedzie traktować jako globalną
    # x=123 # zmienna lokalna , która zastępują zmienną globalną (x=99)
    # print(" w środku funkji: ", x) # to wyswietla niezaleznie dla globalnej lokalnej x = 123, bo globalna zosyała zamieniona
    # (info jak powyżej). Tu nie użyliśmy konkatenacji, dlatego nie zamienilismy liczby całkowitej na stringa

# x = 99 # zmienna globalna 99
# scope_test() # jak to uruchmimy tą funkcje poprzez scope_test i mamy u gory print, to jak widać te 99 się pokazało
# print(" na zewnątrz funkcji: " + str(x)) # po uzyciu instrukcji globalnej jak widać wyswiretla się  x = 123.
# Tu użyliśmy konkatenacji, dlatego zamienilismy liczby całkowitą na stringa



### -------------ZDefiniowanie fukcji, ktorej zadaniem jest zmiana wartości---------

# def change_value(n):# do tej funkcji przekazujemy argument n - mowa o wartosciach skalarnych, czyli liczby (int, float), a potem lista -->
# zadaniem tej funkcji będzie zamiana wartości, do tej funkcji będziemy przekazywać wartości tu n = val
#     print ("przed zmiana:", n) # sprawdzamy wartość obecną
#     n+= 1 # teraz dokunuemy zmiany, gdzie n zwiekszamy o 1
#     print("po zmianie", n) # teraz pokazujemy co się stało po zmianie, czyli po dodaniu 1 do argumentu n, które zgodnie z poniższą
# wartością zmiennej 'val'=7 wynosi 7, będzie wynosić 8.

# val = 7 # do tej zmiennej globalnej przeakuzjemy jakąś wartosc int = 7
# change_value(val) # za pomocą tej change_value mozemy zmienić wartość listy 'val=[1,2]'
# i następnie program przekazuje do piewrszej linii , tak gdzie funkcja def jest opisana ,
# nawet jak jest n ale tu już jest val i to wchodzi zamiast n
# print(val) # tu wiadomo, że wyswietlimy 7, a nie 8, bo ten print odnosi się do zmiennej globalnej (powyżej)


## przekazujemy listę - jakas wartość nieskalarna------------ jakaś np. lista
# def change_value(n):# do tej funkcji przekazujemy argument n - tu nieskalarna, czyli np. lista --> tu n = val = [1,2]
#     print ("przed zmiana:", n) # tu się odnosi do zmiennej globalne
#     n = [0,0] # tu się odwołuje do zmiennej lokalnej, gdzie pod n podstawilismy całkeim inny obiekt, ale lokalnie,
    # który ma pierwszenstow nad globalną, dlatego [1,2], zostało zastąpione [0,0]
    # print("po zmianie", n) # tu po zmianie wyświetli się zmienna n = [0,0], który został podany powyżej

# val = [1,2] # do tej zmiennej globalnej przeakuzjemy liste
# change_value(val) # za pomocą tej change_value mozemy zmienić wartość listy 'val=[1,2] - i następnie program przekazuje do piewrszej linii , tak gdzie funkcja def jest opisana , nawet jak jest n ale tu już jest val i to wchodzi zamiast n
# print(val) # tu funkcja change_value będzie się odnosić do zmiennej 'val', która jest zmienną globalną,
# która rowna się: val = [1,2], czyli wyświetli się lista [1,2]

## Kolejny przyklad - zmien wartosc listy, która jest listą mającą element 0 [0] i podstaw za nią wartos 999--------------
# def change_value(n):
#     print ("przed zmiana:", n)
#     n[0] = 999 # tu bedziemy miec: [999, 2] pod n, w indeksie 0 podstawilismy całkeim inny obiekt, ale lokalnie,
    # który ma pierwszenstow nad globalną, dlatego [1,2]=przed zmianą, zostało zastąpione [999,2]=po zmianie
    # print("po zmianie", n)

# val = [1,2] # do tej zmiennej globalnej przeakuzjemy liste
# change_value(val) # za pomocą tej change_value mozemy zmienić wartość listy 'val=[1,2] - i następnie program przekazuje do piewrszej linii , tak gdzie funkcja def jest opisana , nawet jak jest n ale tu już jest val i to wchodzi zamiast n
# print(val)




##-----------------
### 1. Robię funckje ktora ma zestaw argumetow, ale nie chcemy definiowac ile tych argumetow jest--------
# def my_func(*args):
#     for el in args: # pętla for - dla el(elementów) w zbiorze args(argumentów)
#         print(el)

# my_func(1,2,3,4,5,6,7,8) # teraz z ręki postawiliśmy do funkcji my_func, do jej argumentu (*args) co ten argument 'args'
# będzie w sobie zawierał, czyli będzie zawierał liczby od 1 do 8

### 2. to jest przekazywanie wielu argumentow, jako argumentów przekazywanych przez nazwe, a nie przez pozycję--------
# ????
# def my_func(**args):
#     for el in args.items():
#         print(el)
#
# my_func(val1 = "raz", val2 = 999) # teraz tą funkcje 'my func' sobie wywolujemy!!;
