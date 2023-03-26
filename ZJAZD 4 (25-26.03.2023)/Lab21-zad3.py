# Laboratorium 21 - zad. 3

# Rozbuduj klasę Stack o następujące metody:
# • empty() - powinna zwracać True jeżeli stos jest pusty, w przeciwnym wypadku zwracać False,
# • size() - powinna zwracać rozmiar stosu,
# • top() - powinna zwracać "górny" element stosu, czyli ten, który zostanie "ściągnięty"
# metodą pop().


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

    def empty(self):
        return len(self.__stack_list) == 0

    def size (self):
        return len(self.__stack_list)

    def top (self):
        return self.__stack_list [-1]

stack = Stack()

print("Czy stos pusty?", stack.empty())

stack.push("ala")
stack.push("Tomek")
stack.push("Agata")
print("Czy stos jest pusty?", stack.empty())
print("Ile elementów jest na stosie?", stack.size())
print("Na górze stosu znajduje się:" , stack.top())

print("Ile elem jest na stosie?", stack.size())