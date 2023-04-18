from lotto import get_user_numbers, check_numbers, draw_numbers # tu importujemy moduł lotto, który został przygotowany wcześniej
# i na jego bazie już zaczynamy robić specyficzną obsługę gry, w której ten moduł/silnik zastosowano.
# Po prostu ten moduł/silnik do obsługi lotto ubieramy wg skryptu poniżej już zgodnie z naszymi preferencjami.
# Dodatkowo ten kod poniżej jest przejrzysty, nie rozwija core'a/silnika dla lotto, ale skupia sie na tym co ma być przedsyawione
# w tej konkretnej grze/aplikacji.

print("Witaj w grze lotto!")
user_numbers = get_user_numbers() # zapisuje od uzytkownika podane liczby do zmiennej get_user_numbers
print("Podane liczby to: ", user_numbers) # i teraz drukuję te liczby

print("Nacisnij Enter, aby dokonac losowania liczb!\n") # teraz damy komunikat, nacisnij aby dokonac losowania
input() # Teraz daje input, żeby moc wprowadzić 'enter'
lucky_numbers = draw_numbers() # teraz te szczesliwe liczby zostaną zapisabe do funkcji draw_numbers
print("Wylosowane liczby to: ", lucky_numbers) # i to komunikat o wylosowanych liczbach

result = check_numbers(user_numbers, lucky_numbers) # teraz wyswietlamy resultaty - podajemy wybrane numbery i szczesliwe numery,
# gdzie funkcja result pokaże nam ile padło liczb - a teraz musimy z tymi wynikami losowań coś zrobić, czyli je skomentować, w zależności
# od wygranej - tak jak dokładnie poniżej:
if result == 6:
    print("Gratulacje!!!", "Jesteś milionerem")
elif result == 5:
    print("Brawo!", "Trafiono piątkę", "Zgarniesz sporą sumkę!")
elif result == 4:
    print("Hurra, trafiono czwórkę", "to całkiem niezły wynik")
elif result == 3:
    print("Trafiono trójkę", "Przysługuje Ci minimalna wygrana")
elif result == 2 or result == 1:
    print("Trafiono ", result, "liczbę. Było bardzo blisko!" )
else:
    print("To nie jest Twój dzień!")
