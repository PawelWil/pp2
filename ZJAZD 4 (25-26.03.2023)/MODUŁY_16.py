# !!! TO JEST MODUŁ 16, KTÓRY ZAJMUJE SIĘ TWORZENIEM MODUŁÓW FUNKCJI.
# DLATEGO JEST NAZWANY JAKO module BO PRZY ODNOSZENIU SIE DO KODU Z TEGO MODUŁU NAZWA MUSI BYĆ DOKŁADNIE TA SAMA !!!!


# przyklad importowania  modułów

# 1. import modułu math # importuje,y moduł 'math'
# import math
# print (math.pi) # z modułu math wyswietlamy wartosc pi
   #lub
# print(math.sin(math.pi / 2))# przykład użycia funkcji sinus z pi / 2 --> czyli sinus 1/2 pi


# ** w przegladarce google można się dowiedzieć jakie moduły ma python --> wpisuje python standard library
# --> wchodze do: https://docs.python.org/3/library/index.html
# i tu mamy wszystkie informację

# mozna sobie importować pare modułów na raz, np muduł 'math' i moduł 'sys', wpisując je jeden pod drugim, jak poniżej:
# import math
# import sys

# zeby wywołać konkretną funkcję, musimy wpierw podać z jakiego ona jest modułu - przykłady ponizej:
# print (math.factorial(5)) # np. wyswietlamy z modułu 'math, wartośc silni za pomocą funkcji 'factorial', np. silnia z 5 to: 1*2*3*4*5 = 120
# print(math.floor(4.9999)) # np. wyświetlamy z modułu 'math' funkcje 'floor'

# -- poniżej chcemy zaimportować tylko jeden element-w gtym przypadku stałą 'pi',
# czyli importujemy ją z modułu 'math' i od razu dajemy, jaką zmienną chcemy zaimportować, np. import zmiennej 'pi'
# z uzyciem pętli for za pomocą modułu math:

# from math import pi
# print(pi) # od razu dajemy co chcemy wyswietlić, nie podajemy, że np.chcemy to pi wyswietlic z modułu 'math' bo wyskoczy błąd
# print(math.pi) # tu zgodnie z powyższym wystąpił błąd.

# -- od razu obliczenie sinus z 1/2 pi z uzyciem pętli for za pomocą modułu math - alee musimy te funkcjie pi, sin, factorial i ceil
# zaimportować - jeśli ich nie zaimportujemy, to wyskoczy błąd
# from math import pi, sin, factorial, ceil
# print(pi) # to pokazuje pi
# print(sin(pi / 2)) # to pokazuje sin z 1/2 pi
# print (factorial(7)) # to jest silnia z liczby 7, czyli: 1*2*3*4*5*6*7 = 5040
# print (ceil(3.8)) # dodatkowo obliczenie zaokrąglenia w gore, za pomocą funkcji 'ceil', gdzie 3.8 jest zaokrąglone do liczby 4

# -- from math import *  - można zaimportować wszysytkie funkcje z danego modułu, ale to nie jest zalecane,
# gdyż jak zaimportujemy wszystko robi się bałagan i  wszystko jest dostępne.  Jak widać poniżej nie importowaliśmy poszczegolnych
# fukcji, tylko daliśmy *, co dało nam import wszystkiego
# from math import *
# print(pi)
# print(sin(pi / 2))
# print (factorial(7)) # to jest silnia
# print (ceil(3.8))

# --- ALIASY - to jest zamiana importowanych nazw na nowe, np. moduł 'math' został zamieniony na 'm'
# i od teraz wszystkie funkcje z modułu 'math' są odnajdywane za pomocą nowej nazwy 'm'. Już stara nazwa modułu'math' nie działa
# i za jej pomocą nie odnajdziemy nic, od tej zamiana, musimy tylko i wyłącznie używać nowej nazwy modułu,
# jaką jest w naszym przypadku 'm':

# import  math as m
# print(m.pi) # już mamy zamiast 'math' --> 'm', już math nie mozemy uzyc
# print(math.pi) # jak widać nie działa, bo już nie ma takiego modułu 'math' w mojej bibliotece

# lub zamiana nazwy funkcji. W naszy, przypadku stała funcji 'pi', zamieniona jest na 'mathpi'
# from math import pi as mathpi
# print(mathpi)


# ----- funkcja DIR - ta funkcja pokaze nam, co w danym module mamy dostępne
# --a.
# import math # chcemy zobaczyc jakie elemnty zawiera moduł math
# print(dir(math)) # 1. pokazuje nam całą listę elementów modułu 'math'. Wiadomo, że to jest tak samo dla wszystkich modułów,
# żeby sprawdzić zawartość innych modułów

# for e in dir (math):# 2. teraz sobie iterujemy te elementy modułu 'math' po liscie, za pomoć pętli 'for' żeby były bardziej widoczne:
# import math
# for e in dir(math):
#     print(e)

