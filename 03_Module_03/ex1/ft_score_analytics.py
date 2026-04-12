import sys

def players_analysis(players: list[str]) -> None:
    print('=== Player Score Analytics ===')
    
    if len(players) == 1:
        print(f"No scores provided. Usage: {players[0]} <score1> <score2> ...")
        return
    
    scores = []
    
    for player in players[1:]:
        try:
            score = int(player)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: {player}")

    if len(scores) == 0:
        print(f"No scores provided. Usage: {players[0]} <score1> <score2> ...")
        return
    
    total_score = sum(scores)
    average_score = total_score / len(scores)
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")

def main() -> None:
        players_analysis(sys.argv)

if __name__ == "__main__":
    main()



#=== Player Score Analytics ===
#Scores processed: [1500, 2300, 1800, 2100, 1950]
#Total players: 5
#Total score: 9650
#Average score: 1930.0
#High score: 2300
#Low score: 1500
#Score range: 800
#$> python3 ft_score_analytics.py
#=== Player Score Analytics ===
#No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...
#$> python3 ft_score_analytics.py ab ac
#=== Player Score Analytics ===
#Invalid parameter: 'ab'
#Invalid parameter: 'ac'
#No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...