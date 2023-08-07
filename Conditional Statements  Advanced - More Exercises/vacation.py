budged = float(input())
season = input()

location = ''
accommodation = ''
price = 0

if budged <= 1000:
    accommodation = "Camp"
    if season == 'Summer':
        location = "Alaska"
        price = budged * 0.65
    elif season == 'Winter':
        location = "Morocco"
        price = budged * 0.45
elif 1000 < budged <= 3000:
    accommodation = "Hut"
    if season == 'Summer':
        location = "Alaska"
        price = budged * 0.80
    elif season == 'Winter':
        location = "Morocco"
        price = budged * 0.60
elif budged > 3000:
    accommodation = "Hotel"
    price = budged * 0.90
    if season == 'Summer':
        location = "Alaska"
    elif season == 'Winter':
        location = "Morocco"

print(f"{location} - {accommodation} - {price:.2f}")
