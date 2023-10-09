name = input()
winner = ''
winner_points = 0
points = 0

while name != "Stop":
    for letter in name:
        number = int(input())
        if number == ord(letter):
            points += 10
        elif number != ord(letter):
            points += 2
    if points >= winner_points:
        winner_points = points
        winner = name
    points = 0
    name = input()

print(f"The winner is {winner} with {winner_points} points!")



# https://judge.softuni.org/Contests/Practice/Index/1745#8
# COndition: https://judge.softuni.org/Contests/Practice/DownloadResource/6166
