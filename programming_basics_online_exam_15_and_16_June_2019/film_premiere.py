prices = {
    "John Wick": {
        "Drink": 12,
        "Popcorn": 15,
        "Menu": 19
    },
    "Star Wars": {
        "Drink": 18,
        "Popcorn": 25,
        "Menu": 30
    },
    "Jumanji": {
        "Drink": 9,
        "Popcorn": 11,
        "Menu": 14
    },
}

film = input()
film_package = input()
tickets = int(input())

price = prices[film][film_package]
total_price = price * tickets

if film == 'Star Wars' and tickets >= 4:
    total_price *= 0.70
elif film == 'Jumanji' and tickets == 2:
    total_price *= 0.85

print(f"Your bill is {total_price:.2f} leva.")
