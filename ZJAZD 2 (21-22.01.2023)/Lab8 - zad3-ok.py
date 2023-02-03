# ZAD.3
# Załóżmy, że na pierwsze pole szachownicy kładziemy 1 ziarno zboża, na
# drugie 2 ziarna, na trzecie 4 ziarna i na każde następne pole dwa razy
# więcej ziaren niż na pole poprzednie. Napisz program, który zasymuluje
# taką sytuację i zliczy sumę wszystkich ziaren na szachownicy.

# ROZWIĄZANIE PANA MARCINA:

# Szachownica ma 64 pola
 # tu bedziemy milei od 0 do 63, ale będą 64 iteracje, czyli przeszło 64 razy, tyle ile jest wymagane
 #    r = 2 ** i # ilość ziarenek, które musimy kłaść: 1 2 4 8 16 ... 2 ** i (mowa o 2 do potęgi i-tej) --> a to się równa:  0 1 2 3 4
 #    print(r)
 #    if r > 63:
 #        break

sum = 0
for i in range (64):
    sum += 2 ** i
print ("Suma wszystkich ziaren zboża na szachownicy: " + str(sum))

#  LICZYMY TERAZ ILE TO BĘDZIE TON
# 1 ziarno to: 0,4 mg (mili to jedna tysięczna grama)
# 1 ziarno to: 0,0004 g
# 1 kg = 1000g
#1t = 1000kg
tons = int
tons = int(sum * 0.0004 / 1000 / 1000) # to jest przeliczenie ziarenek po kolei z mg na g(dzielimy przez 1000), a potem na tony(dzielimy przez 1000)
print(tons)

# TERAZ LICZE ILE LAT POTZREBUJE ŻEBY TE ILOSCI zebrać
# Na bazie powyższego mamy daną, że produkcja pszenicy na świecie to ok. 782 mln ton
# years = int(tons / 782_000_000) # tu mamy 782 miliny ton) - tej linii nie używamy
years = round(tons / 782_000_000, 2) # tu mam z zaokragleniem do dwóch miejsc po przecinku - i to trzeba użyć
# years = round(tons / 782e6, 2) # można też tak tą dużą liczbe przedstawić - ta liczba e opisana w zjezdzie numer 1

print (years)

# Pociąg może transportować 2200t maksymalnie - czyli tu kalkulujemu ile potzeba pociągów, żeby tę ilość pszenicy przetrasportować
trains = round(tons / 2200, 1)
# lub tak
trains = int (tons / 2200) + 1
print(trains)



