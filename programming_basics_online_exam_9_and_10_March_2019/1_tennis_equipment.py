# https://judge.softuni.org/Contests/Practice/Index/1538#0
# Condition:https://judge.softuni.org/Contests/Practice/DownloadResource/19353

from math import ceil, floor
tennis_rocket_price = float(input())
tennis_rocket_number = int(input())
part_sneakers_number = int(input())

part_sneakers_price = tennis_rocket_price / 6

total_price_tennis_rocket = tennis_rocket_number * tennis_rocket_price
total_price_sneakers = part_sneakers_number * part_sneakers_price
price_rest_equipment = (total_price_tennis_rocket + total_price_sneakers) * 0.2
total_price = total_price_tennis_rocket + total_price_sneakers + price_rest_equipment

price_for_djokovic = total_price / 8
price_for_sponsors = total_price * 7/8

price_for_djokovic = floor(price_for_djokovic)
price_for_sponsors = ceil(price_for_sponsors)

print(f"Price to be paid by Djokovic {price_for_djokovic}")
print(f"Price to be paid by sponsors {price_for_sponsors}")
