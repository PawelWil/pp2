# LAB. 12, ZAD.1
#
# Napisz funkcję, której zadaniem będzie wyświetlić na ekranie dowolny znak, dowolną
# ilość razy, w poziomie lub w pionie

# Rozwiązanie Pana Marcina:

def print_char(character="*", rep=10, vert=False): # na pewno potrzebujemy funkcj - te zmienne obok, to śa nasze zmienne , wewnetrzne, nie systemowe - tylko dla funkcji. Nie można ich uzywa c na zewnątrrz, tylko sa w obrebie funkci 'char'
# pass # robimy zaslepke na sam początek
    for i in range (rep):
        if vert:
            print (character)
        else:
            print(character + " ", end = "")
    if not vert:
        print()
    print()

print_char()
print_char("+", 5, True)
print_char("^", 7, False)

















