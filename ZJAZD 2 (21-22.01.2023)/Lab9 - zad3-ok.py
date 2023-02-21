# LABORATORIUM 9 - ZAD 3

# # ZAD. 3
# Napisz program wyznaczający wartość n-tego bitu dla dowolnej liczby
# całkowitej. Bity liczymy od 0, od najmniej znaczącego bitu.

#tu mamy sytuacje, że podajemy liczbę całkowitą, która ma swoje rozłożenie bitowe, np. dla liczby 1, mamy 0001, czyli jeśli podam liczbę 1 + bit 0 to wtedy dostanę , że bit na pozycji 0 (tu mamy 1) dla liczby 1(tu mamy bit na pozycji 0) i teraz 1 z 1 na tej samej poycji się nakładają, wieć mamy 1, WYNOSI 1. Zaś gdybym podał na innej pozycji, gdzie dla jedynki było nie jeden, a zeero, to wtedy byłoby 0, bo 1 i 0 daje zero.

number = int (input("Podaj liczbę: "))  #podanie liczby całkowitej, dla której jest wyznaczana wartość n-tego bitu, podanego poniżej
n = int(input("Podaj nr bitu: ")) # numery bitów

# 01001 - przykładowa liczba - i tu się posilkujemy maską
# 00001 - to jest moja  maska
# &      -->za pomocą AND(koniunkcji)=& wyłuskamy te bity
# 00001 - to jest wynik, który

mask = 1 << n #potrzebujemy maskę wiec dodajemy taką zmienną
result = number & mask

bit = int(bool(result)) # wyłuskanie bity, czy to jest jeden, czy zero
print("Bit na pozycji", n, "dla liczby", number, "wynosi", bit)


# SPRAWDZENIE (to jest opcjonalne)
print("{:08b}",format(number))
print("{:08b}",format(mask))
print("-" * 8)
print("{:08b}",format(result))
