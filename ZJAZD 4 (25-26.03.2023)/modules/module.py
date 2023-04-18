"""This is my first own module...""" #wstawiamy string, z komentarzem: 'to jest nasz pierwszy moduł', co będzie widoczne później,
# jak już się do tego modułu za pomocą funkcji import odniesiemy. I wtedy będzie widoczne: NAME=module(bo to jest nazwa tego pliku)
# + 'This is my first own module..."

# I teraz tworzymy ten moduł, który będzie miał zestaw funkcjonalności, jak poniżej:

def is_string(val): # 1 funkcja będzie sprawdzała, czy coś jest napisem lub nie jest + bedzie przyjmowała jakąś wartość='val'
    """Simple string validator""" # wstawiamy opis, że to jest prosty sprawdzacz=walidator
    return isinstance(val, str) # będzie zwracało, czy coś jest stringiem, boolinem itd., co zrealizujemy przez funkcję 'isinstance',
# gdzie przekazujemy jakąś wartość i spradzamy, czy ta wartość jest obiektem typu string

def sum_list_elem(list): # 2 funkcja to bedzie sumator liczby elemenetów listy, z parametrem 'list'
    sum = 0
    for i in list: # iterujemy sobie po liście
        sum += i
    return sum

print(__name__) # mamy tu do dyspozycji własciwość name
if __name__ == "__main__": # tu wrzucam sprawdzenie czy funkcje powyzej wprowadzone pzrze mnie dziłaja poprawnie
    print(is_string("haha") == True) # tu sprawdzamy, jesli jest strinhg, to TRUE
    print(is_string(123) == False) # jesli liczba, to wiadomo FALSE
    print(sum_list_elem([1,1,1]) == 3) #
    print(sum_list_elem([]) == 0)

