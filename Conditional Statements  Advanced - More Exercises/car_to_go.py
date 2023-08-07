budged = float(input())
season = input()

car_class = ''
car_kind = ''
price = 0

if budged <= 100:
    car_class = 'Economy class'
    if season == 'Summer':
        car_kind = 'Cabrio'
        price = budged * 0.35
    elif season == 'Winter':
        car_kind = 'Jeep'
        price = budged * 0.65
elif 100 < budged <= 500:
    car_class = 'Compact class'
    if season == 'Summer':
        car_kind = 'Cabrio'
        price = budged * 0.45
    elif season == 'Winter':
        car_kind = 'Jeep'
        price = budged * 0.80
elif budged > 500:
    car_class = 'Luxury class'
    if season == 'Summer' or season == 'Winter':
        car_kind = 'Jeep'
        price = budged * 0.90

print(f"{car_class}")
print(f"{car_kind} - {price:.2f}")


