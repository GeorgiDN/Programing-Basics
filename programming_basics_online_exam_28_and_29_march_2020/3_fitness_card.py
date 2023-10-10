# https://judge.softuni.org/Contests/Practice/Index/2275#5
# Condition:https://judge.softuni.org/Contests/Practice/DownloadResource/8860

prices = {
    "m": {
        "Gym": 42,
        "Boxing": 41,
        "Yoga": 45,
        "Zumba": 34,
        "Dances": 51,
        "Pilates": 39
    },
    "f": {
        "Gym": 35,
        "Boxing": 37,
        "Yoga": 42,
        "Zumba": 31,
        "Dances": 53,
        "Pilates": 37
    },
}

budged = float(input())
sex = input()
age = int(input())
sport = input()

price = prices[sex][sport]

if age <= 19:
    price *= 0.80

if price <= budged:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    diff = abs(budged - price)
    print(f"You don't have enough money! You need ${diff:.2f} more.")