# b. Teraz moduł Random
# import random
# for e in dir (random):# 2. teraz za pomocą 'dir' sprawdzam co mamy w module 'random' +
    # sobie iterujemy, za pomocą pętli 'for' po te liscie, żeby zobaczyć, w sposób czytleny co jest w module random
    # print(e)

# import random
# print(random.randint(1,3)) # np. losowanie za pomocą funkcji 'randint' liczby losowej od 1 włącznie do 3 włącznie
# print(random.random()) # np.  losowanie za pomocą funkcji 'random' liczby losowej z przedziału od 0(przedział zamknięty,
# czyli od 0 włącznie), do 1(przedział otwarty, czyli nigdy nie węxmie 1, ale zawsze coś mniejszego)

# -- SEED - element ziarno, to jest algorytm, który wpływa na generowanie losowych liczb, jeśli go ustawimy na stałe,
# to zawsze będą te same liczby generowane. Jesli damy jakiś przedział, to tylko z tego przedziału.
# 1 sposób - tu importujemy z modułu 'random' funckję 'random' + 'seed'
# from random import  random, seed
# for i in range(5): # generujemy 5 liczb za pomocą for i przeiterujemy po tych pięciu  = dostajemy jakieś pseudolowoe liczby,
    # które za każdym razem są inne
    # print(random())

# 2 sposób - tu wywołujemy za pomocą ustawionej na stałe funkcji 'seed'- w naszym przypadku 0,
# która nie będzie się zmieniać. I tu poprzez to, dostajemy, że zawsze mamy te same liczby.
# from random import  random, seed
# seed(0)

# for i in range(5):
#     print(random())

# -- MOduły 'choice' and 'sample' - cd. losowania liczb ze zbiorów. One są funkcjami,
# które nam pomogą w losowaniu w lsowaniu z liczb ze zbioru

from random import  choice, sample

# lst = [1,2,3,4,5,6,7,8,9,10] # 1 sposób: tworzymy prostą 10 elemntową listę, o nazwie 'lst'
# lst = [i for i in range(1, 11)] # 2 sposób tworzenia listy: teraz mówimy o liście 10-elementowej, to mozemy to zrobić ręcznie,
# ale gdybyśmy mieli listę np. 1000 elemntową, to ręczne jej uzupełnienie byłoby cięzkie, dlatego wtedy warto skorzystać
# z pętli for, która nam ten przedział w ułamku sekundu przeiteruje

# print(lst) # pokazuje nam całą listę
# print(choice(lst))# funkcja 'choice' wylosuje nam z tego zbioru jakąs losową liczbe
# print(sample(lst, 5)) # funkcja 'sample' -tu wybieramy losowo kilka liczb. Wpierw podajemy zior, z którego te liczby będą wylosowane,
# w naszym przypadku jest to lista 'lst, a następnie podajemy ile z tego zbioru listy 'lst' ma być wylosowanych liczb,
# czyli de facto wyświetli się nam zbiór listy, składający się z 5iu losowo wybranych liczb
# print(sample(lst, 10)) # tu wybieramy nie liczbe ale zbior 10iu liczb
# print(sample(lst, 11))# zbior jest 10 liczbowy, wiec 11 daje bład


# ----- moduł platform
# import platform
# help(platform) # funkcja help nam powie co to za moduł, z którego będziemy za chwilę importować poszczególne funkcje
# print(platform.machine()) # nazwa procesora - procek np firmy intel lub AMD
# print(platform.processor())# tu juz dokładne info o procesorze
# print(platform.system()) # sprawdzamy jaki system operacyjny
# print(platform.version()) # jakiej wersji jest ten system operacyjny
# print(platform.python_implementation()) # jaka implementacja pythona - jest 'C' = canone python
# print(platform.python_version_tuple()) # to jest wersja pythona


# --- dokładne sprawdzenie czegoś za pomocą funkcji 'help':
# from platform import machine # bardziej dokładny opis funkcji 'machine' za pomocą funkcji 'help'
# help (machine)
# print(machine())

# from platform import machine, version # teraz mamy bardziej dokładny opis platformy za pomocą funkcji 'help', czyli dodatkowo wersji
# help (version)
# print(version())

# from platform import platform # importujemy funkcję platform - i za pomocą help, zobaczymy co nam ta funckja 'platfrom' daje
# help(platform) # info o platformie
# print(platform())
# print (platform(True, True)) # tu konkretny typ systemu, czyli za pomocą warunków 'true'upraszczamy informacje, jakie dostajemy,
# w naszym przypdaku to jest info o wersji systemu, czyli np. Windows-10



# -----------------CZEŚĆ II - TERAZ TWORZYMY NASZE WAŁASNE MODUŁY --> przchodzę do folderu 'modules' --> i tam są tworzone te moduły


