# --
# class MyClass:
#     def __init__(self, x=1):
#         self.x = x
#
#     def sety(self, y):
#         self.y = y
#
#
# obj1 = MyClass()  # ustawiamy włascwosci x, na x=1
#
# obj2 = MyClass(4)  # ustawiamy własciwosc x, na x=4
# obj2.sety (7)  # ustawiamy własciwosc y, na y=7
#
# obj3 = MyClass(3)
# obj3.z = 99  # dodajemy nową własciwosc, którą ustawiamu na z=99
#
# print(obj1.__dict__)
# print(obj2.__dict__)
# print(obj3.__dict__)


# --
# class MyClass:
#     def __init__(self, x=1):
#         self.__x = x # prywatna zmienna instancji
#
#     def sety(self, y):
#         self.__y = y # prywatna zmienna instancji
#
#
# obj1 = MyClass()  # ustawiamy włascwosci x, na x=1
#
# obj2 = MyClass(4)  # ustawiamy własciwosc x, na x=4
# obj2.sety(7)  # ustawiamy własciwosc y, na y=7
#
# obj3 = MyClass(3)
# obj3.z = 99  # dodajemy nową własciwosc, którą ustawiamu na z=99
#
# print("obj1", obj1.__dict__)
# print("obj2", obj2.__dict__)
# print("obj3", obj3.__dict__)
#
# print(obj1._MyClass__x)


#---class MyClass:

# class MyClass:
#     counter = 0 # zmienna klasy, wspolna dla całej klasy obiektu
#     def __init__(self, x=1):
#         self.__x = x
#         MyClass.counter += 1
#
# obj1 = MyClass(1)
# obj2 = MyClass(2)
# obj3 = MyClass(77)
#
#
# print(obj1.__dict__, obj1.counter)
# print(obj2.__dict__, obj2.counter)
# print(obj3.__dict__, obj3.counter)
#
# print("Ile obiektów?", MyClass.counter)


#--- NIe działa coś
# class MyClass:
#     __counter = 0 # zmienna klasy, wspolna dla całej klasy obiektu
#     def __init__(self, x=1):
#         self.__x = x
#         MyClass.__counter += 1
#
# obj1 = MyClass(1)
# obj2 = MyClass(2)
# obj3 = MyClass(77)
#
#
# print(obj1.__dict__, obj1.MyClass__counter)
# print(obj2.__dict__, obj2.MyClass__counter)
# print(obj3.__dict__, obj3.MyClass__counter)
#
# print("Ile obiektów?", MyClass._MyClass__counter)


#---
# class MyClass:
#
#     def __init__(self, x=1):
#         if x % 2 == 0:
#             self.a = x
#         else:
#             self.b = x
#
#
#
# obj = MyClass ()
# print((obj.__dict__))
#
#
# if hasattr(obj, "a"):
#     print((obj.a))
# else:
#     print(obj.b)


#-----
# class MyClass:
#
#     def __init__(self, x=1):
#         if x % 2 == 0:
#             self.a = x
#         else:
#             self.b = x
#
#
# class A:
#     x = 1
#
# obj = MyClass ()
#
#
# if hasattr(obj, "a"):
#     print((obj.a))
# else:
#     print(obj.b)
#
# obj2 = A()
# print(hasattr(A, "y"))
# print(hasattr(A, "x"))




#---------- realizacja zbioru pracowników
class Employee:
    def __init__(self, firstname, lastname, age, salary):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        self.__salary = salary

    def getsalary(self):
        return self.__salary

    def getfullname(self):
        return self.__firstname +  " " + self.__lastname

    def getage(self):
        return self.__age

employees = []
employees.append(Employee("Jan", "Kowalski", 25, 3800))
employees.append(Employee("Edmund", "Kaczmarczyk", 45, 7000))
employees.append(Employee("Natalia", "Nowak", 60, 15200))

print("Lista płac")
print("-" * 50)

for e in employees:
    print(e.getfullname(), "wiek: ", e.getage(), "lat, pensja:", e.getsalary(), "zł")



