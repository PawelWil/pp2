## ZADANIE 2 - LAB 16

# Napisz, przetestuj i zastosuj własny moduł do obsługi list liczb całkowitych:
# • stwórz modułu o dowolnej nazwie,
# • dodaj funkcję weryfikującą czy podana lista zawiera wyłącznie liczby całkowite,
# • dodaj funkcję sumującą wszystkie liczby z listy,
# • dodaj funkcję zwracającą iloczyn wszystkich liczb z listy,
# • dodaj testy weryfikujące poprawne działanie napisanych funkcji,
# • zaimportuj utworzony moduł i skorzystaj z jego funkcji.

###! NIestety nie działa :(

# • stwórz modułu o dowolnej nazwie
# moduł tworze poprzez utworzenie nowego katalogu. W tym przypadku to jest 'Lab 16 - zad2'

# • dodaj funkcję weryfikującą czy podana lista zawiera wyłącznie liczby całkowite,
def is_list_of_integers(list):
    for i in list:
        if not isinstance (i, int):
            return False
    return True



# • dodaj funkcję sumującą wszystkie liczby z listy,
def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return  sum



#• dodaj funkcję zwracającą iloczyn wszystkich liczb z listy,
def product_list(list):
    product = 1
    for i in  list:
        product = product * i
    return product



# • dodaj testy weryfikujące poprawne działanie napisanych funkcji,
if __name__ == "__main__":
    list = [1,2,3]
    print(is_list_of_integers(list) == True)
    print(is_list_of_integers(["a", "b", "c"]) == False)
    print(sum_list(list) == 6)
    print(sum_list(list) =! 7)
    print(sum_list(list) == 6)