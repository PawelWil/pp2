# ZAD 3
# Napisz grę w zgadywanie liczby z przedziału od 1 do 10. Gracz powinien dostać
# 3 szanse. Po nieudanej próbie, gracz powinien otrzymać podpowiedź np.
# o parzystości zgadywanej liczby itp.


import random

number = random.randint(1, 10)
msg = "Zgadnij jaką liczbę mam na myśli (od 1 do 10) :"
guess = int(input(msg))
if guess == number:
    print("brawo! Dokładnie taką liczbę miałem na myśli!")
else:
    msg = "Masz kolejną szansę :"
    if number % 2 == 0:
        msg += " twoja liczba jest parzysta: "
    else:
        msg += " twoja liczba jest nieparzysta: "
    guess = int(input(msg))
    if guess == number:
        print("Brawo! Udało się odgadnąć za drugim razem!")
    else:
        msg = "Masz kolejną szansę :"
        if number > 5:
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