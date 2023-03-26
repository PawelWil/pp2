# class MyClass: # tworzenie klasy
#     pass
# #
# #
# my_obj = MyClass() # tworzenie obiektu
# my_obj.x = 5 # obiekt ma własciwość x i wartość 5
# #
# print(my_obj.x)
# print(type(my_obj)) # jaki typ obiektu
#
# my_obj2 = MyClass()# kolejny obiekt cklasy main class
# my_obj2.x = 99
# print(my_obj2.x)
#
# print(my_obj.x, my_obj2.x) # wartosci obiektów w jednej lini, mimo tego ze wslasciwosci raze x, ale mają inne wartośco 5 i 99


# -------Piszemy skrypt implementujący stos klasycznie:

# stack = [] # najlepsza jest lista na przechowywanie elelmentow stosie
# def push (val):#funkcja push wrzuca elelm na stosie/do stosu
#     stack.append(val)
#
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val
#
# push(3)
# push(2)
# push(1)
#
# print(stack)

# ---- wyciaganie elelntów ze stosu 'POP'
# stack = [] # najlepsza jest lista na przechowywanie elelmentow stosie
# def push (val):#funkcja push wrzuca elelm na stosie/do stosu
#     stack.append(val)
#
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val
#
# push(3)
# push(2)
# push(1)
#
# print(pop())
# print(pop())
# print(pop())


# ---------------Tworzenie kolejnego stosu/kolejnych stosów(np.2000) - tu wykorzyystujemy OOP = object oriented programming: -----------

# class Stack: # definiujemy klasę stosu
#     def __init__(self): # definiujemy konstruktor
#         # print("Cześć!") # 1. przykładowe wyswietlenie
#         self.__stack_list = [] # jak są 2 x underscores : __ to jest to traktowane jako stos prywatny
#
#     def push (self, val):# teraz definiujemy metodę push
#         self.__stack_list.append(val)
#
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
# # ----
# obj = Stack()
# obj2 = Stack()
# obj3 = Stack()
#
#
# obj.push (3)
# obj.push (2)
# obj.push (1)
#
# obj2.push (4)
# obj2.push (4)
# obj2.push (4)
#
# obj3.push ("ania")
# obj3.push ("zosia")
# obj3.push ("tomek")
#
#
# print(obj2.pop())
# print(obj2.pop())
# print(obj2.pop())
#
# print(obj.pop())
# print(obj.pop())
# print(obj.pop())
#
#
# print(obj3.pop())
# print(obj3.pop())
#
# # --- tu już korzystamy z tej klasy
#
# obj = Stack()
# # obj.__stack_list = [4,4,4,]
# print()


# -----------teraz chcemy zeby nasz stos liczył dodatkowo sumę wszystkich elementów
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
        self.__sum -=val
        return val

#
# # ----
obj = StackSum()
obj2 = StackSum()
#
#
obj.push(3)
obj.push(2)
obj.push(1)
#
obj2.push(4)
obj2.push(4)
obj2.push(4)
#
print ("stos 1", obj.get_sum())
print ("stos 1", obj2.get_sum())
#
print(obj2.pop())
print(obj2.pop())
print(obj2.pop())
#
print(obj.pop())
print(obj.pop())
print(obj.pop())
#
print ("stos 1", obj.get_sum())
print ("stos 1", obj2.get_sum())
#
# # --- tu już korzystamy z tej klasy
#
# obj = Stack()
# # obj.__stack_list = [4,4,4,]
# print()
