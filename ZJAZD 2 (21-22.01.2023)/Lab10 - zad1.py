# # ZAD. 1
#
# Napisz skrypt, pobierający od użytkownika zbiór imion, w tym celu:
# • skrypt powinien zapytać użytkownika o liczbę elementów zbioru,
# • pobrać kolejne elementy i zapisać je do listy,
# • wyświetlić w podsumowaniu jakie imiona pobrał od użytkownika.


# ROZWIĄZANIE PANA MARCINA:
names  = [] # to jest zmienna na imiona
total_elements = int(input("Podaj liczbę imion: "))

for i in range(1, total_elements + 1):
    names.append(input("Podaj " + str(i) + " imię: "))

print ("Od uztkowanika pobrano nastepujace imiona: ", names)




# MOJE ROZWIĄZANIE
# name_number = int(input("Podaj ilość imion: "))
# names = []
#
# for i in range (name_number):
#     name = input ("podaj imię: ")
#     names.append(names)
#
# for i in range (len(names)):
#     print (name)

