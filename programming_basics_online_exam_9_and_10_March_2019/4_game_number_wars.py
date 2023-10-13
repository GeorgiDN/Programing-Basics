# https://judge.softuni.org/Contests/Practice/Index/1538#6
#Condition:https://judge.softuni.org/Contests/Practice/DownloadResource/5345

first_player_name = input()
second_player_name = input()

first_player_points = 0
second_player_points = 0
number_of_wars = False

while True:
    if number_of_wars:
        break
    command = input()

    if command == "End of game":
        print(f"{first_player_name} has {first_player_points} points")
        print(f"{second_player_name} has {second_player_points} points")
        break

    first_player_card = int(command)
    second_player_card = int(input())

    if first_player_card > second_player_card:
        difference = first_player_card - second_player_card
        first_player_points += difference
    elif first_player_card < second_player_card:
        difference = second_player_card - first_player_card
        second_player_points += difference
    elif first_player_card == second_player_card:
        print("Number wars!")
        first_player_card = int(input())
        second_player_card = int(input())

        if first_player_card > second_player_card:
            print(f"{first_player_name} is winner with {first_player_points} points")
            number_of_wars = True
            break
        elif first_player_card < second_player_card:
            print(f"{second_player_name} is winner with {second_player_points} points")
            number_of_wars = True
            break
