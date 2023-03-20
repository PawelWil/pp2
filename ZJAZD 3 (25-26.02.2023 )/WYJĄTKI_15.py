# WYJĄTKI________________
# 0. EXCEPTION - wyjątek występuję, gdy podczas wykonywania składniowo poprawnego kodu Pythona wystąpi błąd.
# W terminologii Pythona jest zgłaszany wyjątek. Ale kod sie wykona. --> tu chodzi o to, że kod jest napisany prawidłowo,
# ale np. użytkownik wprowadził nieprawidłowe dane wejściowe, żeby ten kod zadziałał-wtedy on się zakończy i powiadomi, że dane są złe
# lub np. jak drukujemy - wszystko poszło dobrze, ale nie drukuje bo nie ma papieru, itd..
# Przykładowe blędy Exceptions = Wyjątków:
# 1.TypeError - nie można wykonać operacji w ramach danego typu, np.dodać wartości do napisu
# 2.IndexError - przekroczenie zasięgu listy lub krotki
# 3.ValueError - nieobslugiwana wartość lub typ danych
# 4.ZeroDivisionError - błąd dzielenia przez zero

# 1. SYNTAX ERROR = błedy skladni, występuje w momencie gdy probujemy uruchomić składniowo nieprawidłowy kod Pythona.
# Taki kod nie jest wogóle wykonywany, nawet te linie, które są poprawne składniowo.
# - tego sie na da ominąc żeby python idle mógł wykonać kod - trzeba po prostu te błędy poprawic.
# a.
# print("adssad") # to jest ok
# print("saddsa" #a tu mamy SyntaxError, bo brak nawiasu. Podpowiedz, że nawias otwarty nie został nigdy zamknięty: '(' was never closed
# i tu jak nie poprawimy tego, to ten kod sie nie wykona


# ---- b.print (1/0) # skaldniowo poprawny, ale nie wolno dzielić przez 0, takze pycharm wyrzuca błed, i mozna tu zrobic wyjątek = except
# - Przykład ZeroDivisionError - wiadomo, że nie wolno dzielić przez zero
# print (1/0) # dostajemy komunikat: ZeroDivisionError: division by zero

# - Ale można dać komunikat np., że "coś poszło nie tak", stosując pętle 'try-except', żeby ten kod niewykonany prawidłowo,
# mógł się jakoś zakończyć, np. z komunikatem, a nie bezpośrednio info o błedzie, gdzie wtedy nie wygląda to profesjonalnie
# try: # wypisujemy sekcje try - to jest start tej pętli 'try-except'
#     print(1/0) # jeśli w tej linijce wystąpi wyjątek = błąd
# except: # to po sekcji try, dajemy sekcję except=wyjątek, który umozliwia zakonczenie tej pętli nie błedem, ale np. komunikatem,
# czyli w tym tylko przypadku, które traktujemy jako except, dajemy komunikat 'coś poszło nie tak'
#     print("Cos poszło nie tak") # program się zakończy informacją 'cos poszło nie tak', zamiast błedem ZeroDivisionError


# c. program fetch number- pobiera od uzytkownika 5 liczb calkowitch - to ponizsze działa dobrze!
# numbers = [] # pusta lista
# for i in range (5): # pobieramy od użytkownika w pętli od i w range 5 te liczby
#     n = int(input("Podaj liczbę całkowitą: ")) # tu poprosimy o tą liczbę calkowitą, pięc razy, bo wiadomo, że mamy pętle for
#     numbers.append(n) # tu wiadomo, że dodajemy naszą liczbę na koniec listy
# print(n) # i teraz jak wszystko pójdzie  dobrze, to te piec liczb można podać i program się zakonczy,
# ale jak coś pójdzie nie tak, np. podam literkę zamiast liczby, to po hamsku się ten kod zakonczy
# z informacją: ValueError: invalid literal for int() with base 10: 'e'

# --- Teraz robię program, który przewiduje wystąpienie pewnych błedów i za pomocą pętli 'try-except' dodajemy te wyjątki,
# co by się nimi zakonczył, a nie po hamsku ;-)
# a.jak dam enter, bez podania liczby wystąpi błąd, czyli trzeba uniknąc zeby program wywalal blad po nacisniencu enter bez liczby
# założeniem jest proszenie uzytkownika, az do momentu, kiedy użytkownik poda poprawne wartości.
# tu dajemy pętlę while

# numbers = []
# counter = 0

# while True:  # ma true zeby sie wogole uruchomila
#     if counter > 4:  # jesli counter większe od 4, to opuść tą pętle, czyli będzie pięć powtórzen = zapytań, bo 0,1,2,3,4 = 5 zapytan, a po przekroczeniu liczby 4,
# czyli piątego powtórzenia, pętla się zakonczy - ale ważne piątego poprawnego
# break  # przy pomocy instrukcji break tą pętlę można opuścic
# try:  # tu robimy sprawdzenie czy czasem ten fragment kodu nie wygenerował jakiegoś wyjątku i obsłuzymy ten błąd jesli go wygenerwoał
# tak jak poniżej:
# n = int(input("Podaj liczbę całkowitą: "))  # wyswietlimy podaj liczbe
# numbers.append(n)  # a jesli już wszystko poszło dobrze, to tą liczbę dopisujemy
# counter += 1  # po to żeby móc zliczać ilość prób
# except:
#     print("To nie jest liczba calkowita-sprobuj ponownie")  # tu damy jako except, to nie jest liczba całkowita

# print(numbers)


# d. ---INWERSJA -  skrypt który pobiera liczbę i wyswietla odwroność te jliczby

while True:  # wykorzystujemny pętlę while
    try:  # wiadomo, żeby dodać wyjątki dajemy klauzule 'try-except'
        number = int(input("Podaj liczbe cakowitą: "))  # pobiermay sobie tą liczbę
        print("Odwrotna liczba:", 1 / number)  # teraz robimy inwersje tej liczby, czyli odwracamy ją,
        # czyli jeden przez naszą liczbę, którą jest number

    # except:  # 1 sposób - ale to jest taki bardzo ogólne info, że coś poszło nie tak, ale dalej do konca nie wiemy co
    #     print("Cos poszło nie tak")
# -- 2 sposób poniżej jest bardziej precyzyjny w obsłudze wyjątków:
    except ValueError: # tu już robimy precyzyjniej, na wypadek wystąpienia liter + musimy podać dokładną nazwę tego błędu
        print("To nie jest liczba calkowita")
    except ZeroDivisionError: # tu już robimy precyzyjniej, na wypadek wystąpienia zera + musimy podać dokładnie tą nazwę tego błedu
        print("Bład dzielenia przez zero")


# ZeroDivisionError: -- zła liczba
# ValueError: -- litery lub sam enter lub myslniki i inne znaki, zamiast liczb calkowitych


# e.
