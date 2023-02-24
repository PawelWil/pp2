# 1. Napisz program sumujący pobrane liczby od użytkownika wg wytycznych:
# • program powinien pobierać od użytkownika liczby całkowite (+),
# • niepodanie liczby powinno zakończyć wprowadzanie danych (???),
# • program powinien podać sumę liczb parzystych oraz sumę liczb nieparzystych (+).


# number = int (input("Proszę podaj 1 liczbę całkowitą: "))
# number1 = int (input("Podaj 2 liczbę całkowitą: "))
#
# if number and number1 % 1 == 0 \
#         and number and number1 % 2 ==0 \
#         or number and number1 % 2 != 0:
#     print ('Podane liczby są całkowite,', 'gdzie suma liczb parzystych i nieparzystych wynosi:', number + number1)
# else:
#     if number and number1 ==0:
#         print('koniec wprowadzania danych')


print ("Proszę podać poniżej zakres liczb, w których znajdziemy liczby całkowite ")
range_from = int(input("Zakres zaczyna się od: "))
range_to = int(input("zakres kończy się na: "))

print("Suma tych liczb, to: ")
for number in range (range_from, range_to + 1):
    if number % 2 == 0 or number % 2 != 0:
        print = sum(number)

# liczba_calkowita = int(input(msg))
# if guess == number:
#     print("brawo! Dokładnie taką liczbę miałem na myśli!")
# else:
#     msg = "Masz kolejną szansę :"
#     if number % 2 == 0:
#         msg += " twoja liczba jest parzysta: "
#     else:
#         msg += " twoja liczba jest nieparzysta: "
#     guess = int(input(msg))
#     if guess == number:
#         print("Brawo! Udało się odgadnąć za drugim razem!")
#     else:
#         msg = "Masz kolejną szansę :"
#         if number > 5:
#             msg += "moja liczba jest większa"
#         else:
#             msg += "moja liczba jest mniejsza lub równa"
#         msg += " od liczby 5: "
#         guess = int(input(msg))
#     if guess == number:
#         print("Brawo! A jednak do trzech razy sztuka")
#     else:
#         msg = "Niestety myślałem o liczbie :" + str(number) + "."
#         print(msg)








# 2. Napisz program, który wylosuje kilka serii liczb całkowitych i wyświetli je
# na ekranie, przy czym:
# • program zapyta użytkownika o zakres minimum oraz maksimum,
# • będzie losował odpowiednie liczby z zakresu podanego przez użytkownika,
# • będzie losował liczbę liczb do wylosowania z zakresu podanego przez użytkownika,
# • będzie losował liczbę serii liczb do wylosowania z zakresu podanego przez
# użytkownika,
# • wyświetli wylosowane serie liczb.



# import random # to jest ściągnięcie biblioteki, która jest mechanizmem do losowania liczb (jakichs znaków)
# up_value = int(input('Podaj górną wartość:'))
# down_value = int(input('Podaj dolną wartość:'))
#
# number = random.randint(up_value, down_value)# ona nam losuje liczbę z przedziału jaki jej podamy, czyli w naszym przypadku, z przdziału od 1 do 3
# if number > up_value and number < down_value:
#     print ("Oto wylosowane liczby z podanego zakresu: ", number)



# guess = int(input("Oto wylosowane liczby z podanego zakresu: ", number)) # zmienna która nam poda jaka liczbę mamy na mysli


# import random # to jest ściągnięcie biblioteki, która jest mechanizmem do losowania liczb (jakichs znaków)
#
# number = random.randint(1, 3) # ona nam losuje liczbę z przedziału jaki jej podamy, czyli w naszym przypadku, z przdziału od 1 do 3
# guess = int(input("Zgadnij jaką liczbę mam na myśli (chodzi o: 1, 2 lub 3) : ")) # zmienna która nam poda jaka liczbę mamy na mysli
# if guess == number:
#     print("brawo! Dokładnie taką liczbę miałem na myśli!")
# else:
#     print("niestety, myślałem o liczbie: " + str(number) + ".")









# 3. Napisz program pobierający od użytkownika liczbę całkowitą i zwracający
# liczbę jedynek w ciągu bitów reprezentujących tę liczbę.


# number = int (input("Podaj liczbę: "))  #podanie liczby całkowitej, dla której jest wyznaczana wartość n-tego bitu, podanego poniżej
# n = int(input("Podaj nr bitu: ")) # numery bitów
# print (bin(number))
# if bin(number) != 1:
# print (number)
# 01001 - przykładowa liczba - i tu się posilkujemy maską
# 00001 - to jest moja  maska
# &      -->za pomocą AND(koniunkcji)=& wyłuskamy te bity
# 00001 - to jest wynik, który

# mask = 1 << n #potrzebujemy maskę wiec dodajemy taką zmienną
# result = number & mask
#
# bit = int(bool(result)) # wyłuskanie bity, czy to jest jeden, czy zero
# print("Bit na pozycji", n, "dla liczby", number, "wynosi", bit)