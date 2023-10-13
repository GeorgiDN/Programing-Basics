# https://judge.softuni.org/Contests/Practice/Index/1538#8
# Condition:https://judge.softuni.org/Contests/Practice/DownloadResource/5349

from math import floor
tournaments_number = int(input())
starting_points = int(input())
wins = 0
points_win = 0

for game in range(tournaments_number):
    result = input()
    if result == "W":
        points_win += 2000
        wins += 1
    elif result == "F":
        points_win += 1200
    elif result == "SF":
        points_win += 720

final_points = points_win + starting_points
average_points_won = points_win / tournaments_number
average_points_won = floor(average_points_won)
percent_wins = (wins / tournaments_number) * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_points_won}")
print(f"{percent_wins:.2f}%")
