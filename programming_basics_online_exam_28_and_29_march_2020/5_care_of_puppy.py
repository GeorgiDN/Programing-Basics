# https://judge.softuni.org/Contests/Practice/Index/2275#8
# Condition:https://judge.softuni.org/Contests/Practice/DownloadResource/8866

food_kg = int(input())
food_gr = food_kg * 1000

command = input()

while command != "Adopted":
    food_eaten = int(command)
    food_gr -= food_eaten
    command = input()

if food_gr >= 0:
    print(f"Food is enough! Leftovers: {food_gr} grams.")
else:
    print(f"Food is not enough. You need {abs(food_gr)} grams more.")
  
