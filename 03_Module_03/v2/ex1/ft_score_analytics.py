#!/usr/bin/python3
import sys


def players_analysis(players: list[str]) -> None:
    print("=== Player Score Analytics ===")
    if len(players) == 1:
        print(
            "No scores provided."
            " Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return
    scores: list[int] = []
    for player in players[1:]:
        try:
            score = int(player)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{player}'")
    if len(scores) == 0:
        print(
            "No scores provided."
            " Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


def main() -> None:
    players_analysis(sys.argv)


if __name__ == "__main__":
    main()
