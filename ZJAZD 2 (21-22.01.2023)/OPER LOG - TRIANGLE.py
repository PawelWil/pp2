#1. Podanie wymiarów trzech odcinków
print ("Podaj długości 3 odcinków (liczby całkowite): ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

#2. Weryfikacja, czy z tych trzech odcinków mozna zbudować trojkąt
# jezeli a + b są wieksze od c, no bo nie moga byc te boki mniejsze od c + inne wariancje też muszą być wymienione, no bo np. bok a nie może być większy od b+c oraz bok b, nie może być wiekszy od c+a
if (a+b > c and b+c > a and c+ a > b):
    print("Z tych odcinków można zbudować trójkat", end=" ")\

# teraz oceniamy jaki jest trójkąt, czy: równoboczny, równoramienny, różnoboczny
    # teraz robimy na równoboczność:
    # if a== b and a==c and c ==b:
    #     print("równoboczny", end=" ")
    # elif a == b or b == c or c ==a: #dajemy elif, bo nie mamy dwóch przypadków(czyli else), tylko trzy
    #     print("Trojkat rownoramienny", end = " ")
    # else:
    #     print("Trojkat rożnoramienny", end = " ")

# teraz oceniamy jaki jest trójkąt, ze względu na katy, czy: prostokatny, rozwartokatny, ostrokatny
    # teraz robimy czy jest prostokatny:
    if (a ** 2 + b ** 2 == c ** 2) or (b ** 2 + c ** 2 == a ** 2) or (a ** 2 + c ** 2 == b ** 2): # za pomocą tego twierdzenie Pitagorasa sprawdzamy, czy trojkat prostokatny - czyli jak to jest spełnione to trojkat prostokatny
        print("prostokatny.")
    # teraz sprawdzamy, czy rozwartokatny ostrokatny:
    if (a ** 2 + b ** 2 < c ** 2) or (b ** 2 + c ** 2 < a ** 2) or (a ** 2 + c ** 2 < b ** 2): # sprawdzamy, czy suma nie jest mniejsza
        print("rozwartokątny.")
    else:
        print("ostrokątny")

else: # gdy coś nie jest spełnione
    print("Niestety z tych odcinków nie powstanie trójkąt!")

