print("Początkowa wartość inwestycji wynosi:", 14_000, "zł")
a = 14000 * 1.4  # ile wynosi inwestycja po pierwszym roku
b = (14000 * 1.4) - 1500  # ile wynosi inwestycja po drugim roku
print((a - 1500) * 1.12)  # ile wynosi inwestycja po trzecim roku

print(round((((a - 1500) * 1.12)), 2)) # sposób zaokrąglenia - i tu mamy zaokrąglenie do 2 miejsc

# Inwestycja po wszystkich 3 latach jest warta  20272 zł
