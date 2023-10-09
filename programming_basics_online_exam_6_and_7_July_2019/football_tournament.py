wins = 0
draws = 0
lost = 0
points = 0

football_team = input()
games_number = int(input())
non_played_games = False


if games_number == 0:
    print(f"{football_team} hasn't played any games during this season.")
    non_played_games = True


else:
    for game in range(games_number):
        result = input()
        if result == "W":
            wins += 1
            points += 3
        elif result == "D":
            draws += 1
            points += 1
        elif result == "L":
            lost += 1

if not non_played_games:
    win_rate = (wins / games_number) * 100
    print(f"{football_team} has won {points} points during this season.")
    print("Total stats:\n"
        f"## W: {wins}\n"
        f"## D: {draws}\n"
        f"## L: {lost}")
    print(f"Win rate: {win_rate:.2f}%")
