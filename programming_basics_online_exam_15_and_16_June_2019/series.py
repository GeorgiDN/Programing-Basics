#https://judge.softuni.org/Contests/Practice/Index/1699#7

budged = float(input())
serials = int(input())
total_price = 0

for serial in range(serials):
    serial_name = input()
    serial_price = float(input())

    if serial_name == 'Thrones':
        serial_price *= 0.5
        total_price += serial_price
    elif serial_name == 'Lucifer':
        serial_price *= 0.6
        total_price += serial_price
    elif serial_name == 'Protector':
        serial_price *= 0.7
        total_price += serial_price
    elif serial_name == 'TotalDrama':
        serial_price *= 0.8
        total_price += serial_price
    elif serial_name == 'Area':
        serial_price *= 0.9
        total_price += serial_price
    else:
        total_price += serial_price

diff = abs(total_price - budged)

if budged >= total_price:
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    print(f"You need {diff:.2f} lv. more to buy the series!")
