budged = float(input())
nights_number = int(input())
price_per_night = float(input())
additional_expenditures = int(input())

if nights_number > 7:
    price_per_night *= 0.95

nights_price = nights_number * price_per_night
percent_additional_expenditures = additional_expenditures / 100
additional_expenditures_money = budged * percent_additional_expenditures

total_price = nights_price + additional_expenditures_money

diff = abs(budged - total_price)

if budged >= total_price:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")
  
