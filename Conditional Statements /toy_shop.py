
tip_price = float(input())
puzzles = int(input())
talking_doll = int(input())
teddy_bear = int(input())
minions = int(input())
trucks = int(input())

total_number_toys = puzzles + talking_doll + teddy_bear + minions + trucks

puzzles_price = puzzles * 2.60
talking_doll_price = talking_doll * 3
teddy_bear_price = teddy_bear * 4.10
minions_price = minions * 8.20
trucks_price = trucks * 2

total_toy_price = puzzles_price + talking_doll_price + teddy_bear_price + minions_price + trucks_price


if total_number_toys >= 50:
    total_toy_price = total_toy_price - (total_toy_price * 0.25)  # = total_toy_price = total_toy_price * 0.75

rent = total_toy_price * 0.1

total_sum = total_toy_price - rent


if total_sum >= tip_price:
    money_left = total_sum - tip_price
    print(f'Yes! {money_left:.2f} lv left.')
else:
    money_left = tip_price - total_sum
    print(f'Not enough money! {money_left:.2f} lv needed.')










