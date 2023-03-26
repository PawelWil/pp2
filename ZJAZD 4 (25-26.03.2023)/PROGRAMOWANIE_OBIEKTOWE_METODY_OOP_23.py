# -----

# class MyClass:
#
#     def my_method(self, x):
#         print("To jest moja metoda z parametrem: ", x)
#
# obj = MyClass()
# obj.my_method(123)
# obj.my_method("aaa")


# ------
# class MyClass:
#     y=99
#
#     def my_method(self, x):
#         print("To jest moja metoda z parametrem: ", x, "i zmienną klasy", self.y)
#
# obj = MyClass()
# obj.my_method(123)
# obj.my_method("aaa")


# ------
# class MyClass:
#     y=99
#
#     def my_method(self, x):
#         self.other_method() # odwołanie do innej metoday za pmocą self
#         print("To jest moja metoda z parametrem: ", x, "i zmienną klasy", self.y)
#
#         print()
#
#     def other_method(self):
#         print("To jest metoda", self.y)
#
# obj = MyClass()
# obj.my_method(123)
# obj.my_method("aaa")

# #------
# class MyClass:
#
#     def __init__(self, name):
#         self.__name = name
#         print("Inincjalizuje obiekt!", name )
#
#     def getname(self):
#         return self.__name
#
# obj = MyClass("Marcin")
#
# print("Mam na imie", obj.getname())


# ------ Cos nie działa
# class MyClass:
#
#     def __my_private_method(self):
#        print("To jest metoda prywatna...")
#
#     def __my_public_method(self):
#         self.__my_private_method()
#         print("To jest metoda publiczna...")
#
# obj = MyClass()
# # obj.__my_private_method() #ak nie zadziała, bo metoda prywatna
# obj.my_public_method


# ------ Cos nie działa
# class MyClass:
#
#     def __my_private_method(self):
#        print("To jest metoda prywatna...")
#
#     def __my_public_method(self):
#         self.__my_private_method()
#         print("To jest metoda publiczna...")
#
# obj = MyClass()
# # obj.__my_private_method() #ak nie zadziała, bo metoda prywatna
# obj.my_public_method()
#
# print()
#
# print(obj.__dict__)
# print(MyClass.__dict__)


# ----My class
# ------ Cos nie działa
# class MyClass:
#
#     def __my_private_method(self):
#        print("To jest metoda prywatna...")
#
#     def __my_public_method(self):
#         self.__my_private_method()
#         print("To jest metoda publiczna...")
#
# obj = MyClass()
# # obj.__my_private_method() #ak nie zadziała, bo metoda prywatna
# obj.my_public_method()
#
# print()
#
# print(obj.__dict__)
# print(MyClass.__dict__)

# print()
# print(MyClass.__name__)
# print(type....)
#
# print(MyClass.__module__)


# ----------Właściwość bases = dziedziczenie

# class A:
#     pass
#
# class B:
#     pass
#
# class C(A, B):
#     pass
#
# print(C.__bases__)
#
#
# # iteracja po klassach
# for c in C.__bases__:
#     print(c.__name__)


# -----------INTROSPEKCJA i REFLEKSJA -- coś nie działa mi to

# class MyClass:
#     x = 5
#
#     def __init__(self):
#         self.y = 9
#
#
# obj = MyClass
# print(obj.x, obj.y)
#
# print(MyClass.__dict__)
# print(obj.__dict__)
# print()
#
# setattr(obj, "z", 1)
#
# print(getattr(obj, "x"))
#
# print("z", obj.z)



#----- ZAD. Program symulujący rzyut dwoma kostkami za pomocą metody obiektowej

import random

class Dice:  # dice = kostka
    def __init__(self):
        self.value = None

    def throw(self):
        self.value = random.randint(1, 6)

    def __str__(self):
        return "[{}]".format(self.value) # mozna tez to zapisac tak:   "[" + self.value + "]"




class DicePair:

    def __init__(self):
        self.pair = [Dice(), Dice()]

    def throw(self):
        self.pair[0].throw()
        self.pair[1].throw()

    def is_double(self):
        return self.pair[0].value == self.pair[1].value

    def __str__(self):
        return str(self.pair[0]) + str(self.pair[1])

dices = DicePair()
while True:
    dices.throw()
    print(dices)
    if dices.is_double():
        break