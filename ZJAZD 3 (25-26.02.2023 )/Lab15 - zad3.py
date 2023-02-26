# LAB 15 - ZAD 3
#
# Zabezpiecz program zliczający punkty w grach (moduł 14, lab 3) przed
# wprowadzaniem błędnych danych przez użytkownika.



# Poniszy program jezt z LAB 14, zad3

def fetch_and_validate_int(standard_msg, error_msg="To nie jest liczba"):
    while True:
        try:
            return int(input(standard_msg))
        except:
            print(error_msg)


def define_player(player_no):  # pojedynczy gracz
    player_points = []  # lista
    player_name = input("Podaj imię" + str(player_no) + "gracza:")
    return {player_name: player_points}


def define_players():
    players = {}
    players_total = fetch_and_validate_int("Podaj liczbe graczy (1-8): ")  # bedzie tam info ilu graczy tam bedzie
    for i in range(players_total):
        players.update(define_player(i + 1))
    return players




def define_win_points():
    return fetch_and_validate_int("Zdefiniuj liczbę punktów wygranej: ")



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
            player_points = fetch_and_validate_int("Podaj punkty dla gracza" + player_name + ":")
            players[player_name].append(player_points)
            if is_winner(players, win_points):
                return player_name
        counter += 1




def show_results(players, winner):
    print("\nWygrał gracz i imieniu: ", winner + ", brawo!\n")
    print("Szczegółowa tabela wyników")
    for player, points in players.items():
        print(player, "->", points)


players = define_players()
win_points = define_win_points()
winner = count_points(players, win_points)
show_results(players, winner)
