# # ZAD. 3
# Napisz program wyznaczający wartość n-tego bitu dla dowolnej liczby
# całkowitej. Bity liczymy od 0, od najmniej znaczącego bitu.


# Rozwiązanie Pana Marcina:

# #I SPOSÓB

number = int (input("Podaj liczbę: "))  #liczba bitów
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