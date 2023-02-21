# LABORATORIUM 9 - ZAD 2

# # ZAD. 2
# Udowodnij, że w zbiorze liczb z zakresu 1-100, jest 11 liczb, które są
# parzyste i jednocześnie większe od 90, a gdy są nieparzyste, to
# przynajmniej dzielą się przez 9.


# Rozwiązanie Pana Marcina:

# zawsze powinnismy to podzielić na mniejsze rowziązania, a potem dopiero to łączyć - bo czasami za duzo na raz tego jest!

counter = 0
for i in range (1, 101):# potrzebujemy liczby od 1 do 100, wiec robimy pętle for
    if i % 2 == 0 and i > 90 or ( i % 2 != 0 and i % 9 == 0): # to jest pierwszy warunek=sprawdzamy parzystsc i wieksze od 90 (i % 2 == 0 and i > 90), a teraz drugi warunek:( i % 2 != 0 and i % 9 == 0)
        counter += 1  # teraz checmy te zmienne zliczyć, wiec dajemy zmienną counter


print("Tak to prawda, w zbiorze liczb z zakresu 1-100, jest " + str(counter) + " liczb, które są parzyste i jednocześnie większe od 90, a gdy są nieparzyste, to przynajmniej dzielą się przez 9.  "  + ".")

