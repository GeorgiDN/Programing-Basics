film_budget = float(input())
number_extras = int(input())
price_clothing_extra = float(input())

decor_price = film_budget * 0.1
sum_of_price_clothing_extra = price_clothing_extra * number_extras

if number_extras > 150:
    sum_of_price_clothing_extra *= 0.9

total_film_sum = decor_price + sum_of_price_clothing_extra


diff = abs(total_film_sum - film_budget)

if total_film_sum > film_budget:
    print(f'Not enough money!')  # moje i bez f
    print(f'Wingard needs {diff:.2f} leva more.')
else:
    print(f'Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')

