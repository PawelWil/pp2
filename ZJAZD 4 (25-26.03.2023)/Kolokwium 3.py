# Napisz funkcję zliczającą ilość wystąpień poszczególnych elementów listy w formie słownika.
#
# Przykład:
#
# print(frequency_occurrences(["Ala", "Tomek", "Ala"]))
#
# {'Ala': 2, 'Tomek': 1}


#Definujemy funkcję zliczającą ilość wystąpień poszczególnych elementów listy w formie słownika.
def sum_numbers(numbers):
    sum = 0  # tu dajemy zmienną lokalną 'sum'
    for element in numbers:
        sum += element
    return sum

print (sum_numbers({1,1,3}))

