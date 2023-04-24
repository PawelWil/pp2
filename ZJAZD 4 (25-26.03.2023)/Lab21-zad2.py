# Laboratorium 21 - zad. 2

# Korzystając z napisanej wcześniej klasy Stack:
# • utwórz 3 stosy (3 obiekty klasy Stack),
# • połóż na pierwszym stosie kolejno liczby od 1 do 100,
# • ściągaj kolejne elementy (liczby) z pierwszego stosu i umieszczaj na drugim,
# • ściągaj kolejne elementy z drugiego stosu i umieszczaj na trzecim,
# • ściągaj i wyświetlaj w tej samej linii elementy z trzeciego stosu.


class Stack:  # definiujemy klasę stosu

    def __init__(self):  # definiujemy konstruktor
        # print("Cześć!") # 1. przykładowe wyswietlenie
            self.__stack_list = []  # jak są 2 x underscores : __ to jest to traktowane jako stos prywatny

    def push(self, val):  # teraz definiujemy metodę push
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
    def show(self):
        print(self.__stack_list)



class StackSum(Stack):  # to dodajemy zeby byla suma
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


# utwórz 3 stosy (3 obiekty klasy Stack),
s1 = Stack()
s2 = Stack()
s3 = Stack()


for i in range (1, 101):
    s1.push(i)
s1.show() # tu nie działa bo trzeba dodać to show - z filmiku wyczaić gdzie

for i in range (100):
    s2.push(s1.pop())
s2.show()

for i in range (100):
    s3.push(s2.pop())
s3.show()


for i in range (100):
    print(s3.pop(), end=" ")


