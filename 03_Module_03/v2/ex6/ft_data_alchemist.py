import random


def initial_list() -> list[str]:
    players = [
        'Alice', 'bob', 'Charlie', 'dylan',
        'Emma', 'Gregory', 'john', 'kevin', 'Liam'
        ]
    return players


def cap_list(players: list[str]) -> list[str]:
    cap_players: list[str] = []
    for player in players:
        cap_players.append(player.capitalize())
    return cap_players


def cap_list_only(players: list[str]) -> list[str]:
    only_cap_players: list[str] = []
    for player in players:
        if player[0].isupper():
            only_cap_players.append(player)
    return only_cap_players


def score_dict(cap_players: list[str]) -> dict[str, int]:
    players_dict: dict[str, int] = {}
    for player in cap_players:
        players_dict[player] = random.randint(1, 1000)
    return players_dict


def highest_scores(players_dict: dict[str, int]) -> dict[str, int]:
    highest_scores_dict: dict[str, int] = {}
    avrg = sum(players_dict.values()) / len(players_dict)
    for player in players_dict:
        if players_dict[player] > avrg:
            highest_scores_dict[player] = players_dict[player]
    return highest_scores_dict


def main() -> None:
    team = initial_list()
    cap_team = cap_list(team)
    cap_only_team = cap_list_only(team)
    cap_team_scores = score_dict(cap_team)
    podium_cap_team = highest_scores(cap_team_scores)
    average = sum(cap_team_scores.values()) / len(cap_team_scores)

    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {team}")
    print(f"New list with all names capitalized: {cap_team}")
    print(f"New list of capitalized names only: {cap_only_team}")
    print(f"score dict: {cap_team_scores}")
    print(f"Score average is {average:.2f}")
    print(f"High scores: {podium_cap_team}")


if __name__ == "__main__":
    main()
