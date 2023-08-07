chrysanthemums_num = int(input())
roses_num = int(input())
tulips_num = int(input())
season = input()
holiday = input()

price = 0

if season == 'Spring' or season == 'Summer':
    price = (chrysanthemums_num * 2) + (roses_num * 4.10) + (tulips_num * 2.50)
    if tulips_num > 7 and season == 'Spring':
        price *= 0.95
    if (chrysanthemums_num + roses_num + tulips_num) > 20:
        price *= 0.8
elif season == 'Autumn' or season == 'Winter':
    price = (chrysanthemums_num * 3.75) + (roses_num * 4.50) + (tulips_num * 4.15)
    if roses_num >= 10 and season == 'Winter':
        price *= 0.9
    if (chrysanthemums_num + roses_num + tulips_num) > 20:
        price *= 0.8

if holiday == 'Y':
    price *= 1.15

print(f'{price + 2:.2f}')
