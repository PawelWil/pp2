# ZAD 3
# Napisz grę w zgadywanie liczby z przedziału od 1 do 10. Gracz powinien dostać
# 3 szanse. Po nieudanej próbie, gracz powinien otrzymać podpowiedź np.
# o parzystości zgadywanej liczby itp.

# Rozwiązanie Pana MArcina -- !! sprawdzić ten kod jeszcze z filmikiem, bo coś nie do końca działa!!

import random # to jest ściągnięcie biblioteki, która jest mechanizmem do loswaonia liczb (jakichs znaków)

number = random.randint(1, 10)# ona nam losuje liczbę z przedziału jaki jej podamy, czyli w naszym przypadku, z przdziału od 1 do 3
msg = "Zgadnij jaką liczbę mam na myśli (od 1 do 10) :"  # zmienna która nam poda jaka liczbę mamy na mysli
guess = int(input(msg))
if guess == number:
    print("brawo! Dokładnie taką liczbę miałem na myśli!")
else:
    msg = "Masz kolejną szansę :" # to jest druga szansa
    if number % 2 == 0:# to już jest trzecia szansa, czyli podpowiedz, o parzystości
        msg += " twoja liczba jest parzysta: "
    else:
        msg += " twoja liczba jest nieparzysta: "
    guess = int(input(msg))
    if guess == number:
        print("Brawo! Udało się odgadnąć za drugim razem!")
    else:
        msg = "Masz kolejną szansę :"  # to jest druga szansa
        if number > 5:  # to już jest trzecia szansa, czyli podpowiedz, o parzystości
            msg += "moja liczba jest większa"
        else:
            msg += "moja liczba jest mniejsza lub równa"
        msg += " od liczby 5: "
        guess = int(input(msg))
    if guess == number:
        print("Brawo! A jednak do trzech razy sztuka")
    else:
        msg = "Niestety myślałem o liczbie :" + str(number) + "."
        print(msg)