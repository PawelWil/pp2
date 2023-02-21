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
# is_sun_shining = True

# if temperature > 0 and is_sun_shining: # jeżeli temp będzie > 0 + operartor and (tu musza być spełnione dwa warunki)
#     print("Idziemy na spacer")
# else:
#     print("Zostaniemy w domu") # odpowiedz jest ze 'Zostaniemy w domu', bo zmienną is_sun_shing ustawiłem na false, a przy AND muszą być spełnione dwa warunki żeby był TRUE, i dopiero wykonała się część kodu po 'Else'

# ----- WARUNEk OR
# temperature  = 12
# is_sun_shining = False

# if temperature > 0 or is_sun_shining: #tu musi być spełniony jeden lub dwa warunki, zeby było True, czyli 'Idziemy na spacer'
#     print("Idziemy na spacer")
# else:
#     print("Zostaniemy w domu")


# --PRZYKŁAD 2 + Zaprzeczenie 'NOT'
# Jezeli temp będzie ujemna lub będzie pochmurno, to zostaniemy w domu, a jeżeli nie, to pójdziemy na spacer

# temperature = 2
# is_sun_shining = False  # tu musi być spełniony jeden lub dwa warunki, zeby było True, czyli 'Zostaniemy w domu'

# if temperature < 0 or not is_sun_shining:  # użyliśmy tej samej zmiennej co powyzej, ale w tym przypdaku uzylismi nowej funkcji, czyli zaprzeczenia 'NOT'
#     print("Zostaniemy w domu")
# else:
#     print("Pójdziemy na spacer")

# ctr alt l = prawidłowe ustawienie kodu!

# --PRZYKŁAD 3 - wyswietlic opartaor od 0 do 9
# wyświetl cyfrę, chyba że
# liczba parzysta lub liczba większa od 6, to wyświetl *

# for i in range(10):
#     if i % 2 == 0 or i > 6:
#         print("*")
#     else:
#         print(i)


# --------------------------OPERATORY  BITOWE -----------------------
# a = 5 # 5 i 3, to są wartości dziesiętne, ale zapisywane są binarnie, czyli liczymy jak binarnie, czyli np. liczba 5 to: 00000101 --> 1 * 2 ** 0(1) + 0 * 2 ** 1(0) + 1 * 2 ** 2 (4) +.. --> i mamy 5 :)
# b = 3

# 1. Koniukncja Bitowa (czyli 'i' - widok operatora &)
# print (a, "&", b, "=", a & b)
# print (bin(a)) # teraz przedstawiamy w postaci binarnej --> bin = binary
# print("{:08b}".format(a)) # na osmiu pozycjach, chcemy rzpisać te bity binarnie - to jest bardziej praktyczne niż powyzsze rozpisanie, które jest ok - i tu korzystamy z funkcji 'format'
# print("{:08b}".format(b))
# print("-" * 8)
# print("{:08b}".format(a & b)) # wynikiem jest 00000001, bo pierwsze 1 mamy w pierwszej linii (a=5) i drugiej linii (b=3) i 1 z 1 daje 1, ale już w drugiej i trzeciej kolumnie mamy 0 i 1 oraz 1 i 0, co daje 0, więc wynik konikunki to 00000001

# 2. Alternatywa Bitowa (czyli 'or' - widok operatora | (pajp-tak sie go nazywa))
# print (a, "|", b, "=", a | b)
# print (bin(a)) # teraz przedstawiamy w postaci binarnej --> bin = binary
# print("{:08b}".format(a)) # na osmiu pozycjach, chcemy rzpisać te bity binarnie - to jest bardziej praktyczne niż powyzsze rozpisanie, które jest ok - i tu korzystamy z funkcji 'format'
# print("{:08b}".format(b))
# print("-" * 8)
# print("{:08b}".format(a | b)) # wynikiem jest 00000111, bo pierwsze 1 mamy w pierwszej linii (a=5) i drugiej linii (b=3) i 1 z 1 daje 1, oraz w drugiej i trzeciej kolumnie mamy 0 i 1 oraz 1 i 0, co daje nam jedynki,  więc wynik a;ternatywy  to 00000111

