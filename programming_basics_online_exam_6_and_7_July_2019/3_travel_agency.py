reservation_prices = {
    "Bansko": {
        "noEquipment": 80,
        "withEquipment": 100,
    },
    "Borovets": {
        "noEquipment": 80,
        "withEquipment": 100,
    },
    "Varna": {
        "noBreakfast": 100,
        "withBreakfast": 130,
    },
    "Burgas": {
        "noBreakfast": 100,
        "withBreakfast": 130,
    }
}

cities = ["Bansko",  "Borovets", "Varna", "Burgas"]
packages = ["noEquipment",  "withEquipment", "noBreakfast", "withBreakfast"]

town = input()
package = input()
vip = input()
days = int(input())
price = 0
total_price = 0
discount = 0
invalid_condition = False

if town == "Bansko":
    if package == "noEquipment":
        discount = 0.05
    elif package == "withEquipment":
        discount = 0.1

elif town == "Borovets":
    if package == "noEquipment":
        discount = 0.05
    elif package == "withEquipment":
        discount = 0.1

elif town == "Varna":
    if package == "noBreakfast":
        discount = 0.07
    elif package == "withBreakfast":
        discount = 0.12

elif town == "Burgas":
    if package == "noBreakfast":
        discount = 0.07
    elif package == "withBreakfast":
        discount = 0.12


if days < 1:
    print("Days must be positive number!")
    invalid_condition = True
elif package not in packages or town not in cities:
    print("Invalid input!")
    invalid_condition = True
else:
    price = reservation_prices[town][package]

    if days > 7:
        days -= 1

    if vip == "yes":
        price = price - (price * discount)

if not invalid_condition:
    total_price = price * days
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
