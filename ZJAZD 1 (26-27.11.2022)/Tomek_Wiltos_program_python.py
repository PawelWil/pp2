# -------- I. KALKULACJA DANYCH KWADRATU:---------
# 1. Pole powierzchni kwadratu: P=a**2
# 2. Obwód kwadratu: Obwód = 4 * a
# 3. Długość przekątnej, z twierdzenia Pitagorasa: d = a ** 2 + a ** 2

#     #Podanie długości boku kwadrata
a = int(input("Proszę podaj długość boku kwadratu: "))
#
#     #Pole powierzchni kwadratu, dla boku o długości a
p = a ** 2 #zmienna określająca pole powierzchni = 'p'
print ("Pole powierzchni wynosi:", p)
#
#     #Obwód kwadratu, dla boku o długości a
obwod = 4 * a #zmienna określająca obwód = 'obwod'
print ("Obwód kwadratu wynosi:", obwod)
#
#     #Długość przekątnej kwadratu, dla boku o długości a
przekatna = a * (2 ** 0.5) #zmienna określająca przekątną = 'przekatna'
print ("Przekątna kwadratu wynosi: ", round(przekatna, 3))




# # -------- II. KALKULACJA DANYCH TRÓJKĄTA:---------
# #1. Podanie wymiarów trzech odcinków
# print ("Podaj długości 3 odcinków (liczby całkowite): ")
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
#
# #2. Weryfikacja, czy z tych trzech odcinków mozna zbudować trojkąt
# #czyli musi być spełniony warunek a + b są wieksze od c, no bo nie moga byc te boki mniejsze od c
# #+ inne kombinacje też muszą być wymienione, no bo np. bok 'a' nie może być większy od 'b+c', zaś bok 'b', nie może być wiekszy od c+a.
# #program musi mieć jasno sprecyzowane warunki, według których wykona obliczenia oraz różnorakie kalkulacje
# if (a+b > c and b+c > a and c+ a > b): # warunek 'if' (polskie 'jeśli') - czyli jeśli coś zostanie spełnione, wtedy program może iść dalej
#     print("Z tych odcinków można zbudować", end=" ")
#
# #3. Teraz oceniamy jaki to jest trójkąt, czy: równoboczny, równoramienny, różnoboczny
#     # warunek 1, który określa czy trójkąt jest równoboczność:
#     if a == b and a == c and c == b: # czyli jesli wszystkie boki są sobie równe to równoboczny trójkąt.
#         # Żeby to było spełnione musimy dać operato'AND' (polskie 'i')
#         print("trójkąt równoboczny", end=" ")
#     # warunek 2, który określa czy trójkąt jest równoramienny:
#     elif a == b or b == c or c ==a: #jeśli warunek 'if' nie jest spełniony, a dalej chcemy na bazie warunków sprawdzać kolejne zależności,
#         # wtedy kontynuacją 'if' jest 'elif'='else_if' (polskie 'w przeciwnym razie=else + jeśli=if')
#         # W tym warunku umieszczamy operator 'OR' (polskie 'lub'), czyli jeśli a = b lub b = c itd. to wiadomo, że któryś z boków jest sobie
#         # rowny, czyli trojkąt jest równoramienny
#         print("trojkat rownoramienny", end = " ")
#
#     # warunek 3, który po niespełnieniu warunków 1 i 2,  wynikowo określa, że jest to trójkąt różnoramienny:
#     else: # czyli ten warunek 'else' konczy warunkowanie danego obszaru kodu - reasumując jak nie jest spełniony warunek 1 i warunek 2,
#         # to mamy coś wynikowego - w tym przypadku wynikiem z niespełnienia warunku 1 i 2 jest warunek 3 = to jest trojkąt różnoramienny.
#         print("trojkat rożnoramienny", end = " ")
#
# #4. Teraz oceniamy trójkąt, ze względu na kąty, czy: prostokatny, rozwartokatny, ostrokatny.
#     # teraz robimy czy jest prostokatny:
#     if (a ** 2 + b ** 2 == c ** 2) or (b ** 2 + c ** 2 == a ** 2) or (a ** 2 + c ** 2 == b ** 2): # za pomocą tego twierdzenie Pitagorasa
#         # sprawdzamy, czy trojkat jest prostokatny - czyli jak to jest spełnione to trojkat prostokatny
#         print("prostokatny.")
#     # teraz sprawdzamy, czy rozwartokatny ostrokatny:
#     elif (a ** 2 + b ** 2 < c ** 2) or (b ** 2 + c ** 2 < a ** 2) or (a ** 2 + c ** 2 < b ** 2): # sprawdzamy, czy suma dwóch boków nie jest
#         # mniejsza od najdłuższego boku. Jeśli tak, tzn. mamy trójkąt rozwartokątny.
#         print("rozwartokątny.")
#     else:
#         print("ostrokątny") # i wiadomo, że jeśli nie jest prostokątny, ani rozwartokątny, to zostaje nam ostatnia możliwa opcja, czyli
#         # trojkąt ostrokątny
#
# else: # Zwróćmy uwagę teraz na wcięcia u góry i tej linii kodu. Jak widać tamte u góry zaczynały się po użyciu tabulatora 'tab',
#     # czyli oznaczają, że są tak jakby podlinią głównej linii, czyli linii 35(ona określa, czy wogóle z tych podanych wymiarów boków można
#     # zbudować trojkąt - jeśli tak, to mamy warunkowanie=sprawdzenie jaki rodzaj trójkąta, jaki kąt -- czyli linie po 'tab-ie').
#     # ALe jeśli nie można zbudować trójkąta, z podanych boków przez użytkowanika programu, to program tych warunków=sprawdzeń już nie wykonuje,
#     # tylko przechodzi do kolejnej głównej linii kończącej go (linia 68) i informuję, że "Niestety z tych odcinków nie powstanie trójkąt!" -
#     print("Niestety z tych odcinków nie powstanie trójkąt!")

