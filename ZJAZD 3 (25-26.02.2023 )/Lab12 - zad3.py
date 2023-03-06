# LAB 12, ZAD.3

# Napisz program obliczającej wskaźnik BMI (Body Mass Index), w tym celu:
# • zapytaj użytkownika o wzrost i wagę,
# • stwórz funkcję obliczającą wskaźnik BMI na podstawie podanych przez użytkownika danych,
# • stwórz funkcję wyznaczającą odpowiednią kategorię (niedowaga, waga prawidłowa, nadwaga,
# otyłość) na podstawie wskaźnika BMI,
# • zaprezentuj wyniki korzystając z wcześniej przygotowanych funkcji.


# jak się liczy wskaźnik BMI:
# BMI = masa / (wzrost)**2

# 1. zapytaj użytkownika o wzrost i wagę,

print ("Obliczanie wskaźnika BMI")
weight_in_kg = float (input("podaj swoją wagę w kg:")) # to dajemy liczbe zmiennprzecinkową, bo moze byc np 55,5 kg
height_in_cm = float (input("podaj swoj wzrost w cm:"))

# print(weight_in_kg, height_in_cm)  # to jest print testowy

# 2. stwórz funkcję obliczającą wskaźnik BMI na podstawie podanych przez użytkownika danych
def calculate_bmi(weight_in_kg, height_in_m):
    return weight_in_kg / height_in_m ** 2

print(calculate_bmi(weight_in_kg, height_in_cm * 0.01)) # height_in_cm * 0.01 - to jest przeliczenie na metry


# 3.  stwórz funkcję wyznaczającą odpowiednią kategorię (niedowaga, waga prawidłowa, nadwaga,
# # otyłość) na podstawie wskaźnika BMI,

def determine_bmi_category(bmi):
    if bmi < 18.5:
        return "niedowaga" # zwracamy, coś podobnego co print
    elif bmi < 25:
        return "waga prawidlowa"
    elif bmi <30:
        return "nadwaga"
    else:
        return "otylosc"

# 4. • zaprezentuj wyniki korzystając z wcześniej przygotowanych funkcji.

bmi = calculate_bmi(weight_in_kg, height_in_cm * 0.01)
category = determine_bmi_category(bmi)

print ("Wskaznik BMI: ", bmi)
print ("Kategoria: ", category)



