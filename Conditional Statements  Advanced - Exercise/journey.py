budget = float(input())
season = input()

price = 0
destination = ''
place_rest = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        price = budget * 0.3
        place_rest = 'Camp'
    elif season == 'winter':
        price = budget * 0.7
        place_rest = 'Hotel'
elif 100 < budget <= 1000:
    if season == 'summer':
        price = budget * 0.4
        place_rest = 'Camp'
    elif season == 'winter':
        price = budget * 0.8
        place_rest = 'Hotel'
elif budget > 1000:
    destination = 'Europe'
    price = budget * 0.9
    place_rest = 'Hotel'

print(f"Somewhere in {destination}")
print(f"{place_rest} - {price:.2f}")
