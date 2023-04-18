# ------------ Tworzymy moduł do obslugi Totolotka: losujemy 6 liczb z 49

from random import sample


def draw_numbers():  # definujemy funkcję, za pomocą której będziemy losować 6 liczb z 49
    numbers = [i for i in range(1, 50)]  # dajemy pętlę for, które nam będzie iterować od 1 do 49
    lucky_numbers = sample(numbers, 6)  # zmienna pod którą zapisujemy nasze wylosowane liczby
    lucky_numbers.sort()  # sortujemy liczby od najniższej do najwyższej
    return lucky_numbers  # dopiero takie posortowane liczby sobie zwrócimy


def get_user_numbers():  # pobieramy od uzytkownika jego zestawu liczb (mechanizm skreslanie liczb przez użytkownika)
    n = 6  # za pomocą zmiennej n, podajemy ze bedziemy pobierac 6 liczb
    counter = 1  # zli
    user_numbers = []  # bedziemy te liczby zapisywać do tej listy
    while counter < n + 1:  # teraz z racji, że musimy pobrac pare liczb, musimy to jakoś zliczac, co robimy za pomocą pętli while -
        # będę sprawdzał licznik counter (zdefiniowany powyzej) - i ta petla bedzie bedzie pobierać liczby dopóki counter mniejszy od n+1
        try:
            number = int(input("Podaj " + str(
                counter) + " liczbę(1-49): "))  # tu wprowadzamy te liczby wybrane przez użytkownika na razie.
            # Dopiero poniżej zaczynamy się zabezpieczać, żeby to były liczby w zakresie od 1 do 49
            if number in user_numbers:  # zabezpieczenie na wypadek podania tej samej liczby
                print("Powtórzona liczba!")
                continue  # jak jest zla/powtórzona liczba to przerywamy pętlę za pomocą instrukcji 'continue', czyli wracamy do linii 20, żeby dalej podawał
            if number < 1 or number > 49:  # tu warunkuemy zakres przedziału, czyli gdy jest inna liczba od tych z przedziału od 1 do 49
                print("Należy podać liczbę z przedziału 1-49!")
                continue  # jak jest zla liczba to przerywamy pętlę za pomocą instrukcji 'continue', czyli wracamy do linii 20, żeby dalej podawał
        except:
            print(
                "To nie jest liczba")  # jezeli nastąpi jakiś wyjątek, to znów pętla wraca z powrotem (dział wyjątów: try + except)
            continue

        user_numbers.append(
            number)  # natomiast jeśli wszystko jednak ok, czyli została dodana prawidłowa liczba przez użytkownika,
        # to zmienna 'user_numbers', ktora przechowuje te liczby za pomocą instrukcji 'append' jest o tą liczbę rozbudowana
        counter += 1  # czyli zwiększamy nasz licznik 'counter'o 1 i tak, aż uzyskamy 6 liczb
    user_numbers.sort()  # sortujemy te numery po dodaniu kolejnych
    return user_numbers  # zwracamy te liczby wybrane przez użytkownika


def check_numbers(user_numbers,
                  lucky_numbers):  # sprawdz liczby, żeby nie sprawdzać tego ręcznie, a konkretnie komputer za pomocą
    # funckji 'check_numbers', ale żeby to zrobił, musimy mu podać jakie liczby zostały podane przez użytkownika('user_numbers)
    # oraz jakie liczby zostały wylosowane przez komputer (lucky_numbers)

    counter = 0  # zmienna pomocnicza typu 'counter', który będzie nam liczył ilość trafionych liczb, czyli na początku mamy 0
    for number in user_numbers:  # teraz pętlą 'for' będziemy sobie wyciągać liczby od uzytkownika (czyli zmienna user_numbers)
        if number in lucky_numbers:  # teraz za pomocą if sprawdzamy czy ta liczba podana przez uzytkowniak jest w
            #         zbiorze liczb szczęsliwych. Jak to sprawdzimy z pierwszą liczbą, idziemy dalej, poporzez użycie 'counter += 1'

            counter += 1
    return counter  # teraz zwracamy te liczby


if __name__ == "__main__":
    user_numbers = get_user_numbers()
    lucky_numbers = draw_numbers()
    result = check_numbers(user_numbers, lucky_numbers)  # teraz pokazujemy nasz finalny rezultat
    print(user_numbers)
    print(lucky_numbers)
    print(result)  # tu już drukujemy finalny rezultat
