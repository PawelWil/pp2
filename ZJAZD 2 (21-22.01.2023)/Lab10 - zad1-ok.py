# # ZAD. 1
#
# Napisz skrypt, pobierający od użytkownika zbiór imion, w tym celu:
# • skrypt powinien zapytać użytkownika o liczbę elementów zbioru,
# • pobrać kolejne elementy i zapisać je do listy,
# • wyświetlić w podsumowaniu jakie imiona pobrał od użytkownika.


# ROZWIĄZANIE PANA MARCINA:
names  = [] # to jest zmienna na imiona
name_number = int(input("Podaj liczbę imion: "))

for i in range(1, name_number + 1): #tu to 1 przed zmienną name_number jest po to żeby liczenie nie zaczęło się od bitu liczby 0, a od 1 - gdyby było bez tego, to jakbym podał liczbe imion 3, to by mi naliczyło 4 imiona, bo zaczeło by liczyć od 0, czyli 0=imie 1, 1=imie 2, 2=imie 3, 3=imie 4
    names.append(input("Podaj " + str(i) + " imię: "))

print ("Od użytkowanika pobrano nastepujace imiona: ", names)


