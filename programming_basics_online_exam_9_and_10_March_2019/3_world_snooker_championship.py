# https://judge.softuni.org/Contests/Practice/Index/1538#5
# Condition:https://judge.softuni.org/Contests/Practice/DownloadResource/5343

prices = {
    "Standard": {
        "Quarter final": 55.50,
        "Semi final": 75.88,
        "Final": 110.10
    },
    "Premium": {
        "Quarter final": 105.20,
        "Semi final": 125.22,
        "Final": 160.66
    },
    "VIP": {
        "Quarter final": 118.90,
        "Semi final": 300.40,
        "Final": 400
    },
}


championship_stage = input()
ticket = input()
ticket_number = int(input())
picture_options = input()

price = prices[ticket][championship_stage]
price *= ticket_number
total_price = price
price_for_picture_per_ticket = 40 * ticket_number

if price > 4000:
    total_price = price * 0.75
elif 2500 < price <= 4000:
    total_price = price * 0.90

if picture_options == "Y" and price <= 4000:
    total_price += price_for_picture_per_ticket

print(f"{total_price:.2f}")
