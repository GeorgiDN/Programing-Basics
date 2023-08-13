actor = input()
academy_points = float(input())
appraiser_num = int(input())

points = 0

for i in range(appraiser_num):
    appraiser_name = input()
    appraiser_points = float(input())
    academy_points += len(appraiser_name) * appraiser_points / 2
    if academy_points > 1250.5:
        break

diff = abs(1250.5 - academy_points)
if academy_points < 1250.5:
    print(f"Sorry, {actor} you need {diff:.1f} more!")
else:
    print(f"Congratulations, {actor} got a nominee for leading role with {academy_points:.1f}!")

