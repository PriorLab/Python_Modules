import random
def players_raw() -> list[str]:
    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    return players

def players_cap_only(players: list[str]) -> list[str]:
    only_cap_players = []
    for player in players:
        if player[0].isupper():
            only_cap_players.append(player)
    return only_cap_players

def players_cap(players: list[str]) -> list[str]:
    cap_players = []
    for player in players:
        capitalization = player.capitalize()
        cap_players.append(capitalization)
    return cap_players

def players_dict(players_cap: list[str]) -> dict[str, int]:
    return {player: random.randint(1,1000) for player in players_cap}

def players_higher_average(players_dict: dict[str, int]):
     average = sum(players_dict.values())/len(players_dict)
     return {player: score for player, score in players_dict.items() if score > average}

def main() -> None:
    init_team = players_raw()
    only_cap_team = players_cap_only(init_team)
    cap_team = players_cap(init_team)
    dict_team = players_dict(cap_team)
    highscores_team = players_higher_average(dict_team)
    average = sum(dict_team.values()) / len(dict_team)

    print('=== Game Data Alchemist ===\n')
    print(f"Initial list of players: {init_team}")
    print(f"New list with all names capitalized: {cap_team}")
    print(f"New list of capitalized names only: {only_cap_team}\n")
    print(f"Score dict: {dict_team}")
    print(f"Score average is {average:.2f}")
    print(f"High scores: {highscores_team}")

if __name__ == "__main__":
    main()