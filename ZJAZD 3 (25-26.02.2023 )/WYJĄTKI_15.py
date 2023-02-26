#WYJĄTKI________________

# 1. SyntaxError - błedy skladni - tego sie na da ominąc, trzeba te błedy poprawic
#a.
# print("adssad")
# print("saddsa" #brak nawiasu

#b.print (1/0) # skaldniowo poprawny, ale nie wolno dzielić przez 0, takze pycharm wyrzuca błed, i mozna tu zrobic wyjątek = except
# try:
#     print(1/0)
# except:
#     print("Cos poszło nie tak")

#c. program fetch number- pobiera od uzytkownika 5 loiczb calkowitch - to ponizsze działa dobrze!
# numbers = []
# for i in range (5):
#     n = int(input("Podaj liczbę całkowitą"))
#     numbers.append(n)
# print(n)

#jak dam enter wystąpi błąd, czyli trezba uniknąc zeby programw ywalal blad po nacisniencu enter bez liczby
# numbers = []
# counter = 0
#
# while True: # ma true zeby sie wogole urucmila
#     if counter > 4:
#         break
#     try: # tu robimy sprawdzenie
#         n = int(input("Podaj liczbę całkowitą")
#     except:
#         print("To nie jest liczba calkowita-sprobuj ponownie")
#         numbers.append(n)
#         counter += 1
#     except:
#         print("To nie jest liczba calkowita-sprobuj ponownie")
#
#
# print(numbers)

# cos tu mi nie działa!!???? -


#d. INWERSJA

while True:
    try:
        number = int (input("Podaj liczbe cakowitą:"))
        print ("Odrtona liczbva:", 1 / number)# teraz robimy inwersje, czyli odrwacamy ją
    # przy podaniu 0 ,czy liery wystapi blad , dlategoi ją usprawnaimy exceptem
    except ValueError:
        print("To nie jest liczba calkowita")
    except ZeroDivisionError:
        print("Bład dzielenia przez zera")
    except:
        print("Cos poszło nie tak")

# ZeroDivisionError: -- zła liczba
# ValueError: -- litery lub sam enter



#e.