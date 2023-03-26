# Napisz funkcję zliczającą ilość wystąpień poszczególnych elementów listy w formie słownika.
#
# Przykład:
#
# print(frequency_occurrences(["Ala", "Tomek", "Ala"]))
#
# {'Ala': 2, 'Tomek': 1}

# DOBRE ROZWIĄZANIE PANA MARCINA:

# def frequency_occurrences (source_list):
#     target_dict = {}
#     for e in  source_list:
#         if e in target_dict:
#             target_dict[e] += 1
#         else:
#             target_dict[e] = 1
#     return  target_dict
#
# print(frequency_occurrences(["Ala", "Tomek", "Ala"]))
# print(frequency_occurrences([1,1,1]))
# print(frequency_occurrences([1,23,34243,35234,522,222,222]))

#lub ponizej szybsza metoda, za pomocą funkcji 'count'

def frequency_occurrences (source_list):
    target_dict = {}
    for e in  source_list:
        target_dict[e] = source_list.count(e)
    return  target_dict
print(frequency_occurrences(["Ala", "Tomek", "Ala"]))
print(frequency_occurrences([1,1,1]))
print(frequency_occurrences([1,23,34243,35234,522,222,222]))


