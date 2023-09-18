ticket_prices = {
    "A Star Is Born": {
        "normal": 7.50,
        "luxury": 10.50,
        "ultra luxury": 13.50
    },
    "Bohemian Rhapsody": {
        "normal": 7.35,
        "luxury": 9.45,
        "ultra luxury": 12.75
    },
    "Green Book": {
        "normal": 8.15,
        "luxury": 10.25,
        "ultra luxury": 13.25
    },
    "The Favourite": {
        "normal": 8.75,
        "luxury": 11.55,
        "ultra luxury": 13.95
    }
}

film = input()
hall = input()
number_of_tickets = int(input())

price = ticket_prices[film][hall]
total_cost = price * number_of_tickets

print(f"{film} -> {total_cost:.2f} lv.")
