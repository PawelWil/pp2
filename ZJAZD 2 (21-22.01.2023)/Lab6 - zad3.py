#ZAD 3
# Za pomocą jednej instrukcji wyświetl na ekranie
# następującą figurę

# Wersja Pana Marcina
 # Figura za pomocą jednej instrukcji

# print ("+" + "-+" * 9) # na razie linia górna - zaczymay od +, potem 9 x mnożymy znak -+
print ("+" + "-+" * 9, "| " * 10, "+" + "+-" *9, sep="\n") #teraz dajemy separator z nową linią, wazna jest też spacja po "|", bo on nam to rozszerza
