# LAB 18 - zad 2 --> obejrzec filmik - bardzo fajne informacje

#  Zaimplementuj funkcję, która przyjmuje jako argument ciąg znaków i zwraca
# liczbę wystąpień każdego znaku w ciągu.
# Na przykład dla ciągu "abracadabra" funkcja powinna zwrócić słownik { 'a': 5, 'b':
# 2, 'r': 2, 'c': 1, 'd': 1 }.


def count_letters(string):
    stats = {}
    for char in string:
        if char in stats.keys():
            stats[char] += 1
        else:
            stats[char] = 1
    return stats


print(count_letters("abracadabra")) # 'a': 5 - tzn, ze jest 5 liter a, itd.
print(count_letters("abc")) # 1 litera a, 1 litera b, 1 litera c
print(count_letters("Ala ma kota a kot ma Alę."))