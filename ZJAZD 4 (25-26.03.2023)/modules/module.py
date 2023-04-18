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


# ------------ Tworzymy moduł do obslugi Totolotka: losujemy 6 liczb z 49
# wziac z filmiku opis tego kodu!
# from random import sample
#
#
# def draw_numbers():  # losujemy 6 liczb z 49
#     numbers = [i for i in range(1, 50)]
#     lucky_numbers = sample(numbers, 6)
#     lucky_numbers.sort()
#     return lucky_numbers
#
#
# def get_user_numbers():  # pobieramy liczby od uzytkownika
#     n = 6
#     counter = 1  # zli
#     user_numbers = []
#     while counter < n + 1:
#         try:
#             number = int(input("Podaj " + str(counter) + " liczbę(1-49): "))
#             if number in user_numbers:  # zabezpieczenie na wypadek podania tej samej liczby
#                 print("Powtórzona liczba!")
#                 continue
#             if number < 1 or number > 49:
#                 print("Należy podać liczbę z przedziału 1-49!")
#                 continue
#         except:
#             print(("To nie jest liczba"))
#             continue
#
#         user_numbers.append(number)
#         counter += 1
#     user_numbers.sort()
#     return user_numbers
#
#
# def check_numbers(user_numbers, lucky_numbers):
#     counter = 0
#     for number in user_numbers:
#         if number in lucky_numbers:
#             counter += 1
#     return counter
#
#
# if __name__ == "__main__":
#     user_numbers = get_user_numbers()
#     lucky_numbers = draw_numbers()
#     result = check_numbers(user_numbers, lucky_numbers)
#     print(user_numbers)
#     print(lucky_numbers)
#     print(result)