# Laboratorium 23 - zad. 3

# Zaprojektuj klasę produktu sklepu internetowego wg wytycznych:
# • stwórz klasę o nazwie Product,
# • dodaj (prywatne) właściwości jak nazwa, kategoria, cena, rabat w procentach,
# • dodaj metodę obliczającą cenę uwzględniającą rabat,
# • dodaj metodę sprawdzającą przynależność produktu do danej kategorii,
# • dodaj metodę reprezentującą obiekt klasy jako ciąg znaków.
# Dodatkowo stwórz grupę produktów z kilku kategorii, ustaw rabat dla produktów z jednej
# kategorii i wyświetl listę produktów.


class Product:
    def __init__(self, name, category, price):
        self.__name = name
        self.__category = category
        self.__price = price
        self.__discount_in_percent = 0

    def set_discount_in_percent(self, discount_in_percent):
        self.__discount_in_percent = discount_in_percent

    def get_current_price(self):
        result = self.__price * (1 - self.__discount_in_percent / 100)
        return round(result, 2)

    def  is_category(self, category):
        return self.__category == category

    def  __str__(self):
        return "{} ({}) - {} zł".format(self.__name, self.__category, self.get_current_price())


def show_products(products):
    for p in products:
        print(p)


def special_offer(products, category, discount_in_percent):
    for p in products:
        if p.is_category(category):
            p.set_discount_in_percent(discount_in_percent)


products = []
products.append(Product("mleko", "spozywcze", 3.99))
products.append(Product("masło", "spozywcze", 6.56))
products.append(Product("jogurt", "spozywcze", 0.99))
products.append(Product("Płyn do naczyń", "chemia", 4.50))


# -----cos mi tu źle podlicza rabat - sprawdzic na filiku!!!!!!!!!!!!!!!!
# ciekawy serwer, gdzie jest duzo kodów: www.codewars.com - tu mozna rozwiązywac różne skrypty

show_products(products)
special_offer(products, "spozywcze,", 30)
print("\nPromocja\n-------------")
show_products(products)