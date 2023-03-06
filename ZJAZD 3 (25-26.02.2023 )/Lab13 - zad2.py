# Lab 13 - Zad.2
# Korzystając z rekurencji wypisz na ekranie tabliczkę mnożenie do 100.


def show_operation(a, b): # funkcja będzie miala argumenty a i b, czyli mnożymy coś przez coś
    print(a, "x", b, "=", a * b )
    if a == 10 and b==10: # to jest mnozenie do 100, dlatego ttrzeba się na tym zatrzymac
        return
    elif a == 10:
        show_operation(1, b+1)
    else:
        show_operation(a + 1, b)


show_operation(1, 1) # tu mnożymy liczby od 1 do 100 zaczynając od 1



