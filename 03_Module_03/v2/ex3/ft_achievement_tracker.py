import random


def gen_player_achievements() -> set[str]:
    all_achievements = [
        "First Steps",
        "Speed Runner",
        "Master Explorer",
        "Boss Slayer",
        "Treasure Hunter",
        "Crafting Genius",
        "World Savior",
        "Untouchable",
        "Collector Supreme",
        "Sharp Mind",
        "Survivor",
        "Strategist",
        "Unstoppable",
        "Hidden Path Finder"
    ]

    number = random.randint(5, len(all_achievements))
    return set(random.sample(all_achievements, number))


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    Alice = gen_player_achievements()
    Bob = gen_player_achievements()
    Charlie = gen_player_achievements()
    Dylan = gen_player_achievements()

    print(f"Player Alice: {Alice}")
    print(f"Player Bob: {Bob}")
    print(f"Player Charlie: {Charlie}")
    print(f"Player Dylan: {Dylan}")

    all_achievements = Alice | Bob | Charlie | Dylan
    print(f"\nAll distinct achievements: {all_achievements}")

    common_achievements = Alice & Bob & Charlie & Dylan
    print(f"\nCommon achievements: {common_achievements}\n")

    unique_Alice = Alice - (Bob | Charlie | Dylan)
    unique_Bob = Bob - (Alice | Charlie | Dylan)
    unique_Charlie = Charlie - (Bob | Alice | Dylan)
    unique_Dylan = Dylan - (Bob | Charlie | Alice)
    print(f"Only Alice has: {unique_Alice}")
    print(f"Only Bob has: {unique_Bob}")
    print(f"Only Charlie has: {unique_Charlie}")
    print(f"Only Dylan has: {unique_Dylan}")

    missing_Alice = all_achievements - Alice
    missing_Bob = all_achievements - Bob
    missing_Charlie = all_achievements - Charlie
    missing_Dylan = all_achievements - Dylan
    print(f"Alice is missing: {missing_Alice}")
    print(f"Bob is missing: {missing_Bob}")
    print(f"Charlie is missing: {missing_Charlie}")
    print(f"Dylan is missing: {missing_Dylan}")


if __name__ == "__main__":
    main()
