# Laboratorium 22 - zad. 2

# Napisz klasę zliczającą wszystkie powstałe swoje instancje.

class C:
    counter = 0

    def __init__(self):
        C.counter += 1

    def getcounter(self):
        return C.counter

for i in range (100):
    C()

print("Utworzono obiektów: ", C.counter)

#--------- albo w inny sposób

class C:
    counter = 0

    def __init__(self):
        C.counter += 1

    def getcounter(self):
        return C.counter

for i in range (100):
    obj = C()

print("Utworzono obiektów: ", obj.getcounter())