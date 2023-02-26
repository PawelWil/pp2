# # LAB 14 - ZAD.1
#
#  Napisz wyszukiwarkę numerów telefonów:
# • zdefiniuj słownik par imię -> numer telefonu,
# • zapytaj użytkownika o imię,
# • wyświetl użytkownikowi numer telefonu lub informacje o jego braku.


phones = {"Tomek": 21312321, "Ada": 12341441, "Karol": 99999999} # numery telefonów ludzi
name = input ("Podaj imię:")
names = [name]

for name in phones():
    if name in phones:
        print(name, "->", phones[name])
    else:
        print("nie znaleziono slowa:", name, "w słowniku.")





# animals_dict= {
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
# }
# words = ["kot", "lew", "chomik"] # to jest lista, bo kwadratowe nawiasy
# for word in words:
#     if word in animals_dict:
#         print(word, "->", animals_dict[word])
#     else:
#         print("nie znaleziono slowa:", word, "w słowniku.")