# LAB 14 - ZAD 2
#
# Napisz funkcje zamieniającą 3 listy na 1 krotkę bez powtarzających się elementów.
# Przykład: [1, 2], [1, 1], [4, 4, 4] -> (1, 2, 4)

def merge_list_without_duplicates(source, target): # source = lista zrodlowa, Target=lista wynikowa)
    for e in source:
        if e not in target:
            target.append(e)


# probujemy mergować
def transform_data(list1, list2, list3): #pobierac bedzie 3 listy
    result = [] #pusta lista,
    merge_list_without_duplicates(list1, result)
    merge_list_without_duplicates(list2, result)
    merge_list_without_duplicates(list3, result)
    return tuple(result)



print(transform_data([1,2], [1,1], [4,4,4]))
print(transform_data([1,2,3], [1,2,3], [4,5,6]))
print(transform_data(["Ala","ma"], ["Ala","ma","kota"], ["mysz"]))

