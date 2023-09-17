#https://judge.softuni.org/Contests/Practice/Index/1596#1

film_budget = float(input())
extras_num = int(input())
clothing_price_per_extra = float(input())

decor = film_budget * 0.1

if extras_num > 150:
    clothing_price_per_extra *= 0.9

total_price = decor + (extras_num * clothing_price_per_extra)

if total_price <= film_budget:
    print(f'Action!\nWingard starts filming with {(film_budget - total_price):.2f} leva left.')
else:
    print(f"Not enough money!\nWingard needs {(total_price - film_budget):.2f} leva more.")
