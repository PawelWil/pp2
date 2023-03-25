# przyklad importowanain  modułów

# import math # importuje,y moduł 'math'
# print (math.pi) # z modułu math wyswietlamy wartosc pi
# print(math.sin(math.pi / 2))# przykład użycia


# w przegladarce google można się dowiedzieć jakie moduły ma python --> wpisuje python standard library --> wchodze do: https://docs.python.org/3/library/index.html
# i tu mamy wszystkie informację

#mozna sobie pare modułów na raz użyc
# import math
# import sys

# print (math.factorial(5)) # warto śc silni za pomocą funkcji factorial, np. silnia z 5 to: 1*2*3*4*5 = 120
# print(math.floor(4.9999))

# -- od razu import pi z uzyciem pętli for za pomocą modułu math
# from math import pi
# print(pi)

# -- od razu obliczenie sinus z uzyciem pętli for za pomocą modułu math
# from math import pi, sin, factorial, ceil
# print(pi)
# print(sin(pi / 2))
# print (factorial(7)) # to jest silnia
#
# print (ceil(3.8))

# -- from math import *  - importujemy wszysytie modu lu, ale to nie zalecane
# print(pi)
# print(sin(pi / 2))
# print (factorial(7)) # to jest silnia
#
# print (ceil(3.8))

# --- ALIASY
# import  math as m
# print(m.pi) # już mamy zamiast math m, już math nie mozemy uzyc

# lub
# from math import pi as mathpi
# print(mathpi)


# ----- funkcja DIR - pokaze nam co w danym module mamy dostępne
# --a.import math # chcemy zobaczyc jakie elemnty zawiera moduł math
# print(dir(math)) # 1. pokazuje całą bibliotekę modułu math. Wiadomo, że to jest tak samo dla wszystkich modułów

# for e in dir (math):# 2. teraz sobie iterujemy po te liscie
#     print(e)

#b. Teraz moduł Random
# import random
# for e in dir (random):# 2. teraz sobie iterujemy po te liscie co jest w module random
#     print(e)

import random
# print(random.randint(1,3))
# print(random.random())

# -- SEED - elemnet ziarno, jak ten algoytm bedzie generowa l liczby
# 1 sposób
# from random import  random, seed
# for i in range(5):
#     print(random())

# 2 sposób - opis z filmiku sciagnąć
# from random import  random, seed

# seed(0)

# for i in range(5):
#     print(random())

# -- MOduły choice and sample
# from random import  choice, sample

# lst = [1,2,3,4,5,6,7,8,9,10] # 1 sposób tworzenia listy 10 elemntowej
# lst = [i for i in range(1, 11)] # 2 sposób tworzenia listy 10 elemntowej, gdzie jak mamy np 1000 elemntów to mozna go uzyc

# print(choice(lst))# funkcja choice wybierze nam z tegio zbioru jakas liczbe
# print(sample(lst, 5)) # tu wybieramy nie liczbe ale zbior 5iu liczb
# print(sample(lst, 10)) # tu wybieramy nie liczbe ale zbior 10iu liczb
# print(sample(lst, 11))# zbior jest 10 liczbowy, wiec 11 daje bład


# ----- moduł platform
import platform
# help(platform) # funkcja help nam powie co to za moduł
# print(platform.machine()) # nazwa procesora - procek np firmy intel lub AMD
# print(platform.processor())# tu juz dokładne info o procesorze
# print(platform.system()) # sprawdzamy jaki system operacyjny
# print(platform.version()) # jakiej wersji ten sys op
# print(platform.python_implementation()) # jaka wersja pythona
# print(platform.python_version_tuple()) # to jest wersja pythona


# --- dokładne sprawdzenie czegoś z funkcją help
# from platform import machine # bardziej dokładny opis maszyny z funkcją help
# help (machine)
# print(machine())

# from platform import machine, version # bardziej dokładny opis wersji systemu z funkcją help
# help (version)
# print(version())

# from platform import platform

# help(platform) # info o platformie
# print(platform()) #
# print (platform(True, True)) # tu konkretny typ systemu




#-----------------TERAZ TWORZYMY NASZE WAŁASNE MODUŁY

"""This is my first own module...""" # to jest nasz pierwszy moduł :)
# bedzie miał zestaw funkcjonalności
def is_string(val): # 1 funkcja
    """Simple string validator""" # prosty sprawdzacz=walidator
    return isinstance(val, str)

def sum_list_elem(list): # 2 funkcja
    sum = 0
    for i in list:
        sum += i
    return sum

# print(__name__)
if __name__ == "__main__":
    print(is_string("haha") == True)
    print(is_string(123) == False)
    print(sum_list_elem([1,1,1]) == 3)
    print(sum_list_elem([]) == 0)



