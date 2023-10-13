# https://judge.softuni.org/Contests/Practice/Index/1538#11
# Condition:https://judge.softuni.org/Contests/Practice/DownloadResource/5355

wins = 0
lost = 0
number_tournaments = 0

while True:
    tournament_name = input()
    if tournament_name == "End of tournaments":
        break

    matches_number = int(input())
    number_tournaments += matches_number
    for game in range(1, matches_number + 1):
        desy_points = int(input())
        opponents_points = int(input())

        if desy_points > opponents_points:
            difference = desy_points - opponents_points
            print(f"Game {game} of tournament {tournament_name}: win with {difference} points.")
            wins += 1
        elif desy_points < opponents_points:
            difference = opponents_points - desy_points
            print(f"Game {game} of tournament {tournament_name}: lost with {difference} points.")
            lost += 1

percent_wins = (wins / number_tournaments) * 100
percent_lost = (lost / number_tournaments) * 100

print(f"{percent_wins:.2f}% matches win\n"
      f"{percent_lost:.2f}% matches lost")

