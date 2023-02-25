# Kolokwium 2:
# Pobierz od użytkownika trzy liczby całkowite reprezentujące długości odcinków i sprawdź czy jest możliwe zbudowanie z tych odcinków trójkąta prostokątnego.

print ("Podaj długości 3 odcinków (liczby całkowite): ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if (a ** 2 + b ** 2 == c ** 2) or (b ** 2 + c ** 2 == a ** 2) or (a ** 2 + c ** 2 == b ** 2):  # za pomocą tego twierdzenie Pitagorasa sprawdzamy, czy trojkat prostokatny - czyli jak to jest spełnione to trojkat prostokatny
    print("prostokatny.")

else:
    print("Niestety z tych odcinków nie powstanie trójkąt prostokątny!")