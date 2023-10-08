# https://judge.softuni.org/Contests/Practice/Index/1745#6

Hearthstone = 0
Fornite = 0
Overwatch = 0
Others = 0

number_sold_games = int(input())
for i in range(number_sold_games):
    game = input()

    if game == "Hearthstone":
        Hearthstone += 1
    elif game == "Fornite":
        Fornite += 1
    elif game == "Overwatch":
        Overwatch += 1
    else:
        Others += 1

percent_Hearthstone = Hearthstone / number_sold_games * 100
percent_Fornite = Fornite / number_sold_games * 100
percent_Overwatch = Overwatch / number_sold_games * 100
percent_Others = Others / number_sold_games * 100

print(f"Hearthstone - {percent_Hearthstone:.2f}%\n"
      f"Fornite - {percent_Fornite:.2f}%\n"
      f"Overwatch - {percent_Overwatch:.2f}%\n"
      f"Others - {percent_Others:.2f}%")
