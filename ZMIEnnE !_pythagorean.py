# to jest twierdzenie Pitagorasa

a = 4. # zmienne typu float
b = 3.

c = (a ** 2 + b ** 2) ** .5 # c=a2 + b2 do pierwiastka, czyli do potęgi 1/2, czyli w kodzie do potęgi 0.5=.5

print("Długość przeciwprostokątnej trójkąta o przyprostokątnych", a, "oraz", b, "wynosi", c, ".")
# ważna uwaga - zmienne już w kodzie zawsze wpisuje bez apostrofów, czy cudzysłowów!!

#teraz z użyciem concatenacji
print("Długość przeciwprostokątnej trójkąta o przyprostokątnych" + str(a) + "oraz" str (b) + "wynosi" + str (c), ".")