# 3. Alternatywa x or - Alternatywq rozłączna - widok operatora ^ - w tej alternatywie jest a, gdy bity się różnią, gdy są takie same jest 0
# print (a, "^", b, "=", a ^ b)
# print (bin(a)) # teraz przedstawiamy w postaci binarnej --> bin = binary
# print("{:08b}".format(a)) # na osmiu pozycjach, chcemy rzpisać te bity binarnie - to jest bardziej praktyczne niż powyzsze rozpisanie, które jest ok - i tu korzystamy z funkcji 'format'
# print("{:08b}".format(b))
# print("-" * 8)
# print("{:08b}".format(a ^ b))

# 4. Przesunięcie bitów w prawo >>

# print (a, ">>", b, "=", a >> b) # tu przesuwamy o 3 miejsca, bo b=3
# print (bin(a)) # teraz przedstawiamy w postaci binarnej --> bin = binary
# print("{:08b}".format(a)) # na osmiu pozycjach, chcemy rzpisać te bity binarnie - to jest bardziej praktyczne niż powyzsze rozpisanie, które jest ok - i tu korzystamy z funkcji 'format'
# print("-" * 8)
# print("{:08b}".format(a >> b))

# print (a, ">>", 2, "=", a >> 2) # tu przesuwamy o 2 miejsca, bo b=3
# print (bin(a)) # teraz przedstawiamy w postaci binarnej --> bin = binary
# print("{:08b}".format(a)) # na osmiu pozycjach, chcemy rzpisać te bity binarnie - to jest bardziej praktyczne niż powyzsze rozpisanie, które jest ok - i tu korzystamy z funkcji 'format'
# print("-" * 8)
# print("{:08b}".format(a >> 2))

# 5. Przesunięcie bitów w lewo <<

# print (a, "<<", 2, "=", a << 2) # tu przesuwamy o 2 miejsca, bo b=3
# # print (bin(a)) # teraz przedstawiamy w postaci binarnej --> bin = binary
# print("{:08b}".format(a)) # na osmiu pozycjach, chcemy rzpisać te bity binarnie - to jest bardziej praktyczne niż powyzsze rozpisanie, które jest ok - i tu korzystamy z funkcji 'format'
# print("-" * 8)
# print("{:08b}".format(a << 2))

# 6. Negacja bitow ~  tylda (zanegowanie) - TYLDĘ WPISUJE poprzez kombinacje: shift + spacja + '~' (tylda jest pod esc) - prezentowanie liczb ujemnych za pomocą zapisu binarnego -- czyli jeśli ostatni bit jest na jeden, to liczba jest ujemna, i u nas tak jest, bo ostatnia jest jedynka
# print ("~" + str(a), "=", ~a)
# print (bin(a)) # teraz przedstawiamy w postaci binarnej --> bin = binary
# print("{:08b}".format(a)) # na osmiu pozycjach, chcemy rzpisać te bity binarnie - to jest bardziej praktyczne niż powyzsze rozpisanie, które jest ok - i tu korzystamy z funkcji 'format'
# print("-" * 8)
# print("{:08b}".format(~a))

# print()
# for i in range(5, -6, -1): # przykład iteracji do tylu i pokazanie jak to wygląda bitowo
#     print("{0:08b} => {1:d}".format(i & 255, i))

# 7. OPERATOR PORÓWNANIA

# # 1 przykład
# a = 3
# b = 4
# c = 7
# print(a < b < c) # da nam to true
# print(a < b and b < c)  # to jest ten sam zapis co powyższy, czyli: print(a < b < c)

# 2 przykład
# a = 3
# b = 4
# c = 7

# def get(a):  # funkcja get pobiera
#     print("!!!!!!!!!")  # funkcja return oddaje dane
#     return a
# print(a < b < c)
