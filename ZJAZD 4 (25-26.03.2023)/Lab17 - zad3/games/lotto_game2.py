from games.MODUŁY_16 import get_user_numbers, check_numbers, draw_numbers

from MODUŁY_16 import get_user_numbers, check_numbers, draw_numbers

print("Witaj w grze lotto!")
user_numbers = get_user_numbers()
print("Podane liczby to: ", user_numbers)

print("Nacisnij Enter, aby dokonac losowania liczb!\n")
input()
lucky_numbers = draw_numbers()
print("Wylosowane liczby to: ", lucky_numbers)

result = check_numbers(user_numbers, lucky_numbers)
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

