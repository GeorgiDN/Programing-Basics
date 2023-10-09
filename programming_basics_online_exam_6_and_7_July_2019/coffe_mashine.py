drink_prices = {
    "Without": {
        "Espresso": 0.9,
        "Cappuccino": 1,
        "Tea": 0.5
    },
    "Normal": {
        "Espresso": 1,
        "Cappuccino": 1.20,
        "Tea": 0.60
    },
    "Extra": {
        "Espresso": 1.20,
        "Cappuccino": 1.60,
        "Tea": 0.70
    }
}

drink = input()
sugar_quantity = input()
number_drinks = int(input())

total_price = drink_prices[sugar_quantity][drink] * number_drinks

if sugar_quantity == "Without":
    total_price *= 0.65
if drink == "Espresso" and number_drinks >= 5:
    total_price *= 0.75
if total_price > 15:
    total_price *= 0.80

print(f"You bought {number_drinks} cups of {drink} for {total_price:.2f} lv.")




#https://judge.softuni.org/Contests/Practice/Index/1745#2
#Conditions:https://judge.softuni.org/Contests/Practice/DownloadResource/6154
