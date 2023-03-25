## ZADANIE 1 - LAB 16

#  Korzystając z odpowiednich modułów napisz skrypt realizujący następujące
# zadania:
# • wyświetl informacje o procesorze komputera,
# • wylosuj 3 niepowtarzalne liczby ze zbioru 1-10,
# • wyznacz sinus 90 stopni.

# ---------- ROZWIĄZANIE Pana Marcina:
# • wyświetl informacje o procesorze komputera,

import math
import random
import platform

print ("Procesor: ", platform.processor())# procesor
print("Losowanie: ", random.sample([x for x in range (1, 11)], 3))# 3 nie powtarzajece sie liczby
print("Sinus 90: ", math.sin(math.radians(90)))


# --------- MOJE ROZWIĄZANIE
# • wyświetl informacje o procesorze komputera:
# import platform
# print(platform.machine()) # nazwa procesora - procek np firmy intel lub AMD
# print(platform.processor())# tu juz dokładne info o procesorze
#
#
# # • wylosuj 3 niepowtarzalne liczby ze zbioru 1-10,
# from random import  choice, sample
# lst = [i for i in range(1, 11)] # 2 sposób tworzenia listy 10 elemntowej, gdzie jak mamy np 1000 elemntów to mozna go uzyc
#
# print(sample(lst, 3)) # tu wybieramy nie liczbe ale zbior 5iu liczb
#
#
# # wyznacz sinus 90 stopni.
# import math # importuje,y moduł 'math'
#
# print(math.sin(90))# przykład użycia