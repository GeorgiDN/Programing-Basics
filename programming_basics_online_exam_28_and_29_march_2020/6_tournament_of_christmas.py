# https://judge.softuni.org/Contests/Practice/Index/2275#10
#Condition https://judge.softuni.org/Contests/Practice/DownloadResource/8872

days = int(input())
wins_per_day = 0
lost_per_day = 0

win_days = 0
lost_days = 0

total_money = 0
money_per_day = 0

for day in range(days):
    while True:
        sport = input()
        if sport == "Finish":
            break

        result = input()
        if result == "win":
            money_per_day += 20
            wins_per_day += 1

        elif result == "lose":
            lost_per_day += 1

    if wins_per_day > lost_per_day:
        money_per_day += money_per_day * 0.1
        total_money += money_per_day
        win_days += 1
    elif wins_per_day < lost_per_day:
        lost_days += 1
        total_money += money_per_day

    wins_per_day = 0
    lost_per_day = 0
    money_per_day = 0

if win_days > lost_days:
    total_money += total_money * 0.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
elif win_days < lost_days:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
