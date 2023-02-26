# KROTKI ------------------------------------------------

# numbers = ( 1, 2, 3) # to jest krotka, nieedytowalna, w nawiasach okrągłych
# numbers = 1, 2, 3 # mozna tez krotke zapisac bez nawiasów
# numbers = () # to jest pusta krotka

# numbers = (1, ) # pokazuje konkretną krotkę
# print (numbers) # pokazuje wszystkie krotki

# iteracja krotki----
# numbers = ( 1, 2, 3)
#
# for i in numbers:
#     print (i)


# #-------
# print(numbers[1:2])

# generator krotki, za pomocą generatora wyrażenia--------
# numbers = tuple(x for x in range (10))
# print(numbers)

# krotki są niemutowalne = niezmienne-----
# numbers = tuple(x for x in range (10))
#
# print(numbers)
#
# numbers[0] = 9999 # jak widać podmiana nie działa, czyli krotki po prostu są niezmienialne=niemutowalne

# nie mozemy tez usunąc danego elelmntu krotki-------

# numbers = tuple(x for x in range (10))
#
# print(numbers)
#
# del numbers[0] # nie da się usunąć elemntów krotki
# del numbers # ale da się usunąć całą krotkę

# jakie opercaje":
#1. ile ma elemntów
# z filmiku ścignąć
#
# #2. Mnozenie:
# numbers = tuple(x for x in range (10))
#
# print(numbers * 2)

# konwersja listy na krotke---------
# numbers = [1,2,3]
# numbers = tuple (numbers) # konwersja listy na krotke
#
# print(numbers)

 # lub
#
# numbers = "Ala"
# numbers = tuple (numbers) # konwersja listy na krotke
#
# print(numbers)


# SŁOWNIKI = zestaw, klucz, wartosc ------------------------------------------------
#
# phones = {"Tomek": 21312321, "Ada": 12341441, "Karol": 99999999} # numery telefonów ludzi
# print(phones)

# klucz musi byc niepowtarzalny, bo jednoznacznie identikuej wpis w naszym słowniku, np:---

# phones = {"Tomek": 21312321, "Ada": 12341441, "Karol": 99999999, "Tomek": 4444444444444} # Tomek z samego poczatku, jest podmienioony z ostatnia wartością
# print(phones)

# zapis takiego słownika---
# animals_dict= {
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
# }
# print (animals_dict)
# print (animals_dict["kot"])
# print (animals_dict.get)...???
# print (animals_dict.get("krowa", "brak takiego slowa"))

#weryfikacja, czy istnieje taki klucz w słowniku-----------*słwonik animals_dict, przy testach musi by ć aktywny
# words = ["kot", "lew", "chomik"] # to jest lista, bo kwadratowe nawiasy
# for word in words:
#     if word in animals_dict:
#         print(word, "->", animals_dict[word])
#     else:
#         print("nie znaleziono slowa:", word, "w słowniku.")

# mozemy tez iterowac po kluczach-------*słwonik animals_dict, przy testach musi by ć aktywny
# for key in animals_dict.keys():
#     print(key, "->", animals_dict[key])

# same values - wyciągnie tylko warytosci
# for val in animals_dict.values():
#     print(val)

# same items -
# for item in animals_dict.items():
#     print(item)

# moze tez byc polsich english
# for pl, en in animals_dict.items():
#     print(pl, "->", en)
# print()

# modyfikacja slownika--------
#

# # aktualizacja slownika
# animals_dict= {
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
# }
# animals_dict["swinka"] = "pig"
# animals_dict.update({"kurczak": "chicken"})
#
# print(animals_dict)

# zmiana--

# animals_dict= {
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
# }
# animals_dict["swinka"] = "pig"
# animals_dict.update({"kurczak": "chicken"})
# animals_dict.update({"swinka": "pigy"})
#
# print(animals_dict)

# kopia---
# animals_dict= {
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
# }
# animals_dict["swinka"] = "pig"
# animals_dict.update({"kurczak": "chicken"})
# animals_dict.update({"swinka": "pigy"})
#
# dict2 = animals_dict.copy()
# print(dict2)
#
# print(animals_dict)

# usuwanie---
# animals_dict= {
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
# }
# animals_dict["swinka"] = "pig"
# animals_dict.update({"kurczak": "chicken"})
# animals_dict.update({"swinka": "pigy"})
#
# dict2 = animals_dict.copy()
#
# del dict2["swinka"]
#
# print(dict2)

# usuwanie ostatniejo ellentu
animals_dict= {
    "kot": "cat",
    "pies": "dog",
    "chomik": "hamster"
}
animals_dict["swinka"] = "pig"
animals_dict.update({"kurczak": "chicken"})
animals_dict.update({"swinka": "pigy"})

dict2 = animals_dict.copy()

# del dict2.popitem() #???????

print(dict2)

# ????????są jeszcz inne rzeczy - przesluchać filmik!!!!