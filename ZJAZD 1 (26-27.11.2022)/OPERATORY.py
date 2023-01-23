# print("mam na imię..") # to jest instrukcja
# 2+2  # to jest wyrażenie, i tu się nic nie dzieje, nie wyświetla się nic. Zeby się wyswietlilo coś trzeba dać jakąś funkcję, np. trzeba dać print

# a = 2 **3 #można go przypisać do zmiennej np a
# print(a) # da nam to 8

# OPERATORY

# 1.Operator Dodawania i odejmowania
# print(2+3) # operator dodawania

# print (2+ -3) #przykkład z minusem

# 2.Operator mnoozenia (*)
# print(2*3)
# print(2*3.) # to jest wynik typu zmiennoprzecinkowy - jako float, bo jeded z operandów jest typu float, czyli zmiennoprzecinkowy

# 3.Operator dzielenia - /-dzielenie zwykłe, //-dzieleni całkowite(floor-divided, tl. ang dla dzielenie całkowitego)
# print(4 / 2) # przy dzieleniu zwykłym zawsze dosatniemy zmiennoprzecinkowy wynik
# print(4 // 2) # ale zeby dostać nie zmiennoprzecinkowy, to trza zastosować dzieleni całkowite (czyli //), ale to tylko gdy mamy dwie liczby całkowite, jak się pojawi chociaż jedna liczba zmiennoprzecinkowa, bedziemy ieli wtedy float=zmiennoprzecinkowe - jak widać poniżej
# print(4 // 2.)

#print (4 // 3) # dzielenie całkowite działa na zasadzie zaokreglenia zawsze w dól do najbliższej liczby calkowitej, wytłumaczenie poniżej:
#print (4 // 3) # 1,3333 i najbliższa liczba do zaokrąglenia to 1, czyli wynik 1

#print(-4//3) # dlatego jest -2, bo po prostu schodzi w dół, a potem zaokrągla do najbliższej liczby, czyli jak poniżej
#print(-4//3) -1,3333, czyli najbliższa liczba to -2


# 4.Potęgowanie (**)
# print(3 ** 3)

# 5.Modulo
# print(4 % 3) # tu 3 w 4 mieści się raz i mamy resztę 1, dlatego wynik to jededn-  modula to wynik reszty
#print(14 % 3) # 14 / 3 = 4.., 3*4 = 12, 14-12=2
#print(14 -(3*4)) # to jest rozpisanie operacji modulo
#print (1 % 2) # tu mamy 1--> ile da się dwójek zmiesic w 1, no 0 dwójek, czyli zostaje nam 1, który jest brany jako wynik. Rozpisujemy: 0*2 =0 -> 1-0 = 1
#print(7 % 2) # ile dwójek zmieścimy 7, no zmiescimy 3, i zostaje nam 1, bo 3*2=6, czyli wynik jest 1


# 6. Sprawdzenie czy liczba jest parzysta
#print(3 % 2) # jeżeli wynik jest 0 to jest parzysta, jeśli wynik nie jest zero, tzn. że nie jest parzysta
#print(3 % 2) # tu jak widać jest jeden, czyli nieparzysta
#print(3%2 ==0) # tu możemy zrobić również za pomocą opearora porówania, nie jst 0 wiec false
#print(16 % 2) # tu mamy wynik 0, czyli parzysta

# Operatory 1-argumentowe, maj najwyzszy priorytet
#print(-1)

# Łączenie operatorów - wsyztskie maja lewostronne, oprócz operatora potęgowania
#print (2 +3 -1)# (2+3) -1 --> łączenie lewostronne

#print(2 ** 2 ** 3) # tu mamy łączenie prawodtronne, bo potęgowanie - i odbywa się to tak: wpierw będzie (2 **3), a potem ten wynik będzie potęgowaniem dla liczby 2
#print(2 ** (2**3))

# 7. Prirytetty operatorów
# -, + - jednoargumentowe
# **
# *, /, //, %
# -, + - dwuargumentowe

#print (5 - 2 ** 1 ** 2 / 2) # tu mamy wynik zmiennopezcinkowe, bo zwykle dzielenie, zeby dosatć wynik ca lkowity, trza by było użec dzielenie całkowite(opisane powyzej)

#print (5 - 2 ** 1 ** 2 / 2) # kolejność wykonania: 5 - (2 ** (1 ** 2)) / 2) = 4.0
#print (5 - (2 ** (1 ** 2)) / 2)

# 8. SYSTEMY LICZBOWE (ZAWSZE idziemy od lewej do Prawej!!)

# A. system osemkowy: 0,1,2,3,4,5,6,7 -- print(0o1237)
#print(0o47)
#print (7 * 8 ** 0 + 4 * 8 ** 1 )    # wytłumaczenie dlaczego to 39 -- print (7 * 8 ** 0 + 4 * 8 ** 1 )

# liczba dziesiętnba dla systemu osemkowego,  47 --> 47 = 7 jedności i 4 dziesiątki
#                               7 * 10 ** 0 (bo 10 do potegi 0 to 1) + 4 * 10 ** 1(to są dziesiątki, dlatego do pot ęgi pierwszej, gdy potem są setki, to będziemy miec do potegi 2, potem 1000, czyli potega 3 itd.)


# B. system szesnastkowy: 0,1,2,3,4,5,6,7,8,9, A=10, B=11, C=12, D=13, E=14, F=15 -- print(0xFF) -
#print(0x2F)
#print(15 * 16 ** 0 + 2 * 16 ** 1) # print(15 * 16 ** 0 + 2 * 16 ** 1) -- bo mamy 15 jedności i 2 szesnastki


# C. system binarny(dwójkowy): 0,1  -- print(0b101)
#print(0b101) # 1 jedność(2**0) + 0 dwójek (2**1) + 1 podwójna dwójka, czyli 1 czwórka (2**2) , potem są czwórki, potem
#print(1 * 2 ** 0 + 0 * 2 ** 1 +  1 * 2 ** 2)

# ZADAnIE z Laboratorium 4 zapisu liczb w różnych systemach

# liczba 777 zapisana ósemkowo
#print(0o777)
#print(7 * 8 **0 + 7 * 8 ** 1 + 7 * 8 ** 2, "\n")

# liczba 1011 zapisana binarnie
#print(0b1011)
#print (1 * 2 ** 0 + 1 * 2 ** 1 + 0 * 2 ** 3 + 1 * 2 ** 3, "\n" )

# liczba FFF zapisana szesnastkowo
#print(0xfff)
#print (15 * 16 ** 0 + 15 * 16 ** 1 + 15 * 16 ** 2, "\n")

# lizba 123 zapisana piątkowo ( i tu podstawą jest 5, bo mamy tą liczbę pokazać w systemie piątkowym)
#print(3 * 5 ** 0 + 2 * 5 **1 + 1 * 5 ** 2, "\n")