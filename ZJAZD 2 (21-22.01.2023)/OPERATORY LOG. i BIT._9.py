# ZŁOŻONE Warunki/wyrażenia logiczne:

# PODSTAWOWE OPERATORY LOGICZNE:
# Operaot logiczy AND=Koniunkcja - czytamy jako int
# Or - alternatywa - to jest lub
# NOT - negacja - czytamy jak 'nie'

# A. Kodowanie warunku:

# --PRZYKŁAD 1
# Jeżeli temperatura będzie dodatnia i będzie słonecznie, to pójdziemy na spacer...
# ...a jeżeli nie, to zostaniemy w domu

# ----- WARUNEK AND
# temperature  = 12
# is_sun_shining = False

# if temperature > 0 and is_sun_shining: # jeżeli temp będzie > 0 + operartor and (tu musza być spełnione dwa warunki)
#     print("Idziemy na spacer")
# else:
#     print("Zostaniemy w domu") # odpowiedz jest ze 'Zostaniemy w domu', bo zmienną is_sun_shing ustawiłem na false, a przy AND muszą być spełnione dwa warunki żeby był TRUE, i dopiero wykonała się część kodu po 'Else'

# ----- WARUNEk OR
# temperature  = 12
# is_sun_shining = False
#
# if temperature > 0 or is_sun_shining: #tu musi być spełniony jeden lub dwa warunki, zeby było True, czyli 'Idziemy na spacer'
#     print("Idziemy na spacer")
# else:
#     print("Zostaniemy w domu")


# --PRZYKŁAD 2 + Zaprzeczenie 'NOT'
# Jezeli temp będzie ujemna lub będzie pochmurno, to zostaniemy w domu, a jeżeli nie, to pójdziemy na spacer

# temperature  = -2
# is_sun_shining = False #tu musi być spełniony jeden lub dwa warunki, zeby było True, czyli 'Zostaniemy w domu'
#
# if temperature < 0 or not is_sun_shining: #użyliśmy tej samej zmiennej co powyzej, ale w tym przypdaku uzylismi nowej funkcji, czyli zaprzeczenia 'NOT'
#     print("Zostaniemy w domu")
# else:
#     print("Pójdziemy na spacer")

#ctr alt l

# --PRZYKŁAD 3 - wyswietlic opartaor od 0 do 9
# wyświetl cyfrę, chyba że
# liczba parzysta lub liczba większa od 6, to wyświetl *

# for i in range(10):
#     if i % 2 == 0 or i > 6:
#         print("*")
#     else:
#         print(i)

# --PRZYKŁAD 4