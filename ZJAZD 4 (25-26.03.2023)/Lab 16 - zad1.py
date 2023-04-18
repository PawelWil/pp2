## ZADANIE 1 - LAB 16

#  Korzystając z odpowiednich modułów napisz skrypt realizujący następujące
# zadania:
# • wyświetl informacje o procesorze komputera,
# • wylosuj 3 niepowtarzalne liczby ze zbioru 1-10,
# • wyznacz sinus 90 stopni.

# ---------- ROZWIĄZANIE Pana Marcina:
# • wyświetl informacje o procesorze komputera,

import math # w module math, będą dane o sinusie
import random # na bazie modułu random będzie losowanie
import platform # w module platform, będą dane o procesorze

print ("Procesor: ", platform.processor())# procesor - korzystamy z modułu platform, która ma funkcję procesorze, na bazie którego
# dostaniemy informacje o procesorze
print("Losowanie: ", random.sample([x for x in range (1, 11)], 3))# wylosowanie 3 nie powtarzajecych sie liczb, za pomocą  modułu random,
# który ma funkcje sample, w której trzeba ustawić zbiór losować
print("Sinus 90: ", math.sin(math.radians(90))) # moduł math, i funkcja sinus





