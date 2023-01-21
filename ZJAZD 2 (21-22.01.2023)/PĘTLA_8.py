# i = 1 #ta zmienna jest tworzona na zewnątrz, ale tyczy się całego skryptu, a nie tylko tej poniższej pętli
# pętla while - w tej pętli korzystamt ze zmiennej globalnej
# while i < 10: # instrukcja petli while. Tu warunkiem jest i <10, jeśli jest mniejsze to się wykona, jeśli będzie większa nie wykona. Będzie się wykonywac do momentu, gdy ten warunek pętli będzie spełniony, jak już nie, to jest stop pętli
#     print(i, end=" ")
#     i += 1 # operator incrementacji

# pętla for - - w tej pętli nie korzystamy ze zmiennej globalnej, która została zdefiniowana powyżej
# for i in range (0,10): # range od 0 do 10, znaczy że będe mial takie wartośc, czyli 10 wartości, ale od 0 do 9. sprawdzamy warunek, czu i jest mniejsze od 10. Jak będzie równe lub większe od 10 to pętla się nie wykona
#     print (i, end=" " )


# for i in range (10): #range(0, 10, 1)
#     print(i)


# for i in range (3,10): # tu iteruje od 3 do 10
#     print(i)

#---------
# for i in range (2, 10, 3):
#     print (i)
 #początek itercaji to i=2
 #dopóki i < 10 => na 10 koncze
 #skaczemy co 3


#---------
# teraz przykład, gdy zaczynamy pęytle od wartości 9, czyli i=9, ale checmy ją wykonywać dopoki nasze i będzie wieszke od -1, poniewaz bedę skakal co -1
# for i in range (9, -1, -1): # czyli tu zamiast inkrementował, będę dekrementował, czyli zmniejszal o 1
#     print(i)

# for i in range (-9, -10, -1): # zaczynam od -9, na -10 koncze, a skacze co -1
#     print(i)


#---------
# for i in range (9, 6, -1):
#     print (i)
# start i=9
# dekrementacja do momentu gdy i > 6
# skok o -1


#---------
# TRYB Debug - wpisuje kod + daję znak robak (prawa górna strona) - wyczaić, co ten try robi..??
# for i in range(5):
#     print(i)

#--------
# SILNIA
# teraz obliczamy silnie "!" - SILNIA to operacja w matematyce, ze operacja 3 silnia (3!), to: 3! = 1 * 2 *3

#----silani za pomocą pętli FOR
# number = 5 # -- dla liczby5 --> 5! = 1 * 2 * 3 * 4 * 5 = 120
# factorial = 1
# # pętla for będzie za to odpowiadac
# for i in range (1, number + 1):
#     factorial *= i
# print(factorial)
#
# number = 3 # -- dla liczby 3 --> 3! = 1 * 2 * 3 = 6
# factorial = 1
# # pętla for będzie za to odpowiadac
# for i in range (1, number + 1):
#     factorial *= i
# print(factorial)


#----silani za pomocą pętli WHILE
# number = 5
# factorial = 1
# while number:
#     factorial *= number
#     print(number, factorial)
#     number -= 1
#     print(factorial)


#------ normalna pętla
# for i in range(5):
#     print(i)
# else: # to else się wykona tylko wtedy, gdy pętla nie zostanie przerwana np. opercają break, czyli zakonczenie pętli definitywnie
#     print("Koniec pętli...")

#---------
# for i in range(5):
#     print(i)
#     if i ==3:
#         break
# else: # tu się else nie wykonało, bo mamy break
#     print("Koniec pętli...")


# GRA-------------
import random

counter = 1 #ta zmienna counter jest po to żeby zliczyła, za którym razem udało nam się zgadnąć tą liczbę, i dzięki temu powie nam za który razem zgadłem
number = random.randint(1,10)
guess = int(input("Zgadnij jaką liczbę mam na mysli (1-10): ")) # pobieranie liczby od użytkownika, poprzez zgadywanie jaką liczbę mamy na myśli, oczywiście w tym przypadku od 1 do 10

while number != guess:
    guess = int(input("Nie, to nie ta. Spróbuj jeszcze raz: "))
    counter +=1 #ta zmienna counter jest po to żeby zliczyła, za którym razem udało nam się zgadnąć tą liczbę, i dzięki temu powie nam za który razem zgadłem

print ("brawo udało Ci się  za: " + str(counter) + "razem" )






