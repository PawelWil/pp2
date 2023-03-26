# Laboratorium 22 - zad. 3

# Napisz klasę reprezentującą obiekty typu książka, w tym celu:
# • stwórz klasę Book z odpowiednimi właściwościami i metodami,
# • stwórz kilka przykładowych egzemplarzy tej klasy,
# • zademonstruj działanie wybranych metod na przykładowych egzemplarzach.


class Book:
    def __init__(self, title, author, publisher, year):
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__year = year

    def show_short_info(self):
        print("Tytul: ", self.__title, "Autor: ", self.__author)

    def show_full_info(self):
        print("Tytul: ", self.__title, "Autor: ", self.__author, "wydawca:", self.__publisher, "rok wydania", self.__year)

books = []
books.append(Book("dzieci", "Astrid", "Wyd. Nasza Ksiegarnia", 2014))
books.append(Book("Moby dick", "Herman", "Wyd. Amercome", 2009))
books.append(Book("Python wprowadzenie", "Mark Lutz", "Wyd. Helion", 2022))

# full info
for b in books:
    b.show_full_info()

# lub skrótowe info
for b in books:
    b.show_short_info()