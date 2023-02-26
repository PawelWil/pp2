# LAB 14 - ZAD 3
#
# Napisz program zliczający punkty w grach (karcianych, planszowych itp.), realizujący:
# • definiowanie liczby oraz imion graczy,
# • definiowanie liczby punktów potrzebnych do wygranej,
# • pobieranie informacji o zdobytych punktach w każdej turze gry,
# • wyświetlanie informacji o zwycięzcy oraz zdobytych punktach poszczególnych graczy.


# 1 krok: definiowanie liczby oraz imion graczy,------
def define_player(player_no):  # pojedynczy gracz
    player_points = []  # lista
    player_name = input("Podaj imię" + str(player_no) + "gracza:")
    return {player_name: player_points}


def define_players():
    players = {}
    players_total = int(input("Podaj liczbe graczy (1-8): "))  # bedzie tam info ilu graczy tam bedzie
    for i in range(players_total):
        players.update(define_player(i + 1))
    return players


# players = define_players()
# print(players)


# 2 krok: definiowanie liczby punktów potrzebnych do wygranej,-----------

def define_win_points():
    return int(input("Zdefiniuj liczbę punktów wygranej: "))


# 3 krok: pobieranie informacji o zdobytych punktach w każdej turze gry,---------

def is_winner(players, win_points):
    for player_name, player_points in players.items():
        sum = 0
        for p in player_points:
            sum += p
        if sum >= win_points:
            return True
    return False


def count_points(players, win_points):
    counter = 1
    while True:
        print("\nTura: ", counter)
        for player_name in players.keys():
            player_points = int(input("Podaj punkty dla gracza" + player_name + ":"))
            players[player_name].append(player_points)
            if is_winner(players, win_points):
                return player_name
        counter += 1


# 4 krok: wyświetlanie informacji o zwycięzcy oraz zdobytych punktach poszczególnych graczy.------------

def show_results(players, winner):
    print("\nWygrał gracz i imieniu: ", winner + ", brawo!\n")
    print("Szczegółowa tabela wyników")
    for player, points in players.items():
        print(player, "->", points)


players = define_players()
win_points = define_win_points()
winner = count_points(players, win_points)
show_results(players, winner)
