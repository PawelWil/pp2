
#print("Hello..") #string


# Liczby całkowite=intiger
#print(8+2)
#print(1_000_000) # to pokazuje w łatwiejszy spób dużą liczbę - latwiej widoczna
#print(-2) #liczba z operatorem
#print(type(2)) # to mowi nam jakiego typu jest ten znak - tu integer
#print(type("asd")) # to mowi nam jakiego typu jest ten znak - tu string


# SYSTEMY LICZBOWE (ZAWSZE idziemy od lewej do Prawej!!)
  # System dziesiętny -- 123 = 1 * 10 ^ 2 + 2 * 10 ^ 1 + 3 * 10 ^ 0
#print (1 * 10 ^ 2 + 2 * 10 ^ 1 + 3 * 10 ^ 0)

#print(0b101) #101 = 1 * 2 ^ 2 + 0 * 2 ^ 1 + 1 * 2 ^0 = 4 + 1 = 5 -- #system dwójokw - tu biorą udział liczby: 0,1,
#print(0o1237) #system ósemkowy - tu biorą udział liczby: 0,1,2,3,4,5,6,7 (8 już nie bierze udziału)
#print(0xFF) # #system szesnastkowy - tu biorą udział liczby: 0,1,2,3,4,5,6,7,8,9, A=10, B=11, C=12, D=13, E=14, F=15
#print(0xFF) # F * 16 ^ 1 + F * 16 ^ 0 = 15*16 + 15*1  (ta 16 to podstawa, że mówimy o systemie szesnastkowym, heksagonalnym, stąd zawsze litery, cyfry mnożymy przez 16)
#print (15*16 + 15*1)
#print(0b11111111) # w osmiu jedynkach w systemie binarnym jest przechowywana liczba 255


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



# Zadanie 1 z Laboratorium 3
#print(0x1F)
#print(0b11101)
#print(0o777)
#print(134)
#print(0x1F + 0b11101 + 0o777 + 134 )



#print(0o12 + 0xA) #10 + 10 = 20


# LICZBY ZMIEnnoprzecinkowe (tu mamy część ułąmkową równą zero) - liczba FLOAT
#print(2.0)
# lub
#print(.123)
# lub
#print(99.)

#print(5e3)  # 5* 10 ^ 3 = 5000  (jak mamy to "e" to zawsze dajemy coś do  expotencjalny, czyli 10 do potęgi tej liczby, która za nim stoi)
#print(5e-3)  # 5* 10 ^ -3 = 0.005
#print(type(1e10)) -  jaki typ liczby

# Zadanie 2 z Laboratorium 3 - określić typy literałów
print (type("100.5"))
print (type(2.0,))
print (type(100.5))
print (type('.0eeee-100'))
print (type(.0e-100))
print (type(528))
print (type(False))



#  CIĄGI ZnAKÓW
#print("") # to jest pusty ciąg znaków
#print ("I'm Monty Python")

#print ('><', '>\t<', '>\t\t\t<')
#print ('><', '>\t<', '>\t\t\t<', sep="\n")



# WARTOŚCI Logiczne (tzw. wartości boolowskie)

#print(False)
#print(type(False))
#print(type(2>3)) #bo 2 nie jest większe od 3
#print(2>3)

#print(bool(1)) # wartość większa od 0, dlatego True
#print(bool(13)) # wartość większa od 0, dlatego True
#print(bool(0)) # to jest zero, dlatego False