# 3. Napisz program pobierający od użytkownika liczbę całkowitą i zwracający
# liczbę jedynek w ciągu bitów reprezentujących tę liczbę.

while True:

    number = int(input("Proszę podać dowolną liczbę całkowitą: "))
    bits = 0
    bitLength = 1
    n = 0

    while True:
        if 2 ** bitLength < number:
            n += 1
            bitLength += 1
        else:
            break

    for i in range(n + 1):
        mask = 1 << i
        val = (number & mask) >> i
        if val == 1:
            bits += 1

    print("Uzyskana liczba jedynek w ciągu bitów dla podanej liczby", number, "wynosi:", bits)
    break
