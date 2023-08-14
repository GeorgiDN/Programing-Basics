import math
tournaments_num = int(input())
starting_points = int(input())

points = starting_points
won_tournaments = 0

for i in range(tournaments_num):
    stage_tournament = input()
    if stage_tournament == 'W':
        points += 2000
        won_tournaments += 1
    elif stage_tournament == 'F':
        points += 1200
    elif stage_tournament == 'SF':
        points += 720

average_points = (points - starting_points) / tournaments_num
percent_won_tournaments = (won_tournaments / tournaments_num) * 100


print(f"Final points: {points}")
print(f"Average points: {math.floor(average_points)}")
print(f'{percent_won_tournaments:.2f}%')
