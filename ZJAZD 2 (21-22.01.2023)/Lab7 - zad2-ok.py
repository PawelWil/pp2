#  ZAD. 2
# Napisz skrypt wyznaczający ocenę jaką otrzyma student, ze względu na ilość
# otrzymanych punków z kolokwium:
# • ocena bardzo (5,0) dobra, jeżeli student otrzymał 95 lub więcej punktów,
# • jeżeli punktów jest mniej niż 95, ale więcej niż 84 studentowi przysługuje ocena ponad dobra
# (4,5),
# • ocena dobra (4,0) przyznawana jest dla ilości punktów z przedziału [70, 84],
# • jeżeli student otrzymał więcej niż 60 ale mniej niż 70 to przysługuje mu ocena dość dobra
# (3,5),
# • ocena dostateczna jest dla studentów z punktowym wynikiem równym przynajmniej 60 ale
# powyżej 50 punktów,
# • wszystkie wyniki równe 50 i mniej punktów wiążą się z otrzymaniem oceny niedostatecznej
# (2.0).



punkty = int(input("Podaj liczbę punktów (0-100): "))# podajemy ilość punktów studenta

print("Twoja ocena jest", end=" ")

if punkty > 95:
    print ("bardzo dobra (5,0)")
elif punkty > 84:
    print("ponad dobra (4,5)")
elif punkty >= 70 :
    print("dobra (4,0)")
elif punkty > 60:
    print("ponad ponad dostateczna (3,5)")
elif punkty > 50:
    print("dostateczna (3,0)")
else: # to już koniec pętli, czyli wystąpi, gdy żadna z powyższych warunków nie zostanie spełnone
    print("niedostateczna (2,0)")

