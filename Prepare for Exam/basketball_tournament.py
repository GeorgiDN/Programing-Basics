tournament = input()

matches_win = 0
matches_lost = 0
total_matches = 0


while tournament != 'End of tournaments':
    matches_num = int(input())
    total_matches += matches_num
    for match in range(1, matches_num + 1):
        points_Desy_team = int(input())
        points_opposing_team = int(input())
        if points_Desy_team > points_opposing_team:
            matches_win += 1
            print(f"Game {match} of tournament {tournament}: win with {points_Desy_team - points_opposing_team} points.")
        elif points_Desy_team < points_opposing_team:
            matches_lost += 1
            print(f"Game {match} of tournament {tournament}: lost with {points_opposing_team - points_Desy_team} points.")

    tournament = input()


print(f'{(matches_win / total_matches) * 100:.2f}% matches win')
print(f'{(matches_lost / total_matches) * 100:.2f}% matches lost')
