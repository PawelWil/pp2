# ctr alt l = prawidłowe ustawienie kodu!

#      -----PĘTLA WHILE:

# ----za pomocą inkrementacji:
# pętla while w tej pętli korzystamt ze zmiennej globalnej
# i = 1 #ta zmienna jest tworzona na zewnątrz, ale tyczy się całego skryptu, a nie tylko tej poniższej pętli
# while i < 10: # instrukcja petli while. Tu warunkiem jest i <10, wszystko co jest mniejsze to się wykona, jeśli będzie już większe to się nie wykona. Będzie się wykonywac do momentu, gdy ten warunek pętli będzie spełniony, jak już nie, to jest stop pętli
#     print(i, end=" ")
#     break  #-jak nie dam break, będzie mi w nieskończoność powtarzać spełniającą się pętlę while, bo i<10
#     i += 1 # operator incrementacji, żeby mi to zwiększało, ale również może być coś zmniejszającego, ktore dobije do tej liczby koncowej zawartej w zakresie (u nas 9 oparacji)

# ----za pomocą dekrementacji:
# i=10 # startuje od 10 -- tu muszę zacząc od jakiejs wiekszej liczby, żeby byo z czegos odejmowac, oraz podać do kiedy ma to byc zmniiejszane- Tu mam start od 10, zmiejszam o -1, i zatrzymuje się na 2, bo 2 jest większe od 1
# while i >1:
#     print(i, end=" ")
#     i-= 1


# pętla for - - w tej pętli nie korzystamy ze zmiennej globalnej, która została zdefiniowana powyżej
# for i in range (0,10): # range od 0 do 10, znaczy że będe mial takie wartośc, czyli 10 wartości, ale od 0 do 9. sprawdzamy warunek, czu i jest mniejsze od 10. Jak będzie równe lub większe od 10 to pętla się nie wykona - iteracja POZIOMA, bo za 'i' jest operator end = " "
#     print (i, end=" " )


# for i in range (10): #range(0, 10, 1) - iteracja PIOnOWA jest gdy w opcji print(i) nie ma end=" ". Jeśli ten operator end=" " jest to wtedy to iterowanie jest poziome
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
# teraz przykład, gdy zaczynamy pętle od wartości 9, czyli i=9, ale checmy ją wykonywać dopoki nasze i będzie wieszke od -1, poniewaz bedę skakal co -1
# for i in range (9, -1, -1): # czyli tu zamiast inkrementował, będę dekrementował, czyli zmniejszal o 1
#     print(i)

# for i in range (-8, -10, -1): # zaczynam od -8, na 10 koncze, a skacze co -1
#     print(i)


#---------
# for i in range (9, 6, -1):
#     print (i)
# start i=9
# dekrementacja do momentu gdy i > 6
# skok o -1


#---------
# TRYB Debug - wpisuje kod + daję znak robak (prawa górna strona) - Debugger to narzędzie pozwalające na kontrolę wykonywania kodu programu. Dzięki niemu możesz zapauzować wykonywanie programu w danym momencie (np. we wskazanej linii kodu). Po zatrzymaniu bardzo często debugger oferuje możliwość podglądnięcia obecnego stanu uruchomionego programu.
# for i in range(5):
#     print(i)

#--------
# SILNIA
# teraz obliczamy silnie "!" - SILNIA to operacja w matematyce, ze operacja 3 silnia (3!), to: 3! = 1 * 2 *3

#----silnia za pomocą pętli FOR
# number = 5 # -- dla liczby5 --> 5! = 1 * 2 * 3 * 4 * 5 = 120
# factorial = 1
# pętla for będzie za to odpowiadac
# for i in range (1, number + 1):
#     factorial *= i #- tu jak dałem *= to te wszystkie liczby się przez siebie mnożą. Jeśli bym dał += to one by się wszystkie dodały i wynik byłby 16
# print(factorial)


# number = 3 # -- dla liczby 3 --> 3! = 1 * 2 * 3 = 6
# factorial = 1
# # pętla for będzie za to odpowiadac
# for i in range (1, number + 1):
#     factorial *= i
# print(factorial)


#------silnia za pomocą pętli WHILE
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
#
counter = 1 #ta zmienna counter jest po to żeby zliczyła, za którym razem udało nam się zgadnąć tą liczbę, i dzięki temu powie nam za który razem zgadłem
number = random.randint(1,10)
guess = int(input("Zgadnij jaką liczbę mam na mysli (1-10): ")) # pobieranie liczby od użytkownika, poprzez zgadywanie jaką liczbę mamy na myśli, oczywiście w tym przypadku od 1 do 10
#
while number != guess:
    guess = int(input("Nie, to nie ta. Spróbuj jeszcze raz: "))
    counter +=1 #ta zmienna counter jest po to żeby zliczyła, za którym razem udało nam się zgadnąć tą liczbę, i dzięki temu powie nam za który razem zgadłem
#
print ("brawo udało Ci się  za: " + str(counter) + "razem" )






