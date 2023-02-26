# Lab 13 - Zad.1
# Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskazanej listy.

#Rozwiązanie Pana Marcina:

# 1 sposób rozwiązania:
# def pow (numbers, exponent): # funkcja pow=power_numbers=podnoszenie do potęgi, będzie przyjmowała dwa argumenty. Numbers=potęga
#     for i in range (len(numbers)):
#         numbers[i] = numbers[i] ** exponent
#     return numbers
#
# print(pow([1,2,3], 2))
#
# print(pow([2, 7, 33], 5))


# # 2 sposób rozwiązania:
#
# def pow (numbers, exponent): # funkcja pow=power_numbers=podnoszenie do potęgi, będzie przyjmowała dwa argumenty. Numbers=potęga
#     for i in range (len(numbers)):
#         numbers[i] = numbers[i] ** exponent
#     return numbers
#
# def pow2(numbers, exponent):
#     result = []
#     for n in numbers:
#         result.append(n ** exponent)
#     return result
#
# print(pow([1,2,3], 2))
# print(pow2([1,2,3], 2))
#
# print(pow([2, 7, 33], 5))
# print(pow2([2, 7, 33], 5))

# 3 sposób rozwiązania:

def pow (numbers, exponent): # funkcja pow=power_numbers=podnoszenie do potęgi, będzie przyjmowała dwa argumenty. Numbers=potęga
    for i in range (len(numbers)):
        numbers[i] = numbers[i] ** exponent
    return numbers

def pow2(numbers, exponent):
    result = []
    for n in numbers:
        result.append(n ** exponent)
    return result

def pow3(numbers, exponent):
    return [x ** exponent for x in numbers]



print(pow([1,2,3], 2))
print(pow2([1,2,3], 2))
print(pow3([1,2,3], 2))

print(pow([2, 7, 33], 5))
print(pow2([2, 7, 33], 5))
print(pow3([2, 7, 33], 5))




#MOJA PRÓBA :)
# def potega_numbers(numbers): # to co jest w nawiasie to są parametry tej fukcji, tutja to zmienna 'numbers'
#     potega = 4
#     for element in numbers: #teraz korzystamy z petli, ktora to zmienna dostanie kolejne lelemty, któr bedzizemy iteroiwac, dla nas to lista, czyli dopisz/dodaj ten elemnt
#         result = (element ** potega)
#         # element = str(numbers) + str(1)
#     return result
#
# numbers = [1, 3] # to jest zmienna globalna 'numbers'
# result = potega_numbers(numbers)
# print (result)