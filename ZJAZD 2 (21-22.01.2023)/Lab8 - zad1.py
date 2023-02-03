# ZAD.1
# Wyświetl liczby od 1 do 100 z pominięciem liczb podzielnych przez 3

print("Liczby od 1 do 100, niepodzielne przez 3, to: " )
for i in range (1, 101):
    if i  % 3 != 0:
        print(i)


