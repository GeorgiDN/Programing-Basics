month = input()
nights_num = int(input())

room_1 = ''
room_2 = ''
price_studio = 0
price_apartment = 0

if month == 'May' or month == 'October':
    room_1 = 'Studio'
    room_2 = 'Apartment'
    price_studio = 50 * nights_num
    price_apartment = 65 * nights_num
    if 7 < nights_num <= 14:
        price_studio *= 0.95
    elif nights_num > 14:
        price_studio *= 0.70
        price_apartment *= 0.9
elif month == 'June' or month == 'September':
    room_1 = 'Studio'
    room_2 = 'Apartment'
    price_studio = 75.20 * nights_num
    price_apartment = 68.70 * nights_num
    if nights_num > 14:
        price_studio *= 0.80
        price_apartment *= 0.9
elif month == 'July' or month == 'August':
    room_1 = 'Studio'
    room_2 = 'Apartment'
    price_studio = 76 * nights_num
    price_apartment = 77 * nights_num
    if nights_num > 14:
        price_apartment *= 0.9

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")
