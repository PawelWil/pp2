# ZAD. 2
# Napisz skrypt wyświetlający na ekranie macierz. Rozmiar macierzy oraz
# znak z jakiej będzie zbudowana powinien określić użytkownik

number = int(input("Podaj rozmiar: "))
char = input ("Podaj znak:")

for i in range(number):
    for j in range(number):
        print(char, end=" ")
    print()