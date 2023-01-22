import random

numbers = []
for i in range(10): # tu mamy wylosowac 10 cyfr
    number = random.randint(1, 100) #tą zmienną number będę lososwał = RANDOM
    numbers.append(number)

print(numbers)