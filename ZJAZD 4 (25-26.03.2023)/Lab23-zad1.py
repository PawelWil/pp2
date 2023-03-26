# Laboratorium 23 - zad. 1

# Zaprojektuj klasę reprezentującą osobę (Person) wg założeń:
# • każdy obiekt tej klasy powinien posiadać właściwości: imię oraz wiek,
# • zabezpiecz właściwości obiektu przed przypadkowym nadpisaniem,
# • ustawienie odpowiednich właściwości obiektu powinno następować podczas jego tworzenia,
# • każdy obiekt tej klasy powinien móc wykonać akcję przedstawienia się.


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def  introduce(self):
        print("Cześć, jestem", self.__name, "i mam", self.__age, "lat.")

persons = []
persons.append(Person("jan", 20))
persons.append(Person("agata", 34))
persons.append(Person("tomek", 55))
persons.append(Person("Monika", 14))

for  p in persons:
    p.introduce()