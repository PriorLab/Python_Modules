import random


def initial_list() -> list[str]:
    players = [
        'Alice', 'bob', 'Charlie', 'dylan',
        'Emma', 'Gregory', 'john', 'kevin', 'Liam'
        ]
    return players


def cap_list(players: list[str]) -> list[str]:
    cap_players = [name.capitalize() for name in players]
    return cap_players


def cap_list_only(players: list[str]) -> list[str]:
    only_cap = [name for name in players if name[0].isupper()]
    return only_cap


def score_dict(cap_players: list[str]) -> dict[str, int]:
    scores = {name: random.randint(1, 1000) for name in cap_players}
    return scores


def highest_scores(players_dict: dict[str, int]) -> dict[str, int]:
    average = sum(players_dict.values()) / len(players_dict)
    high_scores = {
        name: score
        for name, score in players_dict.items()
        if score > average
    }
    return high_scores


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
    print(f"Score dict: {cap_team_scores}")
    print(f"Score average is {average:.2f}")
    print(f"High scores: {podium_cap_team}")


if __name__ == "__main__":
    main()
