# Laboratorium 22 - zad. 1

# Rozbuduj klasę Employee o mechanizm zwiększania wynagrodzeń:
# • dodaj metodę risesalary(),
# • metoda powinna zwiększać zarobki o podaną wartość procentową,
# • domyślnie metoda powinną zwiększać zarobkio 10%.

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

    def risesalary(self, percent=10):
        self.__salary *= percent / 100 + 1 # 100 * 1.10

def payroll(employes):
    print("Lista płac")
    print("-" * 50)

    for e in employees:
        print(e.getfullname(), "wiek: ", e.getage(), "lat, pensja:", e.getsalary(), "zł")



employees = []
employees.append(Employee("Jan", "Kowalski", 25, 3800))
employees.append(Employee("Edmund", "Kaczmarczyk", 45, 7000))
employees.append(Employee("Natalia", "Nowak", 60, 15200))

payroll(employees)
employees[0].risesalary()
employees[2].risesalary((30))
payroll(employees)








# ---- MOje rozwiązanie--

# class Employee:
#     def __init__(self, firstname, lastname, age, salary, risesalary):
#         self.__firstname = firstname
#         self.__lastname = lastname
#         self.__age = age
#         self.__salary = salary
#         self.__risesalary = risesalary
#
#     def getsalary(self):
#         return self.__salary
#
#     def getfullname(self):
#         return self.__firstname +  " " + self.__lastname
#
#     def getage(self):
#         return self.__age
#
#     def getrisesalary(self, salary=1.1):
#         __risesalary = 1.1 * salary
#         return self.__risesalary
#
# employees = []
# employees.append(Employee("Jan", "Kowalski", 25, 3800, 3800 * 1.1))
# employees.append(Employee("Edmund", "Kaczmarczyk", 45, 7000, round(7000 * 1.1, 2)))
# employees.append(Employee("Natalia", "Nowak", 60, 15200, 15200 * 1.1))
#
# print("Lista płac")
# print("-" * 50)
#
# for e in employees:
#     print(e.getfullname(), "wiek: ", e.getage(), "lat, pensja:", e.getsalary(), "zł", ". Zarobki się zwiększą o 10%, czyli : ", e.getrisesalary() - e.getsalary(), "zł", " i będą wynosić:", e.getrisesalary() )
