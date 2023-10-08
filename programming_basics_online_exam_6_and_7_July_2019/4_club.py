# https://judge.softuni.org/Contests/Practice/Index/1745#4
target_sum = float(input())
club_income = 0
target_reached = False

while True:
    price = 0
    if club_income >= target_sum:
        target_reached = True
        break
    cocktail = input()

    if cocktail == "Party!":
        break

    cocktails_number = int(input())
    price_per_cocktail = len(cocktail)
    price += cocktails_number * price_per_cocktail
    if price % 2 != 0:
        price *= 0.75
    club_income += price

diff = abs(target_sum - club_income)

if target_reached:
    print("Target acquired.")
    print(f"Club income - {club_income:.2f} leva.")

elif not target_reached:
    print(f"We need {diff:.2f} leva more.")
    print(f"Club income - {club_income:.2f} leva.")
