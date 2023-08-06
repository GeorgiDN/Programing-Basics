budged = float(input())
ticket_cat = input()
people_num = int(input())

transport_price = 0
price = 0


if 1 <= people_num <= 4:
    transport_price = budged * 0.75
elif 5 <= people_num <= 9:
    transport_price = budged * 0.60
elif 10 <= people_num <= 24:
    transport_price = budged * 0.50
elif 25 <= people_num <= 49:
    transport_price = budged * 0.40
elif people_num >= 50:
    transport_price = budged * 0.25

if ticket_cat == 'VIP':
    price = 499.99 * people_num + transport_price
elif ticket_cat == 'Normal':
    price = 249.99 * people_num + transport_price

diff = abs(budged - price)

if budged >= price:
    print(f"Yes! You have {diff:.2f} leva left.")
elif budged < price:
    print(f"Not enough money! You need {diff:.2f} leva.")
