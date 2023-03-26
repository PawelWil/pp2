# LAB 18 - zad 2 --> obejrzec filmik - bardzo fajne informacje

#  Zaimplementuj funkcję, która przyjmuje jako argument ciąg znaków i zwraca
# liczbę wystąpień każdego znaku w ciągu.
# Na przykład dla ciągu "abracadabra" funkcja powinna zwrócić słownik { 'a': 5, 'b':
# 2, 'r': 2, 'c': 1, 'd': 1 }.

# lista l = [1, 2, 3] - list -- lista charaktyryzuje się, że do elementów odwujemy sie za pomocą indeksów, jest mutowalna
# krotka t = (1,2,3) (ang. tuple) - tuple -- także charaktyryzuje się, że do elementów odwujemy sie za pomocą indeksów, ale nie jest mutowalna
# słownik d = {"a":1, "b":2} - dictionary -- słownik nie jest sekwencją, czyli nie możemy po nim przejść pętlą. Elementy są uporządkowane.
# ciąg znaków s = "asas" - string -- trochę podobny do krotki, mozna po nim iterować, ale jest niemutowalny

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