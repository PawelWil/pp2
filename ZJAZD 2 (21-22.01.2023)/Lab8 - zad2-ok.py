# LABORATORIUM 8 - ZAD 2
# Napisz skrypt wyświetlający na ekranie macierz. Rozmiar macierzy oraz
# znak z jakiej będzie zbudowana powinien określić użytkownik

# ROZWIĄZANIE PANA MARCINA:

number = int(input("Podaj rozmiar: "))
char = input ("Podaj znak:") # to jest zmienna o nazwie 'czar'

# teraz potrzebujemy mechanimz do wygenerowania macierzy
for i in range(number):
    for j in range(number): # zmieniam nazwę zmiennej iteracyjenj
        print(char, end=" ")
    print()