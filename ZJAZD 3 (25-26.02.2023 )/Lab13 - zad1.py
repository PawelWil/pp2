# Lab 13 - Zad.1
# Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskazanej listy.


def pow (numbers, exponent): # funkcja pow=power_numbers=podnoszenie do potęgi, będzie przyjmowała dwa argumenty. Numbers=potęga
    for i in range (len(numbers)):
        numbers[i] = numbers[i] ** exponent
    return numbers

def pow2(numbers, exponent):
    result = []
    for n in numbers:
        result.append(n ** exponent)
    return result

print(pow([1,2,3], 2))


print(pow([2, 7, 33], 5))


