#https://judge.softuni.org/Contests/Practice/Index/1538#7
#Condition:https://judge.softuni.org/Contests/Practice/DownloadResource/5347

starting_points = 301
player_name = input()
successful_shots = 0
unsuccessful_shots = 0
retire_condition = False

while True:
    if starting_points == 0:
        break
    shoot = input()
    if shoot == "Retire":
        retire_condition = True
        break
    points = int(input())

    if shoot == "Double":
        points *= 2
    elif shoot == "Triple":
        points *= 3

    if points <= starting_points:
        starting_points -= points
        successful_shots += 1
    else:
        unsuccessful_shots += 1


if retire_condition:
    print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
else:
    print(f"{player_name} won the leg with {successful_shots} shots.")
