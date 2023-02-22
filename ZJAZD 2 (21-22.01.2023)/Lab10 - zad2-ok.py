# LABORATORIUM 10 - ZAD 2

# # ZAD. 2
# Napisz program, który zasymuluje 16 rzutów kostką do gry a następnie
# wyświetli poniższe informacje:
# • zestaw wylosowanych wyników,
# • wyrzucaną wartość za 8 razem,
# • liczbę wyrzuconych szóstek,
# • maksymalną liczbę wyrzuconych tych samych wartości pod rząd.



# ROZWIĄZANIE PANA MARCINA:

import random

dice_rolls_total = 16 #definuijemy stałą, w której będziemy przechowywać ilośc rzutów kostką - ma być 16
rolls = [] # tu przechowujemy listę wylosowanych oczek

for i in range (dice_rolls_total):
    rolls.append(random.randint(1, 6))
print ("Zbior wyników po", dice_rolls_total, "rzutach kostką do gry:", rolls) # to jest podpunkt 1

print ("Za 8 razem wyrzucono wartość", rolls[8 - 1] ) # to jest podpunkt 2 bez kropki po wartosc
print ("Za 8 razem wyrzucono wartość", str(rolls[8 - 1]) + "." ) # to jest podpunkt 2, ale z kropką po 'wartość'

# podpunkt 3
sixes_total = 0 # na początku tą zmienną pomocniczą ustawiamy na 0
for roll in rolls:
    if roll == 6:
        sixes_total += 1 # to jestzwiakszenie za pomoca opreattoar '+=' o 1
print("Wyrzucono", sixes_total, "razy szostke")

# podpunkt 4
in_row_value_tmp = rolls[0] #zmienna pod rząd, ale pomocnicza = tmp=temporary
in_row_total_tmp = 0 # pod rząd total, tez pomocnicza = tmp=temporary

in_row_value = 0 #tu juz nie pomocnicze, tylko koncowe
in_row_total = 0 # tu juz nie pomocnicze, tylko koncowe

for roll in rolls:
    if(roll == in_row_value_tmp):
        in_row_total_tmp += 1 # in_row_total_tmp zwiaksza sie za pomoca opreattoar '+=', o 1
    else:
        in_row_value_tmp = roll
        in_row_total_tmp = 1
    if in_row_total_tmp > in_row_total:
        in_row_total = in_row_total_tmp
        in_row_value = in_row_value_tmp

print ("Pod rząd wyrzucono: ", in_row_total, "razy wartość", in_row_value)
print ("Pod rząd wyrzucono: ", in_row_total, "razy wartość", str(in_row_value) + ".") # to jest to samo co u góry, ale z kropką po "wartość"
