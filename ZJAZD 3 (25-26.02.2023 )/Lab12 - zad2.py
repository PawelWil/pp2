# LAB 12, ZAD.2

# Napisz skrypt obliczający obwód, pole powierzchni i długość przekątnej dla
# prostokątów o następujących długościach boków:
# • 4 i 5,
# • 2678 i 5678,
# • 344555 i 788998


# tworzymy kilka funcji:

# 1 funkcja - liczy obwód prostokąta:

def perimiter(a, b):
    return 2 * a + 2 * b #dodajemy liczenie obwodu

# 2 funkcja - liczy pole pow prostokąta:

def surface_area(a, b):
    return a * b

# 3 funkcja - dług przekatnej prostokąta_z tw. Pitagorasa:
def diaganol_length(a, b):
    return (a **2 + b**2) ** .5
    # lub tak
    # return (a ** 2 + b ** 2) ** (1/2)

# teraz pokazujemy rezulataty za pomocą jednej funkcji:

def show_result (a, b):# z niej wywolujemy inne funkcje
    print ("Prostokąt o bokach:", a, "i", b)
    print("Owbód:", perimiter(a, b))
    print("Pole powierzchni:", surface_area(a, b))
    print("Długość przekątnej:", diaganol_length(a, b))
    print()

show_result(4, 5)
show_result(2678, 5678)
show_result(344555, 788998